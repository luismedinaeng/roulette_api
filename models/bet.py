#!/usr/bin/python3

import models
import uuid

class Bet():
	
	BLACK_TOKEN = -1
	RED_TOKEN = -2
	MIN_TOKEN = 0
	MAX_TOKEN = 36
	MAX_VALUE = 10000
	WAITING = 0
	WIN = 1
	LOSE = 2

	def __init__(self, token, value, user_id, roulette_id, id=None, status=None):
		self.token = token
		self.value = value
		self.__user_id = user_id
		self.__roulette_id = roulette_id
		self.__id = id if id else str(uuid.uuid4())
		self.__status = status if status else Bet.WAITING		
		self.save()

	@property
	def id(self):
		return self.__id

	@property
	def token(self):
		return self.__token

	@token.setter
	def token(self, token):
		if token in [Bet.BLACK_TOKEN, Bet.RED_TOKEN] or token in range(Bet.MIN_TOKEN, Bet.MAX_TOKEN + 1):
			self.__token = token
			self.save()
		else:
			raise ValueError("The bet is not in the limits")

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if new_value > Bet.MAX_VALUE:
			raise ValueError("Value of the bet should be less than 10.000 USD")
		else:
			self.__value = new_value
			self.save()

	@property
	def user_id(self):
		return self.__user_id

	@property
	def status(self):
		return self.__status
	
	def update_status(self, result):
		if self.token == result["color"] or self.token == result["number"]:
			self.__status = Bet.WIN
		else:
			self.__status = Bet.LOSE
		self.save()

	def to_dict(self):
		new_dict = {}
		for key, value in self.__dict__.items():
			new_key = key.split('__')[-1]
			new_dict[new_key] = value

		return new_dict

	def save(self):
		models.casino.new(self)
		models.casino.save()
