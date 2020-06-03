#!/usr/bin/python3

from models.bet import Bet
import unittest

class TestBet(unittest.TestCase):
	
	def setUp(self):
		self.bet1 = Bet(id="2", token=Bet.BLACK_TOKEN, value=5000, user_id="1357")
		self.bet2 = Bet(id="3",token=30, value=5000, user_id="1357") 

	def test_instatiation(self):
		self.assertEqual(self.bet1.id, "2")
		self.assertEqual(self.bet1.token, Bet.BLACK_TOKEN, msg="The bet1 token is not black")
		self.assertEqual(self.bet1.value, 5000)
		self.assertEqual(self.bet1.user_id, "1357")
	
	def test_value_setter(self):
		with self.assertRaises(ValueError):
			self.bet1.value = 80000

	def test_token_setter(self):
		with self.assertRaises(ValueError):
			self.bet2.token = Bet.MAX_TOKEN + 1

	def test_status(self):
		self.assertEqual(self.bet1.status, Bet.WAITING)
		result = {'number': 29, 'color': Bet.BLACK_TOKEN}
		self.bet1.update_status(result)
		self.bet2.update_status(result)
		self.assertEqual(self.bet1.status, Bet.WIN)
		self.assertEqual(self.bet2.status, Bet.LOSE)
