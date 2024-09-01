import numpy as np
from matplotlib import pyplot as plt


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