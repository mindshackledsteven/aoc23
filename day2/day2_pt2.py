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
power_accumulator = 0

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

        max_red = 0
        max_green = 0
        max_blue = 0

        # Break the draws into color
        for draw in draws:
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

            # Set the upper bounds for each color
            if draw_red > max_red:
                max_red = draw_red
            if draw_green > max_green:
                max_green = draw_green
            if draw_blue > max_blue:
                max_blue = draw_blue

        game_power = max_red * max_green * max_blue
        power_accumulator += game_power

print(power_accumulator)