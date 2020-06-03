#!/usr/bin/python3

from flask import Flask, make_response, jsonify, request, abort
import models
from models.bet import Bet
from models.roulette import Roulette

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(404)
def endpoint_not_found(error):
	content = jsonify({'error': 'Not found'})
	return make_response(content, 404)

@app.route('/')
def index():
	content = jsonify({'status': 'OK'})
	return make_response(content, 200)

@app.route('/roulettes', methods=['GET'])
def get_roulettes():
	roulettes = models.casino.all(Roulette).values()
	list_roulettes = []	
	for roulette in roulettes:
		list_roulettes.append(roulette.to_dict())
	content = jsonify(list_roulettes)
	return make_response(content, 200)

@app.route('/new_roulette')
@app.route('/roulettes', methods=['POST'])
def new_roulette():
	instance = Roulette()
	instance.save()
	print
	content = jsonify({'id_roulette': instance.id})
	return make_response(content, 200)

@app.route('/roulettes/<id>/open', methods=['GET'])	
def open_roulette(id):
	roulette = models.casino.get(Roulette, id)
	roulette.open()
	content = jsonify({'estado_roulette': roulette.status})
	return make_response(content, 200)
	
@app.route('/roulettes/<id>/close', methods=['GET'])	
def close_roulette(id):
	roulette = models.casino.get(Roulette, id)
	list_bets = []
	for bet in roulette.bets():
		list_bets.append(bet)
	content = jsonify(list_bets)
	return make_response(content, 200)

def check_json_bet(request):
	description = ""
	if not request.get_json():
	   description = "Not a JSON"
	elif 'user_id' not in request.get_json():
		description = "missing user_id"
	elif 'token' not in request.get_json():
		description = "Missing token"
	elif 'value' not in request.get_json():
		description = "Missing bet value"
	return description

@app.route('/roulettes/<id>/bet', methods=['POST'])
def create_bet(id):
	roulette = models.casino.get(Roulette, id)
	if roulette.status == Roulette.CLOSE:
		content = jsonify({'error': 'Closed roullette'})
		return make_response(content, 403)
	description = check_json_bet(request)
	if description != "":
		content = jsonify({'error': description})
		return make_response(content, 400)
	data = request.get_json()
	data['roulette_id'] = id
	try:
		bet = Bet(**data)
		bet.save()
	except:
		abort(400, description="Too many args")

if __name__ == '__main__':
	host = '0.0.0.0'
	port = 5000	
	app.run(host=host, port=port, debug=True)

