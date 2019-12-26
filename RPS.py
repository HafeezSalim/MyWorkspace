# Rock Paper Scissors Minigame

import numpy as np
from time import sleep
from os import system

#for reference:
#ROCK     = 1
#PAPER    = 2
#SCISSORS = 3

#clear the screen initially and printing from the bottom part of the console
print("\n" * 50)

#setup the game's initial points and starting round
print("***ROCK PAPER SCISSOR GAME***")
username = input("\nEnter your username: ")
print("\nWelcome " + username + " ! Game is loading...")
sleep(5)

games = 0
player_victory = 0
AI_victory = 0
selections = ['1','2','3']  #provide possible player inputs
rematch = 'Y'
rematch_selections = ['Y','N']

while(rematch=='Y'):
    #reset points per match
    Round=1
    player_points = 0
    AI_points = 0
    #loop between 5 rounds
    while(Round<6):
        print("\n" * 50)
        print("Round " + str(Round) + "!")
        
        #seek input from player
        player = input("\nEnter your choice (rock=1, paper=2, scissors=3): ")
        while(player not in selections):
            print("Please enter a valid input!")
            sleep(3)
            print("\n" * 50)
            print("Round " + str(Round) + "!")
            player = input("\nEnter your choice (rock=1, paper=2, scissors=3): ")
    
        #convert player input string to int
        player = int(player)
        
        #AI generates input
        AI = np.random.randint(1,4)
        #list out all possibilities and outcomes
        if player == 1 and AI == 1:
            print("\nYou chose ROCK, AI chose ROCK!\nDRAW!")
            
        if player == 1 and AI == 2:
            print("\nYou chose ROCK, AI chose PAPER!\nLOSE!")
            AI_points+=1
            
        if player == 1 and AI == 3:
            print("\nYou chose ROCK, AI chose SCISSORS!\nWIN!")
            player_points+=1
            
        if player == 2 and AI == 1:
            print("\nYou chose PAPER, AI chose ROCK!\nWIN!")
            player_points+=1
            
        if player == 2 and AI == 2:
            print("\nYou chose PAPER, AI chose PAPER!\nDRAW!")
            
        if player == 2 and AI == 3:
            print("\nYou chose PAPER, AI chose SCISSORS!\nLOSE!")
            AI_points+=1
            
        if player == 3 and AI == 1:
            print("\nYou chose SCISSORS, AI chose ROCK!\nLOSE!")
            AI_points+=1
        
        if player == 3 and AI == 2:
            print("\nYou chose SCISSORS, AI chose PAPER!\nWIN!")
            player_points+=1
            
        if player == 3 and AI == 3:
            print("\nYou chose SCISSORS, AI chose SCISSORS!\nDRAW!")
        
        sleep(3)
        Round+=1
    
    #tally the overall points and announce the winner after the 5th round
    print("\nOverall results...")
    sleep(3)
    if player_points > AI_points:
        print("\nYOU WON!!! CONGRATULATIONS " + username + " !!")
        print("\nYour score: " + str(player_points))
        print("AI score: " + str(AI_points))
        player_victory+=1
        sleep(8)
    elif player_points < AI_points:
        print("\nYOU LOST!!! GIT GUD " + username + " !!")
        print("\nYour score: " + str(player_points))
        print("AI score: " + str(AI_points))
        AI_victory+=1
        sleep(8)
    else:
        print("\nIT'S A DRAW!!! THAT WAS CLOSE " + username + " !!")
        print("\nYour score: " + str(player_points))
        print("AI score: " + str(AI_points))
        sleep(8)
    
    #list down how many times player and AI won
    games+=1
    print("\nYou won " + str(player_victory) + " times out of " + str(games) + " games so far!")
    print("AI won " + str(AI_victory) + " times out of " + str(games) + " games so far!")
    
    #ask whether player wants a rematch?
    rematch = input("\nDo you want a rematch (Y/N)?: ")
    while (rematch not in rematch_selections):
        print("Please enter a valid input!")
        sleep(3)
        rematch = input("\nDo you want a rematch (Y/N)?: ")

#thanks the gamer and clearing the game
print("\n" * 50)
print("THANK YOU FOR PLAYING :))")
sleep(5)
system('cls')


