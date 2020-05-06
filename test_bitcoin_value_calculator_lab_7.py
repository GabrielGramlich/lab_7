import unittest, json
from unittest import TestCase
from unittest.mock import patch

import bitcoin_value_calculator_lab_7

class TestBitcoinCalculator(TestCase):

	def test_api_call_returns_json(self):
		'''
		 Test isn't part of lab, just wanted to be thorough, and see if this would work
		 Spolier alert: it didn't
		'''
		data = bitcoin_value_calculator_lab_7.get_current_BTC_data()
		result = TestBitcoinCalculator.json_helper(data)
		self.assertTrue(result)

	def json_helper(data):
		try:
			json.loads(data)
		except:
			return False
		return True

	@patch('bitcoin_value_calculator_lab_7.get_current_BTC_data')
	def test_parse_BTC_value(self, mock_get_BTC_value):
		mock_data = [{"time":{"updated":"May 5, 2020 19:13:00 UTC","updatedISO":"2020-05-05T19:13:00+00:00","updateduk":"May 5, 2020 at 20:13 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"8,934.0311","description":"United States Dollar","rate_float":8934.0311},"GBP":{"code":"GBP","symbol":"&pound;","rate":"7,173.0978","description":"British Pound Sterling","rate_float":7173.0978},"EUR":{"code":"EUR","symbol":"&euro;","rate":"8,239.7497","description":"Euro","rate_float":8239.7497}}}]
		mock_get_BTC_value.side_effect = mock_data
		value = bitcoin_value_calculator_lab_7.get_BTC_value()
		self.assertEqual(8934.0311, value)

	@patch('builtins.print')
	def test_display_BTC_value(self, mock_print):
		bitcoin_value_calculator_lab_7.display_BTC_value(8934.0311)
		mock_print.assert_called_once_with('1 bitcoin is equivalent to $8934.03')


if __name__ == '__main__':
    unittest.main()
