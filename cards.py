import random


class Card: 
	def __init__(self, value=2, suit="Clubs"):
		self.value = value
		self.suit = suit
		if value == 2: 
			self.name = "Two"
		elif value == 3: 
			self.name = "Three"
		elif value == 4: 
			self.name = "Four"
		elif value == 5: 
			self.name = "Five"
		elif value == 6: 
			self.name = "Six"
		elif value == 7: 
			self.name = "Seven"
		elif value == 8: 
			self.name = "Eight"
		elif value == 9: 
			self.name = "Nine"
		elif value == 10: 
			self.name = "Ten"
		elif value == 11: 
			self.name = "Jack"
		elif value == 12: 
			self.name = "Queen"
		elif value == 13: 
			self.name = "King"
		elif value == 14: 
			self.name = "Ace"
		else: 
			self.name = "NULL"
		
	def printCard(self): 
		print(self.name, "of", self.suit)
		
class Deck: 
	def __init__ (self):
		self.size = 52
		self.cards = []	
		for x in range(self.size):
			if x+1 < 14: 
				suit = "Clubs"
			elif x+1 < 27: 
				suit = "Diamonds"
			elif x+1 < 40: 
				suit = "Spades"
			elif x+1 < 53: 
				suit = "Hearts"
			else: 
				suit = "NULLS"
			self.cards.append(Card(x % 13 + 2, suit))
	
	def printCards(self): 
		for x in range(self.size): 
			self.cards[x].printCard()
	
	def shuffle(self): 
		print("\nShuffling...\n")
		random.shuffle(self.cards)

		
		
