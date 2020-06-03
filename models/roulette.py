#!/usr/bin/python3

import random
import uuid
from models.bet import Bet

class Roulette():
	
	OPEN = 0
	CLOSE = 1
	WITHOUT_RESULT = -1

	def __init__(self, id):
		self.id = id if id else str(uuid.uuid4())
		self.status = OPEN
		self.bets = []
		self.__result = WITHOUT_RESULT

	@property
	def id(self):
		return self.__id
	
	@id.setter
	def if(self, id):
		self.__id = id

	@property
	def status(self):
		return self.status

	@status.setter
	def status(self, status):
		self.__status = status

	@property
	def bets(self):
		return bets

	def add_bet(self, new_bet):
		self.__bets.append(new_bet)
	
	def delete_bet(self, bet_id):
		for bet in self.__bets:
			if bet.id == bet_id:
				self.__bets.remove(bet)
				break

	def clean(self):
		self.__bets.clear()

	def open(self):
		if self.status = CLOSE:
			self.clean()
			self.result = WITHOUT_RESULT
			self.status = OPEN
			
	def close(self):
		if self.status = OPEN:
			number = random.randrange(Bet.MIN_TOKEN, Bet.MAX_TOKEN)
			color = get_color_of_result(number)
			self.__result = (number, color)

	@staticmethod
	def get_color_of_result(result):
		black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
		red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
		if number in black_numbers.
			color = Bet.BLACK_TOKEN
		else:
			color = Bet.RED_TOKEN
		
		return color
