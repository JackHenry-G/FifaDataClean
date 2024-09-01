"""
Created on Fri Sep 18 17:04:34 2020

@author: Jack Goggin
"""
import pandas as pd
import matplotlib.pyplot as plt
import time
import logging
import os
import menuUtilities
import dataUtilities

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result

handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

def display_menu():
    print("\n\n ---------------- THIS IS THE FIFA 19 VANGUARD HUB ---------------- \n\n")
    print("0. Exit application!")
    print(
        "1. Search the database for player names. Instructions:\n -  Search a player's name\n -  receive all players matching this name\n -  (Is important to know exact name for later features)")
    print("2. Get ALL the data relating to your chosen player.")
    print("3. Get the in-game statistics of a chosen player. E.g sprint speed, strength, sliding tackle, etc.")
    print("4. Get the information of a chosen player. E.g. Full name, shirt number, nationality, etc.")
    print(
        "5. Get all the career mode information of a chosen player. E.g. Release clause value, potential rating, contract end date, etc.")
    print(
        "6. Choose a player, choose a category of in-game statistics and see these statistics displayed in a radar chart.")
    print(
        "7. Answer the question - Which player has the most in-game statistics in total? Who is the most all-round player?")
    print("8. Display the top 100 players by overall rating in a list and display top 20 in a bar chart.")
    print("9. Get data analysis insights into wages and if they correlate to player rating and age.")
    print("10. Some short, simple data analysis.")

    while True:
        try:
            choice = int(input("Enter a number for what you want to do: "))

            if choice in range(11):  # Valid choices are 0 through 10
                if choice == 1:
                    search_database()
                elif choice == 2:
                    get_player_data()
                elif choice == 3:
                    ingame_stats = ['crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'freekick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'composure', 'marking', 'standing_tackle', 'GK_diving', 'GK_handling', 'GK_kicking', 'GK_positioning', 'GK_reflexes']
                    get_player_data(ingame_stats)
                elif choice == 4:
                    player_info = ['birth_date', 'age', 'height_cm', 'weight_kgs', 'positions', 'nationality', 'overall_rating', 'potential', 'preferred_foot', 'international_reputation(1-5)', 'weak_foot(1-5)', 'skill_moves(1-5)', 'work_rate', 'body_type', 'tags', 'traits']
                    get_player_data(player_info)
                elif choice == 5:
                    career_mode = ['full_name', 'positions', 'nationality', 'overall_rating', 'potential', 'value_euro', 'wage_euro', 'release_clause_euro', 'club_team', 'club_rating', 'club_position', 'club_jersey_number', 'club_join_date', 'contract_end_year', 'national_team', 'national_rating', 'national_team_position', 'national_jersey_number', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB' ]
                    get_player_data(career_mode)
                elif choice == 6:
                    radar_chart_stats()
                elif choice == 7:
                    most_total_stats()
                elif choice == 8:
                    top_players()
                elif choice == 9:
                    wage_insight()
                elif choice == 10:
                    data_analysis()
                elif choice == 0:
                    print("\nExiting...")
                    time.sleep(2)  # Delays for 2 seconds
                    print("\nThanks for using the FIFA 19 Vanguard!")
                    break  # Exit the loop and function
            else:
                print("\n !!!! It must be a number from 0 - 10 !!!!")
        except ValueError:
            print("\n !!!! You must input a valid number !!!! ")

def search_database():
    """
    Allows users to search for players in a database. This is needed as a player may search for
    Wilson, as in Callum Wilson, but there are multiple players with the last name Wilson.
    THis will return each player with 'Wilson' in there name, allowing them to specify the correct player.
    """

    df = pd.read_csv('fifa_cleaned.csv')
    player_data = df['name']
    print("\n\nHere you can search for stats belonging to a certain player")
    print("\nFirst we must make sure you are searching for the correct player")

    desired_player = (str(input("Input the player you want to search for: "))).capitalize()
    list_of_players_found = []
    for index, player_name in player_data.items():
        if desired_player in player_name:
            list_of_players_found.append(player_name)

    if len(list_of_players_found) != 0:
        print("\nPlayers found: \n")
        print('\n'.join(list_of_players_found))
        print("\nNow copy the desired players name and use this exact copy when using other features.")
    else:
        print("\nThis name was not found in the database. ")

    menuUtilities.display_return_to_menu_message()

def get_player_data(column_headers = None):
    """
    Get all data about a player, or specific data about a player
    :param column_headers: the specific data to retrieve
    """
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break

            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]

            if column_headers is not None:
                player_stats = player_stats[column_headers]

            print("\nHere are the statistics for '" + desired_player + "': \n")
            for index, value in player_stats.items():
                print(f"{index} - {value}")

            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")

    menuUtilities.display_return_to_menu_message()

def radar_chart_stats():
    player_stats = None
    while True:
        try:
            desired_player = (str(input("\nInput the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break

            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            break
        except KeyError as e:
            print("\nThat player could not be found. Please try again.")
        except Exception as e:
            logging.error(f"Something went wrong with finding a player: {e}")
            print("\nAn unexpected error occurred. Please try again.")

    if desired_player.upper() != "EXIT" and player_stats is not None:
        categories = {
            "pace": player_stats[['acceleration', 'sprint_speed']],
            "shooting": player_stats[['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']],
            "passing": player_stats[
                ['vision', 'crossing', 'freekick_accuracy', 'short_passing', 'long_passing', 'curve']],
            "dribbling": player_stats[['agility', 'balance', 'reactions', 'ball_control', 'dribbling', 'composure']],
            "defending": player_stats[['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']],
            "physicality": player_stats[['jumping', 'stamina', 'strength', 'aggression']]
        }

        valid_categories = {"pace", "shooting", "passing", "dribbling", "defending", "physicality"}
        category_choice = menuUtilities.get_category_choice("Choose which in-game stats you'd like to display in the radar chart", valid_categories)
        selected_data = categories[category_choice]

        try:
            dataUtilities.plot_radar_chart(selected_data)
        except ValueError as e:
            logging.error(f"Radar chart error: {e}")
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {e}")

        repeat_choice = input(
            "\nDo you want to go again?\n - 'yes' to go again\n - 'menu' to return to menu\n - 'no' to exit\n\n").strip().lower()
        if repeat_choice == "yes":
            radar_chart_stats()
        elif repeat_choice == "menu":
            display_menu()
        else:
            print("\nExiting the application. Thanks for using the FIFA 19 Vanguard!")
    else:
        print("\n\n -------------------------Exiting application-------------------------")


def most_total_stats():
    # Load the DataFrame
    player_stats_df = pd.read_csv('fifa_cleaned.csv')

    # Define columns for in-game stats
    stat_columns = [
        'crossing', 'finishing', 'heading_accuracy', 'short_passing', 'dribbling',
        'curve', 'freekick_accuracy', 'long_passing', 'ball_control', 'acceleration',
        'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping',
        'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
        'vision', 'volleys', 'penalties', 'composure', 'marking', 'standing_tackle',
        'sliding_tackle'
    ]

    # create a new column with the total stats for each player
    player_stats_df['total_stats'] = player_stats_df[stat_columns].sum(axis=1)

    # idxmax() finds the row where the total stats are the highest
    highest_stats_player = player_stats_df.loc[player_stats_df['total_stats'].idxmax()]

    # Extract player name and total stats
    name = highest_stats_player['name']
    full_name = highest_stats_player['full_name']
    highest_total_stats = highest_stats_player['total_stats']

    # Print results
    print("\nInformation of player with the most total statistics: \n")
    print(f"    Name - {name}")
    print(f"    Full name - {full_name}")
    print(f"    Amount of stats - {highest_total_stats}")

    menuUtilities.display_return_to_menu_message()
    
def top_players():
    """
    Prints the top 100 players and displays the top 20 in a bar chart

    """
    df = pd.read_csv('fifa_cleaned.csv')

    top100_df = df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(100)

    print("\n\n The top 100 FIFA 19 players by overall rating: \n")
    print(top100_df.to_string(index=False))

    top20_df = df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(20)
    top20_df.plot(kind='bar', x='name', y='overall_rating', rot=90, ylim=(80, 95) , grid=True)

    plt.show()

    menuUtilities.display_return_to_menu_message()
    
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
        display_menu()
    
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
    weak_foot_rating_count.plot.pie(y="weak_foot(1-5)", title="Weak foot rating distribution")
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
        display_menu()
    
if __name__ == "__main__":
    print("\n\nHello and welcome to the FIFA 19 vanguard - a database of players in FIFA 19")
    print("Search for your favourite players and see their stats on the 2019 edition of the game")
    print(
        "But that's not all! With this technology you can compare players stats - shooting, defending, potential in career mode, height; compare it all!")
    print(
        "Search for that perfect player to make your team click? Search via specific parameters to find that player! ")
    print(
        "E.g. Over 6ft, more than 80 pace, more than 84 defending, high defensive work rate. Find the players that match your needs! ")
    print("\n\nThere are 92 different types of statistic stored on each player: \n\n")

    df = pd.read_csv('fifa_cleaned.csv')  # pandas dataframe, a 2d data structure, holding rows and columns of the csv

    # tell the user what information is held about each player
    # by printing each column header
    for index, column_header in enumerate(df.columns.tolist(), start=1):
        print(f"{index} - {column_header}")

    display_menu()
