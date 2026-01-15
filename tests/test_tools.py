from unittest.mock import patch, MagicMock
from src.tools import calculator_func, weather_tool, get_tools

# --- Calculator Tests ---


def test_calculator_basic_math():
    result = calculator_func("10*5")
    # Updated to match the new label format
    assert "Calculation Result: 50" in result


def test_calculator_complex_expression():
    result = calculator_func("(2+2)*10/4")
    assert "Calculation Result: 10.0" in result


def test_calculator_sanitization():
    """Ensures non-math characters are stripped from input."""
    result = calculator_func("10abc+5")
    assert "Calculation Result: 15" in result


def test_calculator_invalid_input():
    result = calculator_func("hello world")
    # Updated to match the new "Error - Invalid input" string
    assert "Invalid input" in result


def test_calculator_division_by_zero():
    result = calculator_func("10/0")
    assert "Calculation error" in result


# --- Weather Tool Tests ---


@patch("src.tools.api_key", None)
def test_weather_tool_missing_api_key():
    result = weather_tool("London")
    assert "Configuration Error" in result


@patch("src.tools.requests.get")
@patch("src.tools.api_key", "fake_key_123")
def test_weather_tool_success(mock_requests):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "main": {"temp": 25.5},
        "weather": [{"description": "clear sky"}],
    }
    mock_requests.return_value = mock_response

    result = weather_tool("Sao Paulo")

    assert "Weather Data" in result
    assert "25.5°C" in result
    assert "clear sky" in result


@patch("src.tools.requests.get")
@patch("src.tools.api_key", "fake_key_123")
def test_weather_tool_input_cleanup(mock_requests):
    """Tests if 'Action Input:' prefix is correctly removed."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "main": {"temp": 20},
        "weather": [{"description": "cloudy"}],
    }
    mock_requests.return_value = mock_response

    result = weather_tool("Action Input: Paris")

    args, kwargs = mock_requests.call_args
    assert kwargs["params"]["q"] == "Paris"
    assert "Paris" in result


@patch("src.tools.requests.get")
@patch("src.tools.api_key", "fake_key_123")
def test_weather_tool_api_error(mock_requests):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"message": "city not found"}
    mock_requests.return_value = mock_response

    result = weather_tool("Narnia")

    assert "Weather API Error" in result
    assert "city not found" in result


# --- Tool Configuration Tests ---


def test_get_tools_structure():
    tools = get_tools()

    assert len(tools) == 2
    tool_names = [t.name for t in tools]
    assert "Calculator" in tool_names
    assert "Weather" in tool_names
