#Managing PlayerBase

import sqlite3
from time import sleep
import numpy as np
from time import sleep
from os import system

#for reference:
#ROCK     = 1
#PAPER    = 2
#SCISSORS = 3

#create and open database
dbase = sqlite3.connect("PlayerBase.db")

#create table called Players
dbase.execute(''' CREATE TABLE IF NOT EXISTS Players(
    ID INT PRIMARY KEY NOT NULL,
    NAME VARCHAR(20) NOT NULL,
    PASSWORD VARCHAR(20) NOT NULL
) ''')

#read names from Players
def check_usernames(user):
    found = False
    player_names = dbase.execute("SELECT NAME FROM Players")
    for each_name in player_names:
        if each_name[0] == user:
            found = True
            break
    return found

#read names and passwords from Players
def check_password(user,pw):
    found = False
    player_data = dbase.execute("SELECT NAME, PASSWORD FROM Players")
    for each_row in player_data:
        if each_row[0] == user:
            if each_row[1] == pw:
                found = True
                break
            break
    return found

#check number of existing players from Players
def check_id():
    last_id = 0
    player_ids = dbase.execute("SELECT ID FROM Players")
    for each_id in player_ids:
        last_id = int(each_id[0])
    return last_id        
        
#insert data into table 
def write_players(var1,var2,var3):
    dbase.execute('''INSERT INTO Players(ID,NAME,PASSWORD)
        VALUES(?,?,?)''',(var1,var2,var3))
    
    #apply these changes to our database
    dbase.commit()
    print("\nNew player recorded into database!")
    sleep(3)
    
#initialization of variables
game_mode_selection = ['1','2']
authorized = False

#Title Screen
retry = True
while(retry):
    print("\n" * 50)
    print("*** ROCK PAPER SCISSOR GAME ***")
    print("\n" * 10)
    game_mode = input("Select Game Mode (NEW GAME=1, LOAD GAME=2): ")
    if game_mode not in game_mode_selection:
        print("Please enter a valid input! (1 or 2)")
        sleep(2)
    else:
        retry = False

#NEW GAME
if game_mode == '1':
    #prompt player to input credentials
    retry = True
    while(retry):
        print("\n" * 50)
        print("*** NEW GAME ***")
        print("\n" * 10)
        user = input("Enter username (max 20 characters): ")
        #check if there is an existing player with that username
        found = check_usernames(user)
        if found:
            retry = True
            print("Ooops! Username already taken! Sorry! Think of another username!!")
            sleep(3)
        else:
            retry = False
    pw = input("Enter password (max 20 characters): ")
    print("\nWelcome to a new game " + user + " !")
    authorized = True
    
#LOAD GAME
if game_mode == '2':
    #prompt player to input credentials
    retry = True
    while(retry):
        print("\n" * 50)
        print("*** CONTINUING PREVIOUS GAME ***")
        print("\n" * 10)
        user = input("Enter username: ")
        #check if there is an existing player with that username
        found = check_usernames(user)
        if found:
            retry = False
        else:
            retry = True
            print("Ooops! Username not found! Sorry! Try to remember your username!!")
            sleep(3)
    correct_password = False
    password_threshold = 3
    while(not correct_password):
        print("\nAttempts left: " + str(password_threshold))
        pw = input("Enter password: ")
        #check if password entered is correct
        correct_password = check_password(user,pw)
        if not correct_password:
            print("Wrong password! Please reenter!")
            password_threshold -= 1
            if password_threshold <= 0:
                print("\nMaximum attempts reached! Shutting down!")
                sleep(3)
                break
            sleep(3)
        else:
            print("Authorized User! Welcome back " + user + " !")
            authorized = True
            sleep(3)

if authorized:
    #GAME STARTS HERE
    #for reference:
    #ROCK     = 1
    #PAPER    = 2
    #SCISSORS = 3
    
    #clear the screen initially and printing from the bottom part of the console
    print("\n" * 50)
    
    #setup the game's initial points and starting round
    print("***ROCK PAPER SCISSOR GAME WILL BEGIN ***")
    print("\nWelcome " + user + " ! Game is loading...")
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
            print("\nYOU WON!!! CONGRATULATIONS " + user + " !!")
            print("\nYour score: " + str(player_points))
            print("AI score: " + str(AI_points))
            player_victory+=1
            sleep(5)
        elif player_points < AI_points:
            print("\nYOU LOST!!! GIT GUD " + user + " !!")
            print("\nYour score: " + str(player_points))
            print("AI score: " + str(AI_points))
            AI_victory+=1
            sleep(5)
        else:
            print("\nIT'S A DRAW!!! THAT WAS CLOSE " + user + " !!")
            print("\nYour score: " + str(player_points))
            print("AI score: " + str(AI_points))
            sleep(5)
        
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
    #GAME ENDS HERE

    if game_mode == '1':        
        #check how many existing players
        last_id = check_id() + 1
        #insert new players into database
        write_players(last_id,user,pw)


#close database
dbase.close()