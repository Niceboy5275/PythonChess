from tableau import tableau
from chess_simple import chess_simple
from chess_linux import chess_linux
from chess_tkinter import chess_tkinter
import sys

inter_input = ""
if len(sys.argv) == 1: #pragma: no cover
    print ("Choose the interface you want to use")
    print (" - simple : text-based interface")
    print (" - linux : text based with colors")
    print (" - windows : windows interface with mouse management")
    inter_input = input ("interface ? (simple, linux, windows) : ")

if len(sys.argv) == 2 and sys.argv[1] == "linux" or inter_input == "linux":
    interface = chess_linux()
elif len(sys.argv) == 2 and sys.argv[1] == "simple" or inter_input == "simple":
    interface = chess_simple()
elif len(sys.argv) == 2 and sys.argv[1] == "tkinter" or inter_input == "windows": #pragma: no cover
    interface = chess_tkinter()
else: #pragma: no cover
    print ("interface not found")
    
tab = tableau(interface)

tab.start()
