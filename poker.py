from cards import *
import random

#play poker

def dealHand(self): 
	#print("Dealing hand...")
	hand = (self.cards.pop(), self.cards.pop())
	return hand

setattr(Deck, "dealHand", dealHand)
	
class Player: 
	def __init__(self, chips, name, human): 
		self.chips = chips
		self.currentBet = 0
		self.name = name
		self.human = human
	
	def printPlayer(self): 
		print("playerName:", self.name)
		print("Chips:", self.chips)
		print("Human?:", self.human)
	
	def showHand(self): 
		self.hand[0].printCard()
		self.hand[1].printCard()
		print()
		
	def bet(self, amount):
		if self.chips >= amount & amount > 0: 
			self.chips = self.chips - amount
			self.currentBet = amount
		else: 
			print("not a valid bet, no action taken.")
			print("Player chips:", self.chips, "Amount bet: ", amount)

	def hasCard(self, card): 
		print("Looking at hand")
		if self.hand[0].name == card: 
			return True
		elif self.hand[1].name == card:
			return True
		else:
			return False
	
	def checkValue(self): 
		print("Looking at card values")
		return self.hand[0].value + self.hand[1].value
	
	def checkSuits(self):
		if self.hand[0].suit == self.hand[1].suit: 
			print("Hand is suited!")
			return True
		else: 
			print("Hand is not suited :(")
			return False
		
	def checkPair(self): 
		if self.hand[0].value == self.hand[1].value: 
			return True
		else: 
			return False
	
	def evaluateHandStrength(self): 
		#open any pocket pair
		if self.checkPair(): 
			return True 
		

class Seat: 
	def __init__(self, name): 
		self.name = name
		self.occupied = False
		self.bb = False
		self.sb = False
		self.btn = False
	
	def printSeat(self): 
		print("seatName:", self.name)
		if self.bb: 
			print("BB")
		elif self.sb: 
			print("SB")
		elif self.btn: 
			print("BTN")
		
		if self.occupied: 
			self.player.printPlayer()
			
class Table:
	def __init__(self, players, blinds): 
		self.maxSize = 9
		self.currentSize = 0
		self.bb = blinds[1]
		self.sb = blinds[0]
		self.deck = Deck()
		self.deck.shuffle()
		
		self.seats = []
		
		for x in range(self.maxSize): 
			self.seats.append(Seat("seat"+str(x)))
		
		for x in range(len(players)): 
			if self.maxSize > self.currentSize: 
				self.addPlayer(players[x])
		

	def addPlayer(self, player):
		#will need more complicated checks in future to ensure players can't skip bb
		for x in range(self.maxSize): 
			if self.seats[x].occupied == False: 
				self.seats[x].player = player
				self.seats[x].occupied = True
				self.currentSize+=1
				return True
	
	#UNTESTED 
	def removePlayer(self, playerName): 
		for x in range(self.currentSize): 
			if self.seats[x].player.name == playerName: 
				#can probably delete player property rather than clearing it
				self.seats[x].player.name = ""
				self.seats[x].player.chips = 0
				self.seats[x].player.hand = (0,0)
				self.seats[x].occupied = false
	
	def printTable(self): 
		for x in range(self.currentSize):
			self.seats[x].printSeat()
			
		print("Blinds:", self.sb, "/", self.bb)
		print("Current size:", self.currentSize, "Max Size:", self.maxSize)


def setupGame(): 
	#create table and players
	humans = input("Please enter how many human players\n")
	cpus = input("Please enter how many computer players\n")
	
	chips = input("Please enter how many starting chips per player\n")
	
	players = []
	for x in range(int(humans)): 
		string = "Please enter player " + str(x+1) + "'s name\n"
		name = input(string)
		players.append(Player(chips, name, True))
		print("added human: ", name)
	
	for x in range(int(cpus)): 
		players.append(Player(chips, "cpu"+str(x), False))
		print("added cpu: ", "cpu"+str(x))
	
	table = Table(players, (int(chips)/100, int(chips)/50))
	#still need to set which seat is bb,sb, and btn
	return table

def playGame():
	table = setupGame() 
	for x in range(len(table.seats)):
		if table.seats[x].occupied: 
			table.seats[x].player.hand = table.deck.dealHand()
			#print humans' hands (but not CPUs')
			if table.seats[x].player.human: 
				table.seats[x].player.showHand()
	
	#wagering can start here
playGame()




