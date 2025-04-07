import random


EMPTY = 0
SHIP = 1
HIT = -1
MISS = -2
GRID_SIZE = 10

def initialize_battlefield():
    return [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def can_place_ship(battlefield, row, col, size, horizontal):
    if horizontal:
        if col + size > GRID_SIZE:
            return False
        return all(battlefield[row][col + i] == EMPTY for i in range(size))
    else:
        if row + size > GRID_SIZE:
            return False
        return all(battlefield[row + i][col] == EMPTY for i in range(size))

def place_ship(battlefield, row, col, size, horizontal):
    for i in range(size):
        if horizontal:
            battlefield[row][col + i] = SHIP
        else:
            battlefield[row + i][col] = SHIP

def randomly_place_ships(battlefield):
    ship_sizes = [2, 2, 3, 3, 5, 5]
    attempts = 0

    for size in ship_sizes:
        placed = False
        while not placed:
            if attempts > 1000:
                print("Error: Couldn't place all ships. Try running again.")
                return
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            horizontal = random.choice([True, False])
            if can_place_ship(battlefield, row, col, size, horizontal):
                place_ship(battlefield, row, col, size, horizontal)
                placed = True
            attempts += 1

def display_battlefield(battlefield, reveal_ships=False):
    print("\n   " + " ".join(str(i) for i in range(GRID_SIZE)))
    for i, row in enumerate(battlefield):
        row_display = []
        for cell in row:
            if cell == HIT:
                row_display.append("H")
            elif cell == MISS:
                row_display.append("M")
            elif cell == SHIP and reveal_ships:
                row_display.append("S")
            else:
                row_display.append("~")
        print(f"{i:<2} " + " ".join(row_display))

def ships_remaining(battlefield):
    return sum(cell == SHIP for row in battlefield for cell in row)

def play_game():
    print("Welcome to Battleship!")
    print("Enter coordinates to attack (row and column between 0–9).")
    print("Enter -1 -1 to reveal all ships (cheat/debug mode).\n")

    battlefield = initialize_battlefield()
    randomly_place_ships(battlefield)

    while ships_remaining(battlefield) > 0:
        display_battlefield(battlefield)

        try:
            coords = input("Enter row and column: ").split()
            if len(coords) != 2:
                raise ValueError
            row, col = map(int, coords)
        except ValueError:
            print("Invalid input. Please enter two integers.")
            continue

        if row == -1 and col == -1:
            print("\n[DEBUG MODE] Revealing all ships:")
            display_battlefield(battlefield, reveal_ships=True)
            continue

        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            print("Invalid coordinates. Try again.")
            continue

        current = battlefield[row][col]
        if current == SHIP:
            battlefield[row][col] = HIT
            print("Hit!\n")
        elif current == EMPTY:
            battlefield[row][col] = MISS
            print("Miss!\n")
        elif current in [HIT, MISS]:
            print("You already attacked this location.\n")

    print("\nCongratulations! You sank all the ships!")
    print("Final battlefield:")
    display_battlefield(battlefield, reveal_ships=True)

if __name__ == "__main__":
    play_game()