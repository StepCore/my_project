from unittest.mock import patch
from unittest.mock import Mock

from src.utils import json_data
import pytest

from ..src.external_api import converter_value, return_sum_transaction


def test_return_sum_transaction(out_list_transaction):
    assert return_sum_transaction() == out_list_transaction


def test_converter_value():
    mock_converter = Mock(return_value="9824.07")
    converter_value = mock_converter
    assert converter_value == "9824.07"
    mock_converter.assert_called_once_with()


def test_converter_value_2():
    with patch('requests.request') as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75.56}
        mock_request.return_value = mock_response

        list_transaction = ["100 USD"]

        assert converter_value()[0] == 75.56
