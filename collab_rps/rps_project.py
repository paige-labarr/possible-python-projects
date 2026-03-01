import glob
import importlib.util
import os

def load_strategies():
    """Dynamically loads strategy modules from the current directory."""
    strategies = []
    # os.path.dirname(os.path.abspath(__file__)) gets the folder where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # glob.glob finds all files matching a pattern
    # We are looking for files that start with 'strategy_' and end with '.py'
    strategy_files = glob.glob(os.path.join(current_dir, "strategy_*.py"))
    
    for filepath in strategy_files:
        # Get the filename (e.g., "strategy_01.py") from the full path
        filename = os.path.basename(filepath)
        module_name = filename[:-3]  # remove the last 3 characters (.py)
        
        # The following lines use importlib to load the python file as a module
        # This allows us to use the code in that file without knowing its name beforehand
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # Check if the module has the required 'move' function and 'NAME' variable
            if hasattr(module, 'move') and hasattr(module, 'NAME'):
                strategies.append(module)
                
    return strategies

def get_winner(move1, move2):
    """Determines the winner of a single round."""
    if move1 == move2:
        return 0  # Tie
    
    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    if (move1 == "R" and move2 == "S") or \
       (move1 == "S" and move2 == "P") or \
       (move1 == "P" and move2 == "R"):
        return 1  # Player 1 wins
    
    return 2  # Player 2 wins

def play_match(strategy1, strategy2, rounds=33):
    """Plays a match of n rounds between two strategies."""
    wins1 = 0
    wins2 = 0
    
    # We need to track the last move made by each player
    # because strategies often base their move on what the opponent did last
    last_move_1 = None
    last_move_2 = None
    
    for _ in range(rounds):
        # Ask each strategy for their move
        # We pass the *opponent's* last move to them
        move1 = strategy1.move(last_move_2)
        move2 = strategy2.move(last_move_1)
        
        winner = get_winner(move1, move2)
        
        if winner == 1:
            wins1 += 1
        elif winner == 2:
            wins2 += 1
            
        # Update last moves for the next round
        last_move_1 = move1
        last_move_2 = move2
        
    return wins1, wins2

if __name__ == "__main__":
    # Load all strategy files found in the folder
    strategies = load_strategies()
    
    if len(strategies) < 2:
        print("Not enough strategies found to play a tournament.")
    else:
        print(f"Tournament started with {len(strategies)} strategies!")
        
        # Create a dictionary to keep track of total wins for each strategy
        tournament_wins = {}
        for strat in strategies:
            tournament_wins[strat.NAME] = 0
        
        # Round Robin Tournament: Every strategy plays every other strategy once
        # The outer loop goes from the first strategy to the second-to-last
        for i in range(len(strategies)):
            # The inner loop starts from the next strategy (i + 1) to the end
            # This ensures we don't play a strategy against itself or repeat matches
            for j in range(i + 1, len(strategies)):
                strat1 = strategies[i]
                strat2 = strategies[j]
                
                # Play the match
                score1, score2 = play_match(strat1, strat2, 33)
                
                # Update the total wins
                tournament_wins[strat1.NAME] += score1
                tournament_wins[strat2.NAME] += score2
                
                print(f"Match: {strat1.NAME} vs {strat2.NAME} -> {score1} to {score2}")
        
        print("\nFinal Scores (Total Wins):")
        
        # Sort the results by number of wins (highest to lowest)
        # .items() gives us pairs of (name, wins)
        # key=lambda x: x[1] tells sort to look at the wins (index 1)
        # reverse=True sorts in descending order
        sorted_results = sorted(tournament_wins.items(), key=lambda x: x[1], reverse=True)
        
        for name, wins in sorted_results:
            print(f"{name}: {wins}")
            
        # The first item in the sorted list is the winner
        winner_name = sorted_results[0][0]
        print(f"\n🏆 The winner is: {winner_name}!")
