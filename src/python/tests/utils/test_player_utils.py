import unittest
import mock
from utils.network_utils import NetworkUtils
from utils.player_utils import PlayerUtils

class TestPlayerUtils(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.mocked_req = {
			"ip": "127.0.0.2",
			"country": "United States"
		}
	
	@mock.patch("utils.network_utils.NetworkUtils.get_ip_info")
	def test_add_player(self, mocked_req):
		mocked_req.return_value = self.mocked_req
		data = {
			"dizzy": {
				"player_name": "dizzy",
				"player_pw": "123",
				"player_ip": "127.0.0.0",
				"player_country": "United States"
			},
			"sunshine": {
				"player_name": "sunshine",
				"player_pw": "1000",
				"player_ip": "127.0.0.1",
				"player_country": "United States"
			}
		}
		returned_res = PlayerUtils.add_player(data, "tino", "555", "127.0.0.2")
		expected_res = {
			"dizzy": {
				"player_name": "dizzy",
				"player_pw": "123",
				"player_ip": "127.0.0.0",
				"player_country": "United States"
			},
			"sunshine": {
				"player_name": "sunshine",
				"player_pw": "1000",
				"player_ip": "127.0.0.1",
				"player_country": "United States"
			},
			"tino": { 
				"player_name": "tino",
				"player_pw": "555",
				"player_ip": "127.0.0.2",
				"player_country": "United States"
			}
		}

		self.assertEqual(returned_res, expected_res)
		
	@mock.patch("utils.network_utils.NetworkUtils.get_ip_info")
	def test_remove_player_admin(self, mocked_req):
		mocked_req.return_value = self.mocked_req
		data = { 
			"dizzy": {
				"player_name": "dizzy",
				"player_pw": "123",
				"player_ip": "127.0.0.0",
				"player_country": "United States"
			},
			"sunshine": {
				"player_name": "sunshine",
				"player_pw": "1000",
				"player_ip": "127.0.0.1",
				"player_country": "United States"
			},
			"tino": { 
				"player_name": "tino",
				"player_pw": "555",
				"player_ip": "127.0.0.2",
				"player_country": "United States"
			}
		}
		returned_res = PlayerUtils.remove_player(data, "tino", "999")
		expected_res = {
			"dizzy": {
				"player_name": "dizzy",
				"player_pw": "123",
				"player_ip": "127.0.0.0",
				"player_country": "United States"
			},
			"sunshine": {
				"player_name": "sunshine",
				"player_pw": "1000",
				"player_ip": "127.0.0.1",
				"player_country": "United States"
				
			}
		}
			
		self.assertEqual(returned_res, expected_res)

		