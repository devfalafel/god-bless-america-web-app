import json
from flask import Flask, request, render_template
from utils.network_utils import NetworkUtils
from utils.token_utils import TokenUtils


class PlayerUtils:
	@staticmethod
	def add_player(data, player_name, player_pw, ip_address) -> dict:
	
		if len(data.values()) <8:
			ip_info = NetworkUtils.get_ip_info(ip_address)
			data[player_name] = {
				"player_name": player_name,
				"player_pw": player_pw,
				"player_ip": ip_info["ip"],
				"player_country": ip_info["country"]
			}
			
		return data
		
	@staticmethod
	def remove_player(data, player_name, player_pw) -> dict:
	
		if data:
			for player,player_info in data.items():
				if ((player_info["player_name"] == player_name) and (player_info["player_pw"] == player_pw)) or \
					((player_info["player_name"] == player_name) and player_pw == TokenUtils.get_admin_creds()):
					data.pop(player)
					break
				
		return data
	
	@staticmethod
	def remove_all_player(data, player_pw) -> dict:
		if data and player_pw == TokenUtils.get_admin_creds():
			data = {}		
		return data