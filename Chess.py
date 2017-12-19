class Player(object):
	def __init__(self, player, play_id): #Player ID is 0 for white, 1 for black.
		#self.pieces_taken = [] #This is an array of strings.
		self.legal_moves = []  #This is an array of arrays. Each inner array has 2 elements, move from and move to.
		self.ai = not player
		self.ai
	def check_legal(cur_player)
		
	
	
class ChessBoard(object):
	def __init__(self):
		# White is capital letters
		self.conversion = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
		self.board = [ \
		['r','h','b','q','k','b','h','r'],\
		['p','p','p','p','p','p','p','p'],\
		['','','','','','','',''],\
		['','','','','','','',''],\
		['','','','','','','',''],\
		['','','','','','','',''],\
		['P','P','P','P','P','P','P','P'],\
		['R','H','B','Q','K','B','H','R']\
		]
	def rotate_board(self):
		self.board = self.board[::-1]
	def setup_board(self, white_top = False, p1Person = False, p2Person = False):
		# This makes adjusts white and black proper places. Does not reset board.
		if white_top:
			self.rotate_board()
			
	def move(self,moves, cur_player):
		#Remember that A1 corresponds to A being col and 1 being row.
		self.board[moves[1][1]][moves[1][0]] = self.board[moves[0][1]][moves[0][0]]
		self.board[moves[0][1]][moves[0][0]] = ''
	def print_board(self):
		print("  | A   B   C   D   E   F   G   H")
		print("_________________________________")
		for row in range(len(self.board)):
			print(8-row,"|", self.board[row][0]," ", self.board[row][1]," ", self.board[row][2]," ", self.board[row][3]," ", self.board[row][4]," ", self.board[row][5]," ", self.board[row][6]," ", self.board[row][7])
		print("                 ")
			
			
class Game():
	def __init__(self):
		self.current_player = None
		self.board = None
		self.board = ChessBoard()
		
	def process_move(self,move, cur_player):
		# A-H are the column, whereas the 1-8 
		moves = move.split(":")
		moves = [list(moves[0]), list(moves[1])]
		print(moves)
		#@TODO: Check whether the move is legal
		#@TODO: Check whether the right person is moving
		
		# We assume at this point all moves are legal.
		# Now, we make sure we can deal with these numbers by converting.
		moves[0][0] = int(self.board.conversion[moves[0][0]])
		moves[0][1] = 8 - int(moves[0][1])
		moves[1][0] = int(self.board.conversion[moves[1][0]])
		moves[1][1] = 8 - int(moves[1][1])
		print(moves)
		
		self.board.move(moves, cur_player)
		
	def start_game(self):
		p1Person = True if input("Is P1 a person? ")=="yes" else False
		p2Person = True if input("Is P2 a person? ")=="yes" else False
		cur_player = 0 #0 is white, 1 is black
		white_top = True
		if p1Person:
			white_top = True if input("Will you play as white? ")=="yes" else False
			cur_player = 1-int(white_top)
		players = [Player(p1Person,cur_player), Player(p2Person,1-cur_player)]
		
		self.board.setup_board(white_top = white_top, p1Person=p1Person, p2Person=p2Person)
		move = ""
		while move is not "quit":
			cur_player = cur_player%2
			# Print the board
			self.board.print_board()
			# We are playing\
			message = "White turn(capital case)" if cur_player==0 else "Black turn (lower case)"
			print(message, cur_player)
			move = input("What shall your move be (type format (move from):(move to). ex:A2:A4 ): ") #Typed like A1A2, means from A1 go to A2
			if move == "quit":
				break
			try:	
				self.process_move(move, cur_player)
			except Exception as e:
				print("Can not do that!")
			cur_player+=1

game = Game()
game.start_game()





