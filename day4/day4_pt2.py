# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 4   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: What do you call an elf who rhymes?
# A: A wrapper

# We keep a stack of cards like the Bozo Grand Prize Game
card_stack = None

# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    # Initialize our stack
    card_stack = {}
    for i in range (1, len(data) + 1):
        card_stack[i] = 1

    # Run through the stack of cards
    for line in data:
        line = line.strip()

        # Get the game numbers
        card_number = line.split(':')[0].split()[1]
        card_number = int(card_number)
        numbers = line.split(':')[1]
        winning_numbers = numbers.split('|')[0]
        winning_numbers = winning_numbers.split()
        player_numbers = numbers.split('|')[1]
        player_numbers = player_numbers.split()

        # Count the winners
        winner_count = 0
        for number in player_numbers:
            if number in winning_numbers:
                winner_count += 1

        # Add the number of cards to each bucket for each win for this card
        for i in range(winner_count):
            card_stack[card_number + i + 1] += 1 * card_stack[card_number]

# Sum the count of each type of card
rolling_sum = 0
for value in card_stack.values():
    rolling_sum += value
print(rolling_sum)