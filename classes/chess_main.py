from tableau import tableau
from chess_simple import chess_simple
from chess_linux import chess_linux
import sys

interface = chess_simple()
if len(sys.argv) == 2 and sys.argv[1] == "linux":
    interface = chess_linux()
if len(sys.argv) == 2 and sys.argv[1] == "simple":
    interface = chess_simple()

tab = tableau(interface)

tab.start()
