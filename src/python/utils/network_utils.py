import json
import requests


class NetworkUtils:
	@staticmethod
	def get_ip_info(ip_address):
		#response = requests.get(f"https://geolocation-db.com/json/{ip_address}&position=true").json()
		# location_data = {
			# "ip": ip_address,
			# "country": response.get("country_name")
		# }
		location_data = {
			"ip": ip_address,
			"country": "United States"
		}
		print(f"get_ip_info(): {location_data}")
		return location_data
	