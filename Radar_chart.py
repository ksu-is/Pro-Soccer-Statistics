import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
circle = np.linspace(0, 2 * np.pi, 5, endpoint=False).tolist()
circle
#%%
def plot_radar(player_stats, player_name):
    # Define the number of variables
    num_vars = len(player_stats) - 1  # Exclude 'Name' column

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop" and append the start to the end.
    stats = player_stats[1:].values.flatten().tolist()
    stats += stats[:1]
    angles += angles[:1]

    # Create the radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='red', alpha=0.25)
    ax.plot(angles, stats, color='red', linewidth=2)

    # Labels for each axis
    plt.xticks(angles[:-1], player_stats.index[1:], color='black', size=10)
    
    # Add title
    plt.title(f'Radar Chart for {player_name}', size=15, color='black', weight='bold')

    plt.show()

# Load the CSV file
def load_player_data(file_path):
    """
    Load player data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: DataFrame containing player data.
    """
    return pd.read_csv(file_path)

# Select a player's stats
def get_player_stats(data, player_name):
    """
    Get stats for a specific player.
    :param data: DataFrame containing player data.
    :param player_name: Name of the player.
    :return: Series containing the player's stats.
    """
    player_data = data[data['Name'] == player_name]
    if player_data.empty:
        raise ValueError(f"Player '{player_name}' not found in the dataset.")
    return player_data.iloc[0]

# Main function to generate radar chart
if __name__ == "__main__":
    # Load data
    file_path = "Sample_players.csv"  # Update with the correct path if needed
    try:
        data = load_player_data(file_path)
        print("Data loaded successfully:")
        print(data.head())  # Print the first few rows to verify the data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit()

    # Specify player name
    player_name = "Jude Bellingham"  # Replace with the desired player's name

    # Get player stats and plot radar chart
    try:
        player_stats = get_player_stats(data, player_name)
        print(f"Player stats for {player_name}:")
        print(player_stats)  # Print the player's stats to verify
        plot_radar(player_stats, player_name)
    except ValueError as e:
        print(e)
