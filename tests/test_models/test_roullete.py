#!/usr/bin/python3

from models.bet import Bet
from models.roulette import Roulette
import unittest

class TestRoulette(unittest.TestCase):
	
	def setUp(self):
		self.roulette = Roulette()
		
	
	def test_instatiation(self):
		self.assertNotEqual(self.roulette.id, "")
		self.assertEqual(self.roulette.status, Roulette.CLOSE)
		self.assertEqual(self.roulette.bets, [])
		self.assertEqual(self.roulette.result, Roulette.WITHOUT_RESULT)

	def test_add_bet(self):
		bet1 = Bet(id="1", token=Bet.BLACK_TOKEN, value=5000, user_id="1357")
		bet2 = Bet(id="2",token=30, value=5000, user_id="1357")
		self.roulette.add_bet(bet1)
		self.assertEqual(len(self.roulette.bets), 1)		
		self.roulette.add_bet(bet2)
		self.assertEqual(len(self.roulette.bets), 2)		
		
	def test_delete_bet(self):
		bet1 = Bet(id="1", token=Bet.BLACK_TOKEN, value=5000, user_id="1357")
		bet2 = Bet(id="2",token=30, value=5000, user_id="1357")
		self.roulette.add_bet(bet1)
		self.roulette.add_bet(bet2)
		self.assertEqual(len(self.roulette.bets), 2)		
		self.roulette.delete_bet(bet1.id)
		self.assertEqual(len(self.roulette.bets), 1)
		bet_left = self.roulette.bets[0]
		self.assertEqual(bet2, bet_left)

	def test_clean(self):
		bet1 = Bet(id="1", token=Bet.BLACK_TOKEN, value=5000, user_id="1357")
		bet2 = Bet(id="2",token=30, value=5000, user_id="1357")
		self.roulette.add_bet(bet1)
		self.roulette.add_bet(bet2)
		self.assertEqual(len(self.roulette.bets), 2)		
		self.roulette.clean()
		self.assertEqual(len(self.roulette.bets), 0)
		self.assertEqual(self.roulette.bets, [])
		

		
