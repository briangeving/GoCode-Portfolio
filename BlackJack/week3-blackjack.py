'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Tips:
1) Aces can count as an eleven or a one - but it only counts as a one if your score is over 21
2) Research random.shuffle()
3) You are not allowed to code until you design your program!
4) Optional: Research __radd__ - it is a built-in method in Python

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''
import random
card_suits = ["Clubs","Spades","Hearts","Diamonds"]
card_faces = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"] 
class Card(object):
	def __init__(self, suit, card_face, value):
		self.suit = suit
		self.card_face = card_face
		self.value = value
class Deck(object):
	def __init__(self):
		self.card_pile = []
		for suit in card_suits:
			for face in  card_faces:
				if face == "Jack" or face == "Queen" or face == "King":
					self.card_pile.append(Card(suit,face,10))
				elif face == "Ace":
					self.card_pile.append(Card(suit,face,11))
				else:
					self.card_pile.append(Card(suit,face,face))
		random.shuffle(self.card_pile)
class Person(object):
	def __init__(self):
		self.name = 'Player'
		self.hand = []		
		self.points = 0
	def hit(self,card):
		self.hand.append(card)
	def recalculate_score(self):
		self.points = 0
		for item in self.hand:
			self.points += item.value
	def gimme_total(self):
		self.total = 0
		for card in self.hand:
			self.total += card.value
		return self.total
class Game(object):
	def __init__(self):
		self.players = [Person()]
		self.deck = Deck()
		self.deal()
	def deal(self):	
		self.players[0].points = 0
		self.players[0].hand = []
		for _ in range (0,2):
			self.players[0].hit(self.deck.card_pile.pop())
		print " "
		print str(self.players[0].hand[0].card_face) + " of " + self.players[0].hand[0].suit
		print str(self.players[0].hand[1].card_face) + " of " + self.players[0].hand[1].suit
		self.players[0].recalculate_score()
		print " "
		print "Your score is: " + str(self.players[0].points)
		print " "
	def play(self):
		self.players[0].points = 0
		player_score = 0
		dealer_score = 0
		while True:
			if self.players[0].points <= 21:
				choice = raw_input("(H)it or (S)tand? ")
				if choice.upper() == 'H':
					self.players[0].hit(self.deck.card_pile.pop())
					self.players[0].recalculate_score()
					print " "
					for card in self.players[0].hand:
						print str(card.card_face) + " of " + card.suit
					self.players[0].recalculate_score()
					player_score = self.players[0].points
					print " "
					print "Your score is: " + str(self.players[0].points)
					self.players[0].recalculate_score()
					
				else:
					self.players[0].recalculate_score()
					player_score = self.players[0].points
					self.players[0].recalculate_score()
					self.players[0].points = 0
					self.players[0].hand = []
					print player_score
					self.dealer_play()
					return

			else:
				print " "
				print "You busted!"
				print "Dealer wins!"
				print " "
				play_again = raw_input("Play again? ")
				if play_again.upper() == 'Y':
					self.players[0].points = 0
					self.players[0].hand = []
					game = Game()
					game.play()
					break
				else:
					return
		while True:
			if self.players[0].points <= 21:
				if self.players[0].points <= 16:
					self.players[0].hit(self.deck.card_pile.pop())
					self.players[0].recalculate_score()
					dealer_score = self.players[0].points
				else:
					self.players[0].recalculate_score()
					for card in self.players[0].hand:
						print str(card.card_face) + " of " + card.suit
						self.players[0].recalculate_score()
					self.players[0].recalculate_score()
					dealer_score = self.players[0].points
					if self.play.player_score > dealer_score:
						print " "
						print "Player score is " + str(player_score)
						print "Dealer score is " + str(dealer_score)
						print " "
						print "Congratulations!"
						print "You win!"
						print " "
						play_again = raw_input("Play again? ")
						if play_again.upper() == 'Y':
							g = Game()
							g.play()
						else:
							break
					elif self.play.player_score < dealer_score:
						print " "
						print "Player score is " + str(player_score)
						print "Dealer score is " + str(dealer_score)
						print " "
						print "So sad..."
						print "You lose. :("
						print " "
						play_again = raw_input("Play again? ")
						if play_again.upper() == 'Y':
							g = Game()
							g.play()
						else:
							return
					break
			else:
				for card in self.players[0].hand:
						print str(card.card_face) + " of " + card.suit
				self.players[0].recalculate_score()
				dealer_score = self.players[0].points
				print " "
				print "Dealer busted!"
				print "You win!"
				print " "
				print "Player score is " + str(player_score)
				print "Dealer score is " + str(dealer_score)
				play_again = raw_input("Play again? ")
				if play_again.upper() == 'Y':
					g = Game()
					g.play()
				else:
					break

g = Game()
g.play()
