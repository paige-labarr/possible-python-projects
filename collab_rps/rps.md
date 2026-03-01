# Rock Paper Scissors Tournament

This project runs a round-robin tournament between different Rock Paper Scissors strategies defined in separate Python files.

## Files

### 1. `rps_project.py`
This is the **Tournament Engine**.
- **Dynamic Loading:** It automatically finds any file in the folder that starts with `strategy_` and imports it as a player.
- **Matchmaking:** It ensures every strategy plays against every other strategy exactly once (Round Robin).
- **Scoring:** It tracks the total number of wins for each strategy across the entire tournament.

### 2. `strategy_*.py` (e.g., `strategy_01.py`)
These files represent the **Players**.
- **Structure:** Each file must contain:
    - A variable `NAME` (the name of the bot).
    - A function `move(previous_opponent_move)` that returns "R", "P", or "S".
- **Logic:** The code inside determines how the bot behaves (e.g., playing randomly, copying the opponent, or using a pattern).

## How the Tournament Works

1. **Setup:** The script scans the folder and loads all valid strategy files.
2. **The Matches:**
    - Every pair of strategies plays a match consisting of **33 rounds**.
    - In each round, the strategies are passed their opponent's last move so they can adapt.
3. **Scoring:**
    - A win grants 1 point. A tie grants 0 points.
    - At the end of all matches, the strategy with the highest total number of wins is declared the **Grand Champion**!