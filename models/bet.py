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

	def __init__(self, id=None, token, value, user_id, status):		
		self.id = id if id else str(uuid.uuid4())
		self.token = token
		self.value = value
		self.__user_id = user_id
		self.status = WAITING 

	@property
	def id(self):
		return self.id

	@id.setter
	def id(self, id):
		self.id = id

	@property
	def token(self):
		return self.__token

	@token.setter
	def token(self, token):
		if token in [BLACK_TOKEN, RED_TOKEN] or token in range(MIN_TOKEN, MAX_TOKEN + 1):
			self.__token = token
		else:
			raise ValueError("The bet is not in the limits")

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, new_value):
		if new_value > MAX_VALUE:
			raise ValueError("Value of the bet should be less than 10.000 USD")
		else:
			self.__value = new_value

	@property
	def user_id(self):
		return self.__user_id

