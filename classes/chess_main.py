from tableau import tableau
from chess_simple import chess_simple
from chess_linux import chess_linux
from chess_tkinter import chess_tkinter
import sys

if len(sys.argv) == 2 and sys.argv[1] == "linux":
    interface = chess_linux()
elif len(sys.argv) == 2 and sys.argv[1] == "simple":
    interface = chess_simple()
elif len(sys.argv) == 2 and sys.argv[1] == "tkinter":
    interface = chess_tkinter()
else:
    interface = chess_tkinter()
    
tab = tableau(interface)

tab.start()
