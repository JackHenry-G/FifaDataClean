"""
Created on Fri Sep 18 17:04:34 2020

@author: Jack Goggin
"""
import matplotlib.pyplot as plt
import config.constants as myconstants
import time
import pandas as pd
from utils import dataUtilities, menuUtilities
from loguru import logger

def display_menu() -> None:
    """
    Displays the main menu, which is terminal based, of the FIFA 19 Vanguard Hub application.
    The menu includes options for what the user can do in the application like
    searching the database, retrieving player statistics, and performing data analysis.
    """

    print("---------------- THIS IS THE FIFA 19 VANGUARD HUB ----------------\n")

    try:
        # Call the load_data function
        fifa19_db_df = dataUtilities.load_data('../data/fifa_sfacleaned.csv', 'name')
    except FileNotFoundError as e:
        logger.error(f"The specified file was not found: {e}")
        print("There was an issue getting the FIFA 19 DB file. Please try again later.")
        return
    except pd.errors.EmptyDataError as e:
        logger.error(f"The file was empty: {e}")
        print("There was an issue getting the FIFA 19 DB file. Please try again later.")
        return
    except pd.errors.ParserError as e:
        logger.error(f"The file could not be parsed: {e}")
        print("There was an issue getting the FIFA 19 DB file. Please try again later.")
        return
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print("There was an issue getting the FIFA 19 DB file. Please try again later.")
        return

    # Define menu options
    menu_options = {
        0: "Exit application!",
        1: "Search the database for player names.",
        2: "Get ALL data relating to your chosen player.",
        3: "Get in-game statistics of a chosen player (e.g., sprint speed, strength).",
        4: "Get information about a chosen player (e.g., full name, shirt number, nationality).",
        5: "Get career mode information of a chosen player (e.g., release clause value, potential rating).",
        6: "Display in-game statistics of a chosen player in a radar chart.",
        7: "Find the player with the most in-game statistics (most all-round player).",
        8: "Display the top 100 players by overall rating and the top 20 in a bar chart.",
        9: "Analyze if player wages correlate with rating and age.",
        10: "Perform some short, simple data analysis."
    }

    # Display menu options
    for key, value in menu_options.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("\n Enter a number for what you feature you would like to use: "))

            if choice in menu_options:  # Valid choices are 0 through 10
                if choice == 0:
                    print("\nExiting...")
                    time.sleep(2)  # Delays for 2 seconds
                    print("\nThanks for using the FIFA 19 Vanguard!")
                    break  # Exit the loop and function
                elif choice == 1:
                    search_database(fifa19_db_df)
                elif choice == 2:
                    get_player_data(fifa19_db_df)
                elif choice == 3:
                    get_player_data(fifa19_db_df, myconstants.INGAME_STATS_DATA)
                elif choice == 4:
                    get_player_data(fifa19_db_df, myconstants.PLAYER_INFO_DATA)
                elif choice == 5:
                    get_player_data(fifa19_db_df, myconstants.CAREER_MODE_DATA)
                elif choice == 6:
                    radar_chart_stats(fifa19_db_df)
                elif choice == 7:
                    most_total_stats(fifa19_db_df)
                elif choice == 8:
                    top_players(fifa19_db_df)
                elif choice == 9:
                    wage_insight(fifa19_db_df)
                elif choice == 10:
                    data_analysis(fifa19_db_df)
            else:
                print("\n !!!! It must be a number from 0 - 10 !!!!")
        except ValueError:
            print("\n !!!! You must input a valid number !!!! ")

def search_database(fifa19_db_df):
    """
    Allows users to search for players in a database. This is needed as a player may search for
    Wilson, as in Callum Wilson, but there are multiple players with the last name Wilson.
    THis will return each player with 'Wilson' in their name, allowing them to specify the correct player.
    """
    print("\n\nHere you can search for stats belonging to a certain player")
    print("\nFirst we must make sure you are searching for the correct player")

    desired_player = (str(input("Input the player you want to search for: "))).capitalize()
    list_of_players_found = [player_name for player_name in fifa19_db_df.index.values if desired_player in player_name]

    if len(list_of_players_found) != 0:
        print("\nPlayers found: ", ' | '.join(list_of_players_found))
        print("\nNow copy the desired players name and use this exact copy when using other features.")
    else:
        print("\nThis name was not found in the database. ")

    menuUtilities.display_return_to_menu_message()

def get_player_data(fifa19_db_df, column_headers = None):
    """
    Get all data about a player, or specific data about a player
    :param fifa19_db_df: dataframe to search
    :param column_headers: the specific data to retrieve
    """
    specific_player_stats = dataUtilities.fetch_player_stats_by_name(fifa19_db_df)

    if column_headers is not None:
        player_stats = specific_player_stats[column_headers]

    print("\nHere are the player's stats")
    for index, value in specific_player_stats.items():
        print(f"{index} - {value}")


    menuUtilities.display_return_to_menu_message()



def radar_chart_stats(fifa19_db_df):
    # find specific player's stats
    specific_player_stats = dataUtilities.fetch_player_stats_by_name(fifa19_db_df)

    # select which category of stats to display
    if specific_player_stats is not None:
        category_choice = menuUtilities.get_category_choice("Choose which in-game stats you'd like to display in the radar chart", myconstants.INGAME_STATS_CATEGORIES_DATA.keys())
        selected_data = specific_player_stats[myconstants.INGAME_STATS_CATEGORIES_DATA[category_choice]]

        # draw radar chart with stats
        dataUtilities.plot_radar_chart(selected_data)
    else:
        print("No data could be found about this player.")

    menuUtilities.display_return_to_menu_message()


def most_total_stats(fifa19_db_df):
    # create a new column with the total stats for each player
    fifa19_db_df['total_stats'] = fifa19_db_df[myconstants.INGAME_STATS_DATA].sum(axis=1)

    # idxmax() finds the row where the total stats are the highest
    highest_stats_player = fifa19_db_df.loc[fifa19_db_df['total_stats'].idxmax()]

    # Extract player name and total stats
    name = highest_stats_player['name']
    club_team = highest_stats_player['club_team']
    highest_total_stats = highest_stats_player['total_stats']

    # Print results
    print("\nInformation of player with the most total statistics: \n")
    print(f"    Name - {name}")
    print(f"    Club - {club_team}")
    print(f"    Amount of stats - {highest_total_stats}")

    menuUtilities.display_return_to_menu_message()
    
def top_players(fifa19_db_df):
    """
    Prints the top 100 players and displays the top 20 in a bar chart

    """
    top100_df = fifa19_db_df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(100)

    print("\n\n The top 100 FIFA 19 players by overall rating: \n")
    print(top100_df.to_string(index=False))

    top20_df = fifa19_db_df.sort_values(by='overall_rating', ascending=False)[['name', 'overall_rating']].head(20)
    top20_df.plot(kind='bar', x='name', y='overall_rating', rot=90, ylim=(80, 95) , grid=True)

    plt.show()

    menuUtilities.display_return_to_menu_message()
    
def wage_insight(fifa19_db_df):
    print("\n\nPlease see graphs.")
    fifa19_db_df.plot.scatter(x='overall_rating',y='wage_euro')
    # plots scatter graph for all data, the x values using the overall ratings and the y value using the wages of players
    plt.title('Correlation between rating and wage - all players')
    # sets a title for the scatter graph
    plt.show()
    # shows the graph
    print("\n\nCorrelation between rating and wage graph:")
    print("\nConclusion drawn - positive correlation between rating and wage. Proves that players who rate higher, meaning they are better players, usually earn more")
    
    big_earners = fifa19_db_df.loc[fifa19_db_df['wage_euro'] > 300000]
    # creates a smaller dataframe from the original, of all players earning above 300,000
    big_earners.plot.scatter(x='age', y='wage_euro')
    # plots scatter graph with age as the x value, and euros as the y value
    plt.title('Correlation between age and wage - players earning above 300,000 euros')
    # sets title for the graph
    plt.show()
    # shows the graph
    print("\n\nCorrelation between age and wage (players earning over 300,000) graph:")
    print("\nConclusion drawn - slight postive correlation between age and wage. Proves player wages may increase with wage, but not evident.")

    menuUtilities.display_return_to_menu_message()

def data_analysis(fifa19_db_df):
    print("\n\nPlease see graphs showing distribution of weak foot and skill move values. Also some basic data anlysis for facts about the data.\n\n")
    
    # The following statements work by obtaining a column from the overall pandas dataframe as a singular pandas series
    # Then on this pandas series, performs a function that calculates the mean, mode, min and max

    average_rating = round(fifa19_db_df['overall_rating'].mean())
    # retrieves the 'overall_rating' column as a pandas series, then performs a function on this pandas series to retrieve the mean of the values
    # gets average of the 'overall_rating' column, then rounds to closest integer(whole number) using a pandas function .mean()
    print(f"The average overall rating of FIFA 19 player is {average_rating}")
    # uses f string to print the value
    
    most_common_rating = fifa19_db_df['overall_rating'].mode()[0]
    # gets most common value of the 'overall_rating' value using the .mode() function from pandas library
    print(f"The most common rating is {most_common_rating}")
    # uses f string to print the value
    
    min_rating = fifa19_db_df['overall_rating'].min()
    max_rating = fifa19_db_df['overall_rating'].max()
    print(f"The lowest rating is {min_rating} and the highest rating is {max_rating}.")
    
    min_height = fifa19_db_df['height_cm'].min()
    max_height = fifa19_db_df['height_cm'].max()
    height_range = max_height - min_height
    print(f"The tallest player is {max_height}cm, the shortest is {min_height}cm. That's a difference of {height_range}cm.")
    
    min_weight = fifa19_db_df['weight_kgs'].min()
    max_weight = fifa19_db_df['weight_kgs'].max()
    weight_range = round(max_weight - min_weight, 2)
    # rounds to decimal places
    print(f"The heaviest player is {max_weight}kg, the lightest is {min_weight}kg. That's a difference of {weight_range}kg.")
    
    oldest_player = fifa19_db_df['age'].max()
    youngest_player = fifa19_db_df['age'].min()
    age_range = oldest_player - youngest_player
    print(f"The oldest player is {oldest_player} years old. The youngest is {youngest_player} years old. Thats a difference of {age_range} years.")
    
    weak_foot_rating_count = fifa19_db_df.pivot_table(index = ['weak_foot(1-5)'], aggfunc ='size')
    # makes a smaller dataframe of the amount of times each weak foot rating shows in the database
    weak_foot_rating_count.plot.pie(y="weak_foot(1-5)", title="Weak foot rating distribution")
    # plots a pie chart of this data
    plt.ylabel('Week foot value')
    # adds a label to the graph
    plt.title('Distribution of weak foot rating')
    # adds a title to the graph
    plt.show()
    # shows the graph
    
    skill_move_rating_count = fifa19_db_df.pivot_table(index = ['skill_moves(1-5)'], aggfunc ='size')
    skill_move_rating_count.plot.pie(subplots=True)
    plt.ylabel('Skill move value')
    plt.title('Distribution of skill move ratings')
    plt.show()
    # same as previous graph but with skill move rating instead

    menuUtilities.display_return_to_menu_message()

if __name__ == "__main__":
    welcome_text = """
        Welcome to the FIFA 19 Vanguard - your comprehensive database for players in FIFA 19!

        Search for your favorite players and view their stats from the 2019 edition of the game.

        But that's not all! With our advanced technology, you can:
        - Compare player stats including shooting, defending, potential in career mode, height, and more.
        - Find the perfect player for your team by searching specific parameters.

        For example, search for players who are:
        - Over 6ft tall
        - Have more than 80 pace
        - More than 84 defending
        - High defensive work rate

        Find players that match your exact needs and make your team excel!
        """

    print(welcome_text)
    display_menu()