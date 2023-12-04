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

# Read the input data
grand_total = 0
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    
    for line in data:
        line = line.strip()
        # Get the card number
        card = line.split(':')[0]
        card_number = card.split()[1]

        # Get the game numbers
        numbers = line.split(':')[1]
        winning_numbers = numbers.split('|')[0]
        winning_numbers = winning_numbers.split()
        player_numbers = numbers.split('|')[1]
        player_numbers = player_numbers.split()

        winner_count = 0
        for number in player_numbers:
            if number in winning_numbers:
                winner_count += 1

        if winner_count == 1:
            grand_total += 1
        elif winner_count == 2:
            grand_total += 2
        elif winner_count == 3:
            grand_total += 4
        elif winner_count == 4:
            grand_total += 8
        elif winner_count == 5:
            grand_total += 16
        elif winner_count == 6:
            grand_total += 32
        elif winner_count == 7:
            grand_total += 64
        elif winner_count == 8:
            grand_total += 128
        elif winner_count == 9:
            grand_total += 256
        elif winner_count == 10:
            grand_total += 512
        elif winner_count == 11:
            grand_total += 1024
        elif winner_count == 5:
            grand_total += 16
        elif winner_count == 5:
            grand_total += 16
        
print(grand_total)