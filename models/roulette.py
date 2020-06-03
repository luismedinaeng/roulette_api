#!/usr/bin/python3
from models.bet import Bet
import random
import uuid

class Roulette():
	
	OPEN = 0
	CLOSE = 1
	WITHOUT_RESULT = {} 

	def __init__(self, id=None, status=None, result=None, bets=[]):
		self.__id = id if id else str(uuid.uuid4())
		self.__status = status if status else Roulette.CLOSE
		self.bets = bets
		self.__result = result if result else Roulette.WITHOUT_RESULT

	@property
	def id(self):
		return self.__id
	
	@id.setter
	def id(self, id):
		self.__id = id

	@property
	def status(self):
		return self.__status

	@status.setter
	def status(self, status):
		self.__status = status

	@property
	def bets(self):
		return self.__bets

	@property
	def result(self):
		return self.__result

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
		if self.status == Roulette.CLOSE:
			self.clean()
			self.result = Roulette.WITHOUT_RESULT
			self.status = Roulette.OPEN
			
	def close(self):
		if self.status == Roulette.OPEN:
			number = random.randrange(Bet.MIN_TOKEN, Bet.MAX_TOKEN)
			color = get_color_of_result(number)
			self.__result = {'number': number, 'color': color}
			self.close_bets()

	def close_bets(self):
		for bet in self.__bets:
			bet.update_status(self.__result)

	@staticmethod
	def get_color_of_result(result):
		black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
		red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
		if number in black_numbers:
			color = Bet.BLACK_TOKEN
		else:
			color = Bet.RED_TOKEN
		
		return color
