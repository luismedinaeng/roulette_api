#!/usr/bin/python3

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

	def __init__(self, id, token, value, user_id):
		self.id = id 
		self.token = token
		self.value = value
		self.__user_id = user_id
		self.__status = Bet.WAITING 

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, id):
		self.__id = id

	@property
	def token(self):
		return self.__token

	@token.setter
	def token(self, token):
		if token in [Bet.BLACK_TOKEN, Bet.RED_TOKEN] or token in range(Bet.MIN_TOKEN, Bet.MAX_TOKEN + 1):
			self.__token = token
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
