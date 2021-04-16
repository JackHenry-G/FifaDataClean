# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:04:34 2020

@author: Jack Goggin
"""
#final_version
import pandas as pd
# imports the pandas library
# assigns it to the word 'pd', as this is shorter it saves time because we don't have to write 'pandas' each time
# we use this module, instead just write 'pd'
import matplotlib.pyplot as plt
# imports the matplotlib.pyplot library and assigns to plt
# used this module for display graphs about data
import math
# imported math library to use pi
import time
# imported time library to use delays in the application

def menu():
    print("\n\n ---------------- THIS IS THE FIFA 19 VANGUARD HUB ---------------- \n\n")
    print("0. Exit application! ")
    print("1. Search the database for player names. Instructions:\n -  Search a player's name\n -  receive all players matching this name\n -  (Is important to know exact name for later features)")
    print("2. Get ALL the data relating to your chosen player.")
    print("3. Get the in-game statistics of a chosen player. E.g sprint speed, strength, sliding tackle, etc.")
    print("4. Get the information of a chosen player. E.g. Full name, shirt number, nationality, etc.")
    print("5. Get all the career mode information of a chosen player. E.g. Release clause value, potential rating, contract end date, etc.")
    print("6. Choose a player, choose a category of in-game statistics and see these statistics displayed in a radar chart.")
    print("7. Answer the question - Which player has the most in-game statistics in total? Who is the most all round player?")
    print("8. Display the top 100 players by overall rating in a list and displays top 20 in a bar chart")
    print("9. Get data anlysis insights into wages and if they correlated to player rating and age.")
    print("10. Some short, simple data anlysis.")
    loop = True
    while loop is True:
        # this will loop asking the user for a number, which decides what section the user goes to, until the user enters a valid entry
        # essentially if the user inputs a number, an error will not be returned, so it will not loop
        # if anything other than an integer is entered, like a string, an error will be returned and the 'except' code will run
        # once user inputs a valid entry and can go to the next step in the program, the 'loop' variable is set to False to break the loop
        try:
            # tries this code until the user enters a valid entry
            choice = (int(input("Enter a number for what you want to do: ")))
            # specifies an integer must be inputted
            
            while choice not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                # will loop asking for a number if the user enters a number not in this array
                print("\n !!!! It must be a number from 0 - 10 !!!!")
                choice = (int(input("Enter your decision: ")))
                # coverts entry to integer
            
            if choice == 1:
                # simple if-elif statements, that will execute a certain function call depending on what number is entered
                loop = False
                # loop is set to False, so that the original while loop will not iterate again
                # without this, after the function that has been called is completed, this would be looped through again as the value would still be true
                search_database()
            elif choice == 2:
                loop = False
                get_all_player_data()
            elif choice == 3:
                loop = False
                get_ingame_stats()
            elif choice == 4:
                loop = False
                get_player_info()
            elif choice == 5:
                loop = False
                get_career_mode_info()
            elif choice == 6:
                loop = False
                radar_chart_stats()
            elif choice == 7:
                loop = False
                most_total_stats()
            elif choice == 8:
                loop = False
                top_players()
            elif choice == 9:
                loop = False
                wage_insight()
            elif choice == 10:
                loop = False
                data_analysis()
            elif choice == 0:
                loop = False
                print("\nExiting...")
                time.sleep(2) # delays 2 seconds
                print("\nThanks for using the FIFA 19 Vanguard! ")
              
            # the choice entry decides which function is called
            # if the user inputs 1, the function will be called to search the database and that code will be executed
        
        except:
            # if input for choice returns an error this will be called
            # then the while loop will loop again
            print("\n !!!! You must input a number from the list !!!! ")

    
def intro():
    # defines the function for the introduction of the user
    # decompostion - breaks down big problems into smaller problems. Smaller problems easier to solve, re-construct to solve big problem
    # good to use decomposition, as makes code more readable, easier to troubleshoot and the function can be re-used elsewhere
    
    print("\n\nHello and welcome to the FIFA 19 vanguard - a database of players in FIFA 19")
    print("Search for your favourite players and see their statisitcs on the 2019 edition of the game")
    print("But that's not all! With this technology you can compare players stats - shooting, defending, potential in career mode, height; compare it all!")
    print("Search for that perfect player to make your team click? Search via specific parameters to find that player! ")
    print("E.g. Over 6ft, more than 80 pace, more than 84 defending, high defensive work rate. Find the players that match your needs! ")
    print("\n\nThere are 92 different types of statistic stored on each player: \n\n")
    # display an introduction message to the user - explains what the application can do
    
    df = pd.read_csv('fifa_cleaned.csv')
    # 'df' is short for data frame. A dataframe, part of the pandas library, is a "2D tabular data structure"
    # "data is aligned in a tabular fashion in rows and columns"..."three principal components, the data, rows and columns"
    # https://www.geeksforgeeks.org/python-pandas-dataframe/
    # this line read the comma-seperated value (csv) file into a data frame, via the file name 'fifa_claned.csv'
    # this is saved in the same location as the file, otherwise we would have to specify the filepath
    # by using a dataframe, the information is more readable and easier to parse
    
    column_headers = df.columns.tolist()
    # df.columns gets the header of each column, this is stored as a 'numpy.ndarray'
    # .tolist() converts the columns from type 'numpy.ndarray' to a list type, making it easier to read and parse
        
    for counter, value in enumerate(column_headers, start = 1):
        print(counter, ' - ', value)
    # enumrate function adds a counter to the variable. So this would add a counter to each header in the table
    # the for loop iterates through the list generated by the enumerate function
    # the enumerate function splits the list into two values - a number (counter), and the header name
    # the for loop assings the variable name counter to the number and the value variable to the header name
    # then for each line as it loops, it prints the counter variable, followed by a string ' - ', then the value variable
    # which displays the "counter ' - ' header name" or "1 - id"
    
    menu()
    

def search_database():
    # this will be a fucntion that allows users to search for players in a database
    # this is needed as a player may search for Wilson, as in Callum Wilson, but there are multiple players with the last name Wilson
    # this will return each player with 'Wilson' in there name, allowing them to specify the correct player
    
    df = pd.read_csv('fifa_cleaned.csv')
    player_data = df['name']
    # converts data frame into a pandas series that includes just the column with header 'name'
    # where a series is a one dimensional object, as opposed to the two dimensional data frame
    print("\n\nHere you can search for stats belonging to a certain player")
    print("\nFirst we must make sure you are searching for the correct player")
    # explains what is needed before we search for the stats
    
    desired_player = (str(input("Input the player you want to search for: "))).capitalize()
    # gets a string input from the user to determine the player they want to search for
    # capitalize() is a function that capitalises the first letter, as each name in the dadtabase has a capital first letter, so this is needed to match properly
    list_of_players_found = []
    # defines a list of the players that will be found on the upcoming search on the users input
    for index, player_name in player_data.items():
    # iterates through the series, assigning the index the variable index and the data in the column 'name' to the variable 'player_name'
        if desired_player in player_name:
            # if statement, if the string that the user entered is contained in one of the values in the 'name' column
            # rather than use the "player_name = value", this function will check if the string is contained within
            # meaning players with similiar names, but no exact to the user input, can be found
            list_of_players_found.append(player_name)
            # if a name is found, it is added onto the list defined above
            # append adds to end, rather than overwriting

    if len(list_of_players_found) != 0:
        # if statement checks that list is not empty
        # a list of length 0 would mean it is empty, as there are no entries. A empty list would mean no players found
        print("\nPlayers found: \n")
        print('\n'.join(list_of_players_found))
        # this join() function, displays the list without the brackets, but seperates them but '\n' which leaves a line
        # makes it more readable and user friendly
        print("\nNow copy the desired players name and use this exact copy when using other features.")
    else:
        print("\nThis name was not found in the database. ")
        # prints no players found as the list length was zero
        
        
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input
        
def get_all_player_data():
    while True:
        try:
            desired_player = (str(input("Enter a player's name to see ALL their data: ")))
            if desired_player.upper() == "EXIT":
                break
            pd.set_option('display.max_rows', None)
            # this option is a function in pandas that says that there is no limit to how much data is displayed
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            # this saves just the column 'name' to the 'player_stats' variable. This means just the player names
            player_stats = player_stats_column.loc[desired_player]
            # .loc method accesses a group of rows and columns by a label. Previously defined just the 'name' column. This allows us to search by 'name'
            # so we pass a parameter, say 'L. Messi' this searches the previous data frame that stores just the player names column
            # .loc will then access all data belonging to 'L.Messi' name. We then print this data. Assigns this to the 'player_stats' column
            print("\n")
            # print empty line to make displayed data more readable
            for index, value in player_stats.items():
                # iterates through the panda series 'player_stats'. Assigns the index column to the variable index and the corresponding statistic to the variable value
                print(f"{index} - {value}")
                # f string format
                # curly brackets represent what will be replaced. In this case index and value variables are placed in the string within the curly brackets
                # this function iterates through each index and corresponding value, prints the value followed by the dash followed by the statistic
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")  
        
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input

def get_ingame_stats():
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'freekick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'composure', 'marking', 'standing_tackle', 'GK_diving', 'GK_handling', 'GK_kicking', 'GK_positioning', 'GK_reflexes']] 
            print("\nHere are the statistics for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.") 
             
    # while True will loop, repeatedly asking the user for a desired player, until the user either exits or enters a valid player
    # if the player is not valid, the 'desired_player' will throw an error, jumping to the except section, and looping through again
    # if the player is valid, the code continues, if the player entered is 'EXIT' then the loop will break and the application ends
    # otherwise, the code continues, passing in the csv file, getting a the data related to the specific player
    # defining the columns that we will be looking for, it tehn loops through these columns
    # it will loop through the array of columns in the CSV, getting the index and then stat belonging to this column
    # Then for each line, using a f-string that passes in the index, which is the player name, and the value, prints the stats
    # this code is then repeated for the following functions, but with different in  column values
            
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input
    
def get_player_info():
    # this function works in the same way as previous but changes the column names
    # this means it gets different infromation for the different application path choice
    # however, it functions in exact same way as 'get_ingame_stats()'
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['birth_date', 'age', 'height_cm', 'weight_kgs', 'positions', 'nationality', 'overall_rating', 'potential', 'preferred_foot', 'international_reputation(1-5)', 'weak_foot(1-5)', 'skill_moves(1-5)', 'work_rate', 'body_type', 'tags', 'traits']] 
            print("\nHere is the player information for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")    
            
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input

def get_career_mode_info():
    # this function works in the same way as previous but changes the column names
    # this means it gets different infromation for the different application path choice
    # however, it functions in exact same way as 'get_ingame_stats()'
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['full_name', 'positions', 'nationality', 'overall_rating', 'potential', 'value_euro', 'wage_euro', 'release_clause_euro', 'club_team', 'club_rating', 'club_position', 'club_jersey_number', 'club_join_date', 'contract_end_year', 'national_team', 'national_rating', 'national_team_position', 'national_jersey_number', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB' ]] 
            print("\nHere is the career mode information for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.") 
            
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input
            

def radar_chart_stats():
    exit_choice=False
    # referenced later in this function to decide whether the user wants to exit
    # will be set to True to exit this function
    while True:
        # another try/except statement within a while loop that willl loop until it gets a valid player name
        try:
            desired_player = (str(input("\nInput the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break
            # if user wants to exit, they input the word 'exit'
            # and based on this if-statement, if the string input (when changed to all upper case) is equal to 'EXIT'
            # the if statement will run, which is just to break the original while loop, and therefore exit this part of the program
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            pace = player_stats[['acceleration', 'sprint_speed']]
            shooting = player_stats[['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']]
            passing = player_stats[['vision', 'crossing', 'freekick_accuracy', 'short_passing', 'long_passing', 'curve']]
            dribbling = player_stats[['agility', 'balance', 'reactions', 'ball_control', 'dribbling', 'composure']]
            defending = player_stats[['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']]
            physicality = player_stats[['jumping', 'stamina', 'strength', 'aggression']]
            # defining every stat by the statistics that make them up, by column header
            break
        except:
            print("\nThat was not a valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")

    def pace_stats(*args):
        # *args states that the function will receive an undefined amount of arguments
        
        #display radar chart of specific values - this one is pace
        pace_categories = ['acceleration', 'sprint_speed']
        # array defined here, this will act as the labels for the radar chart
        N = len(pace_categories)
        # the length of this array signals how many labels/values will be on the chart
        values_of_categories = []
        # empty array defined, which will later be filled with the values corresponding to each label
        for index, value in pace.items():
                    values_of_categories.append(value)
        # for loop, iterates through the panda series assigned to each category
        # so in this case iterates through the pace variable, .items() returns a tuple of the index and value in the series
        # for loop assigns it to the variables
        # each value, so each statistic, will be appended to the previously defined empty list
        # making a list of each statistic in this category for the specified player
        values_of_categories += values_of_categories[:1]
        # this appends the first value onto the end of the list, so that it completes the circle
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        # what will be the angle of each axis in the plot? (we divide the plot / number of variable)
        # this determines the angle between each value, which is of course dependent on how many values we are making it with
        # adds this to a list, and finishes the list with the same value to complete the circle as before
        
        plt.polar(angles, values_of_categories)
        # plots the points on the graph
        plt.fill(angles, values_of_categories, alpha=0.3)
        # color the area inside the polygon
        plt.xticks(angles[:-1], pace_categories)
        # gives the graph the correct labels at each point
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        # sets labels for each circle, the color of text and the size of the text
        plt.ylim(0,100)
        # says the values must have a minimum of 0 and maximum of 100
        
        plt.show()
        # displays the graph
        
        # websites used to gain knowledge of how to create this graph:
            # - https://medium.com/python-in-plain-english/radar-chart-basics-with-pythons-matplotlib-ba9e002ddbcd
            # - https://python-graph-gallery.com/390-basic-radar-chart/
    
    
    def shooting_stats(*args):
        # functions in the same way as 'pace_stats()' function but changes the column variables to display the correct stats
        # display radar chart of specific values
        shooting_categories = ['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']
        N = len(shooting_categories)
        values_of_categories = []
        for index, value in shooting.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], shooting_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def passing_stats(*args):
        # functions in the same way as 'pace_stats()' function but changes the column variables to display the correct stats
        # display radar chart of specific values
        passing_categories = ['vision', 'crossing', 'freekick_accuracy', 'short_passing', 'long_passing', 'curve']
        N = len(passing_categories)
        values_of_categories = []
        for index, value in passing.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], passing_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def dribbling_stats(*args):
        # functions in the same way as 'pace_stats()' function but changes the column variables to display the correct stats
        # display radar chart of specific values
        dribbling_categories = ['agility', 'balance', 'reactions', 'ball_control', 'dribbling', 'composure']
        N = len(dribbling_categories)
        values_of_categories = []
        for index, value in dribbling.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], dribbling_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def defending_stats(*args):
        # functions in the same way as 'pace_stats()' function but changes the column variables to display the correct stats
        # display radar chart of specific values 
        defending_categories = ['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']
        N = len(defending_categories)
        values_of_categories = []
        for index, value in defending.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], defending_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def physicality_stats(*args):
        # functions in the same way as 'pace_stats()' function but changes the column variables to display the correct stats
        # display radar chart of specific values
        physicality_categories = ['jumping', 'stamina', 'strength', 'aggression']
        N = len(physicality_categories)
        values_of_categories = []
        for index, value in physicality.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], physicality_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75,], color = "black", size = 11)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    
    if desired_player.upper() != "EXIT":
        # if the string is not equal to 'EXIT' when changed to uppercase (meaning they have entered a valid player name) this code will execute
        print("\nThese are the categories to choose from: \n - pace\n - shooting\n - passing\n - dribbling\n - defending\n - physicality")
        category_choice = (str(input("Input the category of statistics you want to search for: ")))    
        while category_choice.lower() not in ["pace", "shooting", "passing", "dribbling", "defending", "physicality", "exit"]:
            # if the player's input is not in this list, it will ask again and this will keep looping until a value from the list is entered
            print("It must be one of these categories: \n - pace\n - shooting\n - passing\n - dribbling\n - defending\n - physicality")
            category_choice = (str(input("Input the category of statistics you want to search for: "))) 
        
        if category_choice.lower() == "pace":
            pace_stats(desired_player, player_stats, pace) 
        elif category_choice.lower() == "shooting":
            shooting_stats(desired_player, player_stats, pace) # the 'pace' variable is poorly named and should be the relevant statistic
        elif category_choice.lower() == "passing":
            passing_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "dribbling":
            dribbling_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "defending":
            defending_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "physicality":
            physicality_stats(desired_player, player_stats, pace)  
        else:
            exit_choice=True
        # if-elif-else statement that decides which statistics the user wants to display a radar chart about
        # will call the correct function based on the string input, then passing the correct information
            
        if exit_choice:
            print("\n\n -------------------------EXIT path chosen-------------------------")
            # if exit_choice variable is true (player chose to exit rather than choose category)
            # then this is displayed and application ends
        else:
            repeat_choice = input(str("Do you want to go again?\n - 'yes' to go again\n - 'menu' to return to menu\n - 'no' to exit\n\n"))
            if repeat_choice.lower() == "yes":
                radar_chart_stats()
            elif repeat_choice.lower() == "menu":
                menu()
            else:
                print("\n\n -------------------------EXIT path chosen-------------------------")
            # if the player once to goes again by entering 'yes', recursion is applied
            # the function is called again, essentially starting again from scratch
            # if the player enters anything other than 'yes' the exit path is chosen and the application ends
    else:
        print("\n\n -------------------------EXIT path chosen-------------------------")
    # if the player enters something that is not equal to 'EXIT' after upper case has been applied then the application will get the statistics
    # if the player enters 'exit' after upper case has been applied the application will stop


def most_total_stats():
    print("\n\nProcessing the data...\n")
    print("\nThis may take a while...")
    
    highest_stats_player_name = ''
    # defining string variable for player
    
    # which player has the most stats?        
    player_stats_df = pd.read_csv('fifa_cleaned.csv')
    highest_total_stats = 0
    # initialises the variable to 0 so it can be used as comparison later
    for player_index in range(0, 17954): # 17954 players based of how many index values there are
        player_stats = player_stats_df.loc[player_index]
        # .loc accesses a group of rows and columns
        # this accesses the group and rows corresponding the variable 'player_index' which is passed, which iterates with the loop
        # this index corresponds to the CSV file, it will print information pertaining to once player
        # allowing us to anlayse each players stats one by one
        
        ingame_stats = player_stats[['crossing', 'finishing', 'heading_accuracy', 'short_passing', 'dribbling', 'curve', 'freekick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'volleys', 'penalties', 'composure', 'marking', 'standing_tackle', 'sliding_tackle']] 
        # defines all the in game stats, by column name
        
        player_name = player_stats[['name', 'full_name']]
        # defines all the columns that contain player name information
        
        stat_list = []
        # creates empty list so that we can add the values of the player's stats to this list
        for index, value in ingame_stats.items():
            stat_list.append(value)
            # appends the value, which is the number relating to the stat, to the list
        total_stats = (sum(stat_list))
        # this adds together each value in the 'stat_list' list, and assigns it to the value of 'total_stats'
        # adds each stat of a player to get the total
        
        if total_stats > highest_total_stats:
            highest_total_stats = total_stats
            # value of the total
            highest_stats_player_name = player_name
            # name of the player with the most stats
        # this keeps track of each player's total in-game stats
        # on each loop/player, it will check if the player has more in-game stats
        # if the player has a larger total, it will replace the original variable with that new total
        # therefore the variable always stores the value of the player with the highest stats from the already searched players            
            
    name_information_array = highest_stats_player_name.values
    # highest_stats_player_name was originally a pandas series that contained the value and column titles of 'name' and 'full_name'
    # .values seperates this series, of column title and values, into an array containing just the values, in this case the names

    print("\nInformation of player with the most total statistics: \n")
    print("    Name - " + name_information_array[0]) # displays the player name
    print("    Full name - " + name_information_array[1]) # displays the player's full name
    print("    Amount of stats - "+ str(highest_total_stats)) # displays the total number of stats
    
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    # return to menu or exit the application, determined by user input
    
def top_players():
    df = pd.read_csv('fifa_cleaned.csv')
    print("\n\n The top 100 FIFA 19 players by overall rating: \n")
    #print(df.sort_values('overall_rating')['name']['overall_rating'].tail(10))
    top100_df = df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(100)
    # sorts the original data frame into a new data frame, that is sorted into descending order of the player's overall rating
    # this is done by the 'sort_values()' function
    # by='overall_rating' tells teh function to sort it by the column with this title
    # asending=False, tells the function to sort it into descending order
    # then I define that the only columns I want included in this data frame are the names and overall rating of the players
    # .head(20) limits it to just the first 100 players

    print(top100_df.to_string(index=False))
    # this converts the top 100 players dataframe into a string, and removes the index, to make it more readable
    
    top20_df = df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(20)
    # creates a dataframe of top 20 players using same method as before
    # displays top 20, as top 100 provided too much information, and chart was difficult to read as it was crowded
    top20_df.plot(kind='bar', x='name', y='overall_rating', rot=90, ylim=(80, 95) , grid=True)
    # using the dataframe of top 20 players, plots a bar chart, with the axis values being the player names and y values being their overall rating
    # rot=90 rotates the names 90 degrees, so they are vertical, meaning they do not overlap and are easier to read
    # grid=True, means the grid is turned on and turns the index to two, making it much easier to determine differnces in player ratings
    # the y limit is also set between 80 and 95, this is because:
        # each top 20 player rating is between these values
        # prior to these limits, the graph was too hard to read and determine the difference in ratings
        # this zooms in to between these values, making the differences much more apparent
    plt.show()
    # shows the chart in plots
    
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    
def wage_insight(): 
    print("\n\nPlease see graphs.")
    fifa_df = pd.read_csv('fifa_cleaned.csv')
    fifa_df.plot.scatter(x='overall_rating',y='wage_euro')
    # plots scatter graph for all data, the x values using the overall ratings and the y value using the wages of players
    plt.title('Correlation between rating and wage - all players')
    # sets a title for the scatter graph
    plt.show()
    # shows the graph
    print("\n\nCorrelation between rating and wage graph:")
    print("\nConclusion drawn - positive correlation between rating and wage. Proves that players who rate higher, meaning they are better players, usually earn more")
    
    big_earners = fifa_df.loc[fifa_df['wage_euro'] > 300000]
    # creates a smaller dataframe from the original, of all players earning above 300,000
    big_earners.plot.scatter(x='age', y='wage_euro')
    # plots scatter graph with age as the x value, and euros as the y value
    plt.title('Correlation between age and wage - players earning above 300,000 euros')
    # sets title for the graph
    plt.show()
    # shows the graph
    print("\n\nCorrelation between age and wage (players earning over 300,000) graph:")
    print("\nConclusion drawn - slight postive correlation between age and wage. Proves player wages may increase with wage, but not evident.")
    
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    
def data_analysis():
    print("\n\nPlease see graphs showing distribution of weak foot and skill move values. Also some basic data anlysis for facts about the data.\n\n")
    
    # The following statemetns work by obtaining a column from the overall pandas dataframe as a singular pandas series
    # Then on this pandas series, performs a function that calculates the mean, mode, min and max
    
    fifa_df = pd.read_csv('fifa_cleaned.csv')
    average_rating = round(fifa_df['overall_rating'].mean())
    # retrieves the 'overall_rating' column as a pandas series, then performs a function on this pandas series to retrieve the mean of the values
    # gets average of the 'overall_rating' column, then rounds to closest integer(whole number) using a pandas function .mean()
    print(f"The average overall rating of FIFA 19 player is {average_rating}")
    # uses f string to print the value
    
    most_common_rating = fifa_df['overall_rating'].mode()[0]
    # gets most common value of the 'overall_rating' value using the .mode() function from pandas library
    print(f"The most common rating is {most_common_rating}")
    # uses f string to print the value
    
    min_rating = fifa_df['overall_rating'].min() 
    max_rating = fifa_df['overall_rating'].max()
    print(f"The lowest rating is {min_rating} and the highest rating is {max_rating}.")
    
    min_height = fifa_df['height_cm'].min()
    max_height = fifa_df['height_cm'].max()
    height_range = max_height - min_height
    print(f"The tallest player is {max_height}cm, the shortest is {min_height}cm. That's a difference of {height_range}cm.")
    
    min_weight = fifa_df['weight_kgs'].min()
    max_weight = fifa_df['weight_kgs'].max()
    weight_range = round(max_weight - min_weight, 2)
    # rounds to decimal places
    print(f"The heaviest player is {max_weight}kg, the lightest is {min_weight}kg. That's a difference of {weight_range}kg.")
    
    oldest_player = fifa_df['age'].max()
    youngest_player = fifa_df['age'].min()
    age_range = oldest_player - youngest_player
    print(f"The oldest player is {oldest_player} years old. The youngest is {youngest_player} years old. Thats a difference of {age_range} years.")
    
    weak_foot_rating_count = fifa_df.pivot_table(index = ['weak_foot(1-5)'], aggfunc ='size') 
    # makes a smaller dataframe of the amount of times each weak foot rating shows in the database
    weak_foot_rating_count.plot.pie(y="weak_foot(1-5)", title="Weak foot rating distribution");
    # plots a pie chart of this data
    plt.ylabel('Week foot value')
    # adds a label to the graph
    plt.title('Distribution of weak foot rating')
    # adds a title to the graph
    plt.show()
    # shows the graph
    
    skill_move_rating_count = fifa_df.pivot_table(index = ['skill_moves(1-5)'], aggfunc ='size')  
    skill_move_rating_count.plot.pie(subplots=True)
    plt.ylabel('Skill move value')
    plt.title('Distribution of skill move ratings')
    plt.show()
    # same as previous graph but with skill move rating instead
    
    key = str(input("\n\n Enter 'Y', when you are ready, to return to menu. Any other input will end the application: "))
    if key.upper() == "Y":
        menu()
    


intro()
# calls intro function, in order to start the whole program
