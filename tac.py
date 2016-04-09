#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import curses
# import system locale
import locale
import tictactoe
locale.setlocale(locale.LC_ALL, '')
# set the variable coding to the system's encoding, so we can use it for str.encode()-calls.
coding=locale.getpreferredencoding()

# this function is the main curses function
def ticTac(stdscr):

    # initiate the game object
    # we can send other grid sizes & win conditions to the object here.
    game = tictactoe.ticTacToe(stdscr,int(boardHeight),int(boardWidth),int(winLen),overWriteBool)

    # and start a loop that keeps the game running
    while game.winner == "":

        # read a keypress, and interpret it
        keyPress=game.getkey()
        game.readKey(keyPress)


# initialize a curses session using curses.wrapper
# wrapper takes a function as argument - our ticTacToe function, which is the main program.


boardHeight = int(raw_input('How high should the board be? (3) ') or 3 )
boardWidth = int(raw_input('How wide should the board be? ('+str(boardHeight)+') ') or boardHeight)
lowest= sorted((boardHeight,boardWidth))[0]
winLen = int(raw_input('How many in a row to win? (' + str(lowest) + ') ') or lowest)
if winLen > boardHeight and winLen > boardWidth:
    print "That's too long for the game board!"
    winLen = sorted((boardHeight,boardWidth))[1]
    print "I adjusted it to " + str(winLen)
overWriteStr = raw_input('Should markers be overwriteable? [y/n] ')
if overWriteStr == 'n':
    overWriteBool = False
else:
    overWriteBool = True
curses.wrapper(ticTac)
