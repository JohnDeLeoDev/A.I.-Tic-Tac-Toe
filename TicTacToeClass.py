# John DeLeo
# CS534
# Individual Project Assignment 3
# Tic Tac Toe Game App
############################################################################################################
# This is the TicTacToe class that is used in the TicTacToeGameApp.py file. It contains the Board, Player, and Node classes. 
# The Board class is used to create the game board and check for a winner or a draw. 
# The Player class is used to create the players and their moves. 
# The Node class is used for the MCTS player to create the nodes for the tree search.
############################################################################################################
import random
import time

# The TicTacToe class is used to create the game and play the game.
class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.round = 1
        self.round_log = []
        self.draws_in_a_row = 0
        self.draws_cap = 3

    def display_board(self):
        self.board.display_board()

    def set_players(self, player1, player2):
        self.player1 = Player(player1, 'X', 1)
        self.player2 = Player(player2, 'O', 2)
        self.current_player = self.player1

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    # Check to see if 3 draws have occurred in a row. If so, the game is a draw.
    def check_draws(self):
        if self.draws_in_a_row == self.draws_cap:
            print("Three draws in a row! Game is a draw.")
            print()
            print("Recap:")
            for i in range(len(self.round_log)):
                if self.round_log[i] == 0:
                    print("Round ", i + 1, ": Draw")
                else:
                    print("Round ", i + 1, ": Player ", self.round_log[i], " wins")
            return True
        return False

    # Check to see if a player has won 2 rounds. If so, the game is over.
    def check_rounds_winner(self):
        if self.player1.wins == 2:
            print(f"Player 1 ({self.player1.player_shape}), {self.player1.type_str}, wins the game! {self.player1.wins} to {self.player2.wins} wins in {self.round - 1} rounds.")
            print()
            print("Recap:")
            for i in range(len(self.round_log)):
                if self.round_log[i] == 0:
                    print("Round ", i + 1, ": Draw")
                else:
                    print("Round ", i + 1, ": Player ", self.round_log[i], " wins")
            return True
        elif self.player2.wins == 2:
            print(f"Player 2 ({self.player2.player_shape}), {self.player2.type_str}, wins the game! {self.player2.wins} to {self.player1.wins} wins in {self.round - 1} rounds.")
            print()
            print("Recap:")
            for i in range(len(self.round_log)):
                if self.round_log[i] == 0:
                    print("Round ", i + 1, ": Draw")
                else:
                    print("Round ", i + 1, ": Player ", self.round_log[i], " wins")
            return True
        return False

    # Play the game until a player has won 2 rounds or 3 draws have occurred in a row.
    def play_game(self):
        while self.player1.wins < 2 and self.player2.wins < 2:
            print(f"Round {self.round}")
            print()
            print("Player 1 currently has ", self.player1.wins, " wins.")
            print("Player 2 currently has ", self.player2.wins, " wins.")
            print("First player to 2 wins wins the game.")
            print()
            if self.round > 1:
                if self.player1.type[1] == "query_player" or self.player2.type[1] == "query_player":
                    print("Ready for the next round?")
                    print()
                    input("Press Enter to continue...")
                    print()
            self.play_round()
            if self.check_draws():
                break

        print()
        print("Game Over!")
        print()

    # Play a round of the game.
    def play_round(self):
        while not self.board.game_over():
            self.display_board()
            self.current_player.make_move(self.board)
            print(f"{self.current_player.player_shape} moves to {self.current_player.actions[-1]}")
            self.switch_players()
        self.display_board()
        if self.board.check_winner():
            self.switch_players()
            print(f"Player {self.current_player.number} ({self.current_player.player_shape}), {self.current_player.type_str}, wins the round!")
            print()
            self.current_player.wins += 1
            self.draws_in_a_row = 0
            self.round_log.append(self.current_player.number)
        else:
            print("It's a draw!")
            print()
            self.round_log.append(0)
            self.draws_in_a_row += 1
        self.round += 1

        if not self.check_rounds_winner():
            self.board = Board()
            self.current_player = self.player1
############################################################################################################
# The Player class is used to create the players and their moves.
class Player:
    def __init__(self, player_type, player_shape=None, player_number=None):
        self.player_types = [
            [1, "random_player"],
            [2, "minimax_player"],
            [3, "alpha_beta_player"],
            [4, "heuristic_alpha_beta_player"],
            [5, "mcts_player"],
            [6, "query_player"]
        ]
        self.player_shape = player_shape
        self.opponent_shape = 'O' if player_shape == 'X' else 'X'
        self.actions = []
        self.number = player_number
        self.type = self.player_types[player_type - 1]
        self.wins = 0
        if self.type[1] == "mcts_player":
            self.type_str = "MCTS Player"
        elif self.type[1] == "query_player":
            self.type_str = "Query Player"
        elif self.type[1] == "random_player":
            self.type_str = "Random Player"
        elif self.type[1] == "minimax_player":
            self.type_str = "MiniMax Player"
        elif self.type[1] == "alpha_beta_player":
            self.type_str = "Alpha Beta Player"
        elif self.type[1] == "heuristic_alpha_beta_player":
            self.type_str = "Heuristic Alpha Beta Player"

    # Record the player's move to the log
    def record_action(self, action):
        self.actions.append(action)

    # Make a move based on the player's type
    def make_move(self, board):
        if self.type[1] == "random_player":
            self.random_move(board)
        elif self.type[1] == "minimax_player":
            self.minimax_move(board)
        elif self.type[1] == "alpha_beta_player":
            self.alpha_beta_move(board)
        elif self.type[1] == "heuristic_alpha_beta_player":
            self.heuristic_alpha_beta_move(board)
        elif self.type[1] == "mcts_player":
            self.mcts_move(board)
        elif self.type[1] == "query_player":
            self.query_move(board)

    # Random move
    def random_move(self, board):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board.board[row][col] == ' ':
                board.board[row][col] = self.player_shape
                self.record_action((col + 1, row + 1))
                break

    # MiniMax move
    def minimax_move(self, board):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    valid_moves.append((i, j))
        best_move = None
        best_score = float('-inf')
        for move in valid_moves:
            board.board[move[0]][move[1]] = self.player_shape
            score = self.minimax(board, False)
            board.board[move[0]][move[1]] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        board.board[best_move[0]][best_move[1]] = self.player_shape
        self.record_action([best_move[1] + 1, best_move[0] + 1])

    # MiniMax algorithm
    def minimax(self, board, is_maximizing):
        if board.check_winner() == self.player_shape:
            return 1
        elif board.check_winner() == self.opponent_shape:
            return -1
        elif board.check_draw():
            return 0
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.player_shape
                        score = self.minimax(board, False)
                        board.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.opponent_shape
                        score = self.minimax(board, True)
                        board.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    # Alpha Beta move
    def alpha_beta_move(self, board):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    valid_moves.append((i, j))
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in valid_moves:
            board.board[move[0]][move[1]] = self.player_shape
            score = self.alpha_beta(board, False, alpha, beta)
            board.board[move[0]][move[1]] = ' '
            if score > alpha:
                alpha = score
                best_move = move
        board.board[best_move[0]][best_move[1]] = self.player_shape
        self.record_action([best_move[1] + 1, best_move[0] + 1])

    # Alpha Beta algorithm
    def alpha_beta(self, board, is_maximizing, alpha, beta):
        if board.check_winner() == self.player_shape:
            return 1
        elif board.check_winner() == self.opponent_shape:
            return -1
        elif board.check_draw():
            return 0
        if is_maximizing:
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.player_shape
                        alpha = max(alpha, self.alpha_beta(board, False, alpha, beta))
                        board.board[i][j] = ' '
                        if alpha >= beta:
                            return beta
            return alpha
        else:
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.opponent_shape
                        beta = min(beta, self.alpha_beta(board, True, alpha, beta))
                        board.board[i][j] = ' '
                        if alpha >= beta:
                            return alpha
            return beta       

    # Heuristic Alpha Beta move
    def heuristic_alpha_beta_move(self, board):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    valid_moves.append((i, j))
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in valid_moves:
            board.board[move[0]][move[1]] = self.player_shape
            score = self.heuristic_alpha_beta(board, False, alpha, beta)
            board.board[move[0]][move[1]] = ' '
            if score > alpha:
                alpha = score
                best_move = move
        board.board[best_move[0]][best_move[1]] = self.player_shape
        self.record_action([best_move[1] + 1, best_move[0] + 1])

    # Heuristic Alpha Beta algorithm
    def heuristic_alpha_beta(self, board, is_maximizing, alpha, beta):
        if board.check_winner() == self.player_shape:
            return 1
        elif board.check_winner() == self.opponent_shape:
            return -1
        elif board.check_draw():
            return 0
        if is_maximizing:
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.player_shape
                        alpha = max(alpha, self.heuristic_alpha_beta(board, False, alpha, beta))
                        board.board[i][j] = ' '
                        if alpha >= beta:
                            return beta
            return alpha
        else:
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = self.opponent_shape
                        beta = min(beta, self.heuristic_alpha_beta(board, True, alpha, beta))
                        board.board[i][j] = ' '
                        if alpha >= beta:
                            return alpha
            return beta   

    # MCTS move
    def mcts_move(self, board):
        root = Node(board, None)
        for _ in range(1000):
            node = root
            temp_board = Board()
            temp_board.board = [row[:] for row in board.board]
            while node.untried_actions == [] and node.children != []:
                node = node.select_child()
                temp_board.board[node.action[1]][node.action[0]] = node.player_shape
            if node.untried_actions != []:
                action = random.choice(node.untried_actions)
                temp_board.board[action[1]][action[0]] = node.player_shape
                node.untried_actions.remove(action)
                new_node = Node(temp_board, node, action)
                node.children.append(new_node)
                node = new_node
            while not temp_board.game_over():
                action = random.choice(temp_board.available_moves())
                temp_board.board[action[1]][action[0]] = node.player_shape
            result = temp_board.check_winner()
            while node != None:
                node.update(result)
                node = node.parent
        best_child = root.best_child()
        board.board[best_child.action[1]][best_child.action[0]] = self.player_shape
        self.record_action([best_child.action[0] + 1, best_child.action[1] + 1])

    # Query move
    def query_move(self, board):
        while True:
            print("Enter your move in the format col, row")
            print("Colums and rows are indexed from 1 to 3")
             
            col = int(input("Enter col: "))
            while col not in [1, 2, 3]:
                col = int(input("Enter col: "))

            row = int(input("Enter row: "))
            while row not in [1, 2, 3]:
                row = int(input("Enter row: "))   

            if board.board[row-1][col-1] == ' ':
                board.board[row-1][col-1] = self.player_shape
                self.record_action((col, row))
                break
            else:
                print("That spot is already taken, please try again")

############################################################################################################
# The Board class is used to create the game board and check for a winner or a draw.
class Board:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def display_board(self):
        horizontal_lines = self.rows - 1
        vertical_lines = self.cols - 1
        print()
        for i in range(self.rows):
            print(" " + " | ".join(self.board[i]) + " ")
            if i < horizontal_lines:
                print("---|---|---")
        print()
        print("Available Moves:")
        for spot in self.available_moves():
            print(f"                ({spot[0] + 1}, {spot[1] + 1})")
        print()

    def game_over(self):
        if self.check_winner() or self.check_draw():
            return True
        return False

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((j, i))
        return moves

############################################################################################################
# The Node class is used for the MCTS player to create the nodes for the tree search.
class Node:
    def __init__(self, board, parent, action=None):
        self.board = board
        self.parent = parent
        self.action = action
        self.player_shape = 'X' if parent == None or parent.player_shape == 'O' else 'O'
        self.untried_actions = self.board.available_moves()
        self.children = []
        self.wins = 0
        self.visits = 0

    def select_child(self):
        best_score = float('-inf')
        best_child = None
        for child in self.children:
            score = child.wins / child.visits + 1.41 * (2 * (self.visits / child.visits) ** 0.5)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def best_child(self):
        best_score = float('-inf')
        best_child = None
        for child in self.children:
            score = child.visits
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def update(self, result):
        self.visits += 1
        if result == self.player_shape:
            self.wins += 1
        elif result == None:
            self.wins += 0.5

