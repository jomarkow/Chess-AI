import connectivity
import board

broker = connectivity.Broker()

board.move("pD7-D5")
board.move("NG1-F3")
board.run_game()
