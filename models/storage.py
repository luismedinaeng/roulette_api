#!/usr/bin/python3

import json
from models.roulette import Roulette
from models.bet import Bet
from os import getenv
import redis

classes = {Roulette, Bet}

class Storage:
	__engine = None
	__objects = {}

	def __init__(self):
		host = getenv("ROULETTE_DB_HOST")
		port = getenv("ROULETTE_DB_PORT")
		db = getenv("ROULETTE_DB")
		test = getenv("ROULETTE_ENV")
		if not host:
			host = 'localhost'
		if not port:
			port = '6379'
		if test and test == 'test':
			db = 15
		elif not db:
			db = 0
		self.__engine = redis.Redis(host=host, port=port, db=db)

	def all(self, cls=None):
		if cls is not None:
			new_dict = {}
			for key, value in self.__objects.items():
				if cls.__name__ == key.split(":")[0]:
					new_dict[key] = value
			return new_dict
		return self.__objects

	def new(self, obj):
		if obj is not None:
			key = obj.__class__.__name__ + ":" + obj.id
			self.__objects[key] = obj

	def save(self):
		with self.__engine.pipeline() as pipe:
			for key, value in self.__objects.items():
				pipe.set(key, json.dumps(value.to_dict()))		
			pipe.execute()

	def reload(self):
		for cls in classes:
			byte_keys = self.__engine.keys(cls.__name__ + "*")
			for bkey in byte_keys:
				key = bkey.decode("utf-8")
				json_element = json.loads(self.__engine.get(key).decode("utf-8"))
				self.__objects[key] = cls(**json_element)

	def delete(self, obj=None):
		if obj is not None:
			key = obj.__class__.__name__ + ":" + obj.id
			if key in self.__objects:
				del self.__objects[key]

	def get(self, cls, id):
		if cls not in classes:
			return None

		all_cls = self.all(cls)
		for value in all_cls.values():
			if (value.id == id):
				return value

		return None

	def watch_object(self, obj):
		key = obj.__class__.__name__ + ":" + obj.id		
		self.__engine.watch(key)	

	def unwatch(self):
		self.__engine.unwatch()
