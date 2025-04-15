from data_loader import load_player_data
from visualizer import plot_radar

def main():
    filepath = 'data/sample_players.csv'  # path to your CSV file
    df = load_player_data(filepath)       # load the data using pandas

    if df is not None:
        print("\n📋 Available players:")
        for name in df['Name']:
            print(f"- {name}")

        player_name = input("\nType the exact name of a player to view their radar chart: ")

        player_row = df[df['Name'] == player_name]

        if not player_row.empty:
            player_stats = player_row.iloc[0]
            plot_radar(player_stats, player_name)
        else:
            print("\n❌ Player not found in dataset. Check spelling and capitalization.")

if __name__ == "__main__":
    main()
