import json
import unittest
import mock
from utils.network_utils import NetworkUtils

class TestNetworkUtils(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.holder = 0

	def test_get_ip_info(self):
		ip = "64.233.160.0"
		returned_res = NetworkUtils.get_ip_info(ip)
		expected_res = "United States"
		self.assertEqual(returned_res["country"], expected_res)
	