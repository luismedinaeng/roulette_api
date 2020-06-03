#!/usr/bin/python3
from models.bet import Bet
import models
import random
import redis
import uuid

class Roulette():
	
	OPEN = 'open'
	CLOSE = 'close'
	WITHOUT_RESULT = {} 

	def __init__(self, id=None, status=None, result=None, number_bets=0):
		self.__id = id if id else str(uuid.uuid4())
		self.__status = status if status else Roulette.CLOSE
		self.__number_bets = number_bets
		self.__result = result if result else Roulette.WITHOUT_RESULT
		self.save()

	@property
	def id(self):
		return self.__id
	
	@property
	def status(self):
		return self.__status

	@property
	def bets(self):
		all_bets = models.casino.all(Bet)
		actual_bets = []
		for key, obj in all_bets.items():
			if self.id == obj.roulette_id:
				actual_bets.append(obj)

		return actual_bets

	@property
	def number_bets(self):
		return self.__number_bets

	@property
	def result(self):
		return self.__result

	def add_bet(self, new_bet):
		if self.__status == Roulette.OPEN:
			new_bet.save()
			self.__number_bets += 1
			models.casino.add_bet_to_roulette(self)
			return True
		else:
			return False
		self.save()

	def delete_bet(self, bet):
		bet.delete()
		self.__number_bets -= 1
		models.casino.delete_bet_to_roulette(self)
		self.save()

	def clean(self):
		bets = models.casino.all(Bet).values()
		for bet in bets:
			if bet.roulette_id == self.__id:
				delete_bet(bet)
		self.save()

	def open(self):
		if self.status == Roulette.CLOSE:
			self.clean()
			self.__result = Roulette.WITHOUT_RESULT
			self.__status = Roulette.OPEN
			self.save()

	def close(self):
		if self.status == Roulette.OPEN:
			while True:
				try:
					models.casino.watch_roulette_counter(self)
					number = random.randrange(Bet.MIN_TOKEN, Bet.MAX_TOKEN)
					color = Roulette.get_color_of_result(number)
					self.__result = {'number': number, 'color': color}
					self.save()
					self.close_bets()
					break
				except redis.WatchError:
					pass
			models.casino.unwatch()

	def close_bets(self):
		for bet in self.__bets:
			bet.update_status(self.__result)

	def to_dict(self):
		new_dict = {}
		for key, value in self.__dict__.items():
			new_key = key.split('__')[-1]
			new_dict[new_key] = value

		return new_dict

	@staticmethod
	def get_color_of_result(result):
		black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
		red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
		if result in black_numbers:
			color = Bet.BLACK_TOKEN
		else:
			color = Bet.RED_TOKEN
		
		return color

	def save(self):
		models.casino.new(self)
		models.casino.save()

	def delete(self):
		models.casino.delete(self)
