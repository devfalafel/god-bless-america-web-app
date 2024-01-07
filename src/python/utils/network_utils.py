import json
import requests


class NetworkUtils:
	@staticmethod
	def get_ip_info(ip_address):
		response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
		location_data = {
			"ip": ip_address,
			"country": response.get("country_name")
		}
		print(f"get_ip_info(): {location_data}")
		return location_data
	