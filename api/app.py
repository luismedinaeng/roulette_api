#!/usr/bin/python3

from flask import Flask, make_response, jsonify
import models
from models.bet import Bet
from models.roulette import Roulette

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(404)
def endpoint_not_found():
	content = jsonify({'error': 'Not found'})
	return make_response(content, 404)

@app.route('/')
def index():
	content = jsonify({'status': 'OK'})
	return make_response(content, 200)
	
@app.route('/ruletas', methods=['GET'])
def get_roulettes():
	roulettes = models.casino.all(Roulette).values()
	list_roulettes = []	
	for roulette in roulettes:
		list_roulettes.append(roulette.to_dict())
	content = jsonify(list_roulettes)
	return make_response(content, 200)

@app.route('/ruletas', methods=['POST'])
def new_roulette():
	instance = Roulette()
	instance.save()
	print
	content = jsonify({'id_ruleta': instance.id})
	return make_response(content, 200)
		




if __name__ == '__main__':
	host = '0.0.0.0'
	port = 5000	
	app.run(host=host, port=port, debug=True)

