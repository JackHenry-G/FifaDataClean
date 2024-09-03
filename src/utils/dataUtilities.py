import numpy as np
from matplotlib import pyplot as plt
from loguru import logger
import pandas as pd

def load_data(file_path: str, index_column: str) -> pd.DataFrame:
    """
    Load the FIFA 19 data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the FIFA 19 data, or None if loading fails.
        :param index_column: The column to index the data on
    """
    try:
        return pd.read_csv(file_path, index_col=index_column)
    except FileNotFoundError:
        logger.error("The data file was not found. Please check the file path.")
        raise
    except pd.errors.EmptyDataError:
        logger.error("The data file is empty. Please check the file content.")
        raise
    except pd.errors.ParserError:
        logger.error("Error parsing the data file. Please check the file format.")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while loading data: {e}")
        raise

def plot_radar_chart(stats):
    """
    Draws a radar chart for the given stats

    :param stats: A pandas Series object containing the player's statistics.
                                      Each index represents a specific statistic (e.g., 'acceleration',
                                      'sprint_speed', 'finishing') and the corresponding value
                                      represents the player's score for that statistic.
    :return: void
    """
    if stats.empty:
        raise ValueError("The 'stats' Series is empty. Please provide a Series with statistics.")

    # Values and categories
    values = stats.values.tolist()
    values += values[:1]  # Repeat the first value to close the loop

    # calculate angles for each axis
    number_of_stats = len(stats)
    angles = [n / float(number_of_stats) * 2 * np.pi for n in range(number_of_stats)]
    angles += angles[:1]  # Repeat the first angle to close the loop

    try:
        # Create radar chart, where figure is the windows its draw on and subplots is the actual chart
        figure, subplots = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        subplots.plot(angles, values, color='b', linewidth=2, linestyle='solid')
        subplots.fill(angles, values, color='b', alpha=0.25)

        # Set the labels for the categories
        subplots.set_xticks(angles[:-1])
        subplots.set_xticklabels(stats.index, fontsize=12, color='black')

        # Set the y-axis labels and limits
        subplots.set_yticks([25, 50, 75])
        subplots.set_yticklabels(['25', '50', '75'], color='black', size=11)
        subplots.set_ylim(0, 100)

        plt.title('Player Statistics Radar Chart', size=15, color='black', pad=20)
        plt.show()
    except ValueError as e:
        logging.error(f"Radar chart error: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

def fetch_player_stats_by_name(fifa19_db_df):
    while True:
        try:
            desired_player = (str(input("\nInput the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                return None

            return fifa19_db_df.loc[desired_player]
        except KeyError:
            print("\nThat player could not be found. Please try again.")
        except Exception as e:
            logging.error(f"Something went wrong with finding a player: {e}")
            print("\nAn unexpected error occurred. Please try again.")