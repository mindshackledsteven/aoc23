# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 2   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something

# Keep tally of possible games
possible_accumulator = 0

with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    for line in data:
        # Clear any extra space
        line = line.strip()

        # Grab the game number
        game_number = int(line.split(':')[0].split()[1])
        
        # Grab the draws from each game
        draws = line.split(':')[1].split(';')

        game_possible = True

        # Break the draws into color
        for draw in draws:
            max_red = 12
            max_green = 13
            max_blue = 14
            draw_red = 0
            draw_green = 0
            draw_blue = 0
            # Split the draw into words
            split = draw.split()
            # Run through each word
            for i in range(len(split)):
                # if the word is a number
                if split[i].isdigit():
                    # Store the count
                    count = split[i]
                    # Store the color
                    color = split[i + 1].replace(',','')
                    if color == 'red':
                        draw_red = int(count)
                    elif color == 'green':
                        draw_green = int(count)
                    elif color == 'blue':
                        draw_blue = int(count)

            # print('Reds', max_red - draw_red)
            # print('Greens', max_green - draw_green)
            # print('Blues', max_blue - draw_blue)
            if game_possible is not False:
                game_possible = draw_red <= max_red and draw_green <= max_green and draw_blue <= max_blue

        print(game_number, game_possible)
        if game_possible:
            possible_accumulator += game_number

print(possible_accumulator)
