import matplotlib.pyplot as plt
import numpy as np

def plot_radar(player_stats, player_name):
    """
    Plot a radar chart for a single player based on key performance stats.
    """
    # Labels for the radar chart axes
    labels = ['Goals', 'Assists', 'Interceptions', 'Tackles']

    # Extract the player’s values for those stats
    values = [
        player_stats['Goals'],
        player_stats['Assists'],
        player_stats['Interceptions'],
        player_stats['Tackles']
    ]

    # Setup for radar chart
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]   # repeat first value to close the circle
    angles += angles[:1]   # repeat first angle

    # Create radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles), labels)
    ax.set_title(f"{player_name} - Key Stats Radar", fontsize=14)
    ax.grid(True)

    # Show the chart
    plt.tight_layout()
    plt.show()
