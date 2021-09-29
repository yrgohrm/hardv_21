def rps(player1, player2):
    if type(player1) is not str or \
        type(player2) is not str:
        raise TypeError("argument must be a string")

    correct = ["rock", "paper", "scissors"]
    if player1 not in correct or player2 not in correct:
        raise ValueError(f"Bad value, only {correct} allowed")

    if player1 == player2:
        return 0

    if (player1 == "rock" and player2 == "paper") or \
        (player1 == "paper" and player2 == "scissors") or \
        (player1 == "scissors" and player2 == "rock"):
        return 2

    return 1
