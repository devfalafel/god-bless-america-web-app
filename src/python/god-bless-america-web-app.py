from flask import Flask, request, render_template
import json
from utils.player_utils import PlayerUtils

app = Flask(__name__)

@app.route('/')
def god_bless_america_web_app():
    return render_template("home.html")

@app.route('/get-players', methods=['GET'])
def get_players():
	# input sanitizer
	
    with open('./data/players-data.json') as f:
    data = json.load(f)
	return render_template('displayPlayers.html', results=data)
		
@app.route('/post-player', methods=['POST'])
def post_player(player_name, player_pw):
	# input sanitizer
	
    with open('./data/players-data.json') as f:
		data = json.load(f)
	data = PlayerUtils.add_player(data, player_name, player_pw, request.remote_addr)
	return render_template('displayPlayers.html', results=data)

@app.route('/delete-player', methods=['DELETE'])
def delete_player(player_name, player_pw):
	# input sanitizer
	
    with open('./data/players-data.json') as f:
		data = json.load(f)
	data = PlayerUtils.remove_player(data, player_name, player_pw, request.remote_addr)
	return render_template('displayPlayers.html', results=data)
	
@app.route('/delete-all-players', methods=['DELETE'])
def delete_all_players():
	# input sanitizer
	
    with open('./data/players-data.json') as f:
		data = json.load(f)
	data = PlayerUtils.remove_all_player(data, player_pw)
	return render_template('displayPlayers.html', results=data)
	
if __name__ == "__main__":
	print("main(): Launching GodBlessAmerica Web Application")
	app.run(host="0.0.0.0", port=8000, debug=True)