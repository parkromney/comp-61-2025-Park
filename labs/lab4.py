import random

def roll_die():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    rolls = [roll_die() for _ in range(num_dice)]
    print(f"Rolled dice: {rolls}")
    return sum(rolls)

def get_round_result(player_total, computer_total):
    if(player_total > computer_total):
        return "Win"
    elif(player_total < computer_total):
        return "Loss"
    else:
        return "Draw"

def shop(score):
    while(True):
        print("\nShop Menu:")
        print("1. Add +5 points (Cost: 5 points)")
        print("2. Add +15 points (Cost: 10 points)")
        print("3. Exit Shop")
        choice = input("Enter your choice: ")
        
        if(choice == "1" and score >= 5):
            score -= 5
            print("You gained 5 points!")
        elif(choice == "2" and score >= 10):
            score -= 10
            print("You gained 15 points!")
        elif(choice == "3"):
            break
        else:
            print("Not enough points or invalid choice.")
    return score

def display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results):
    print("\nGame Summary:")
    print(f"Total Rounds Played: {rounds}")
    print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
    print(f"Final Score: {score}\n")
    
    print("Round History:")
    for i in range(len(round_numbers)):
        print(f"Round {round_numbers[i]}: Player {player_totals[i]} vs Computer {computer_totals[i]} -> {results[i]}")

random.seed()
score = 0
rounds = 0
wins = 0
draws = 0
losses = 0
round_numbers = []
player_totals = []
computer_totals = []
results = []

while(True):
    rounds += 1
    print(f"\nRound {rounds}")
    if(input("Do you want to visit the shop? (yes/no): ").lower() == "yes"):
        score = shop(score)
    
    player_total = roll_multiple_dice(2)
    computer_total = roll_multiple_dice(2)
    result = get_round_result(player_total, computer_total)
    
    if(result == "Win"):
        wins += 1
        score += 20
    elif(result == "Draw"):
        draws += 1
        score += 10
    else:
        losses += 1
    
    round_numbers.append(rounds)
    player_totals.append(player_total)
    computer_totals.append(computer_total)
    results.append(result)
    
    print(f"Result: {result}")
    print(f"Current Score: {score}")
    
    if(input("Do you want to play another round? (yes/no): ").lower() != "yes"):
        break

display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results)
