# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 3   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: Why did Santa's helper see the doctor?
# A: Because they had low 'elf' esteem.

def is_number(value):
    valid_numbers = ['0','1','2','3','4','5','6','7','8','9']
    if value in valid_numbers:
        return True
    else:
        return False

def find_digit_from(haystack, line_ndx, char_ndx):
    start_line = line_ndx
    start_index = char_ndx
    end_index = char_ndx
    # Find where the digit starts
    while start_index > 0 and is_number(haystack[start_index - 1]):
        start_index -= 1
    # Find where the digit ends
    while end_index < len(haystack) - 1 and is_number(haystack[end_index]):
        end_index += 1
    return (haystack[start_index:end_index], f'({line_ndx},{start_index})')

found_gears = []
gear_ratios = 0
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    
    # Read the each line
    for i in range(len(data)):
        # For each line, find a number
        for j in range(len(data[i])):
            # Ignore everything that isn't an *
            character = data[i][j]
            if character == '*':
                adjacent_numbers = []
                # Find any adjacent numbers
                line_above = None
                line_below = None
                top_left_character = None
                top_right_character = None
                top_middle_character = None
                bottom_left_character = None
                bottom_right_character = None
                bottom_middle_character = None
                left_character = None
                right_character = None
                # Grab the lines above and below us
                if i > 0:
                    line_above = data[i - 1]
                if i < len(data) - 1:
                    line_below = data[i + 1]
                # Check the character up and left
                if line_above != None:
                    if j > 0:
                        top_left_character = line_above[j - 1]
                        if line_below != None:
                            bottom_left_character = line_below[j - 1]
                    top_middle_character = line_above[j]
                # Check the character up and right
                if line_below != None:
                    if j < len(data[i]) - 1:
                        top_right_character = line_above[j + 1]
                        if line_below != None:
                            bottom_right_character = line_below[j + 1]
                    bottom_middle_character_middle_character = line_below[j]
                # Build list of adjacent numbers and coordinates
                if top_left_character != None:
                    if is_number(top_left_character):
                        adjacent_numbers.append(find_digit_from(data[i - 1], i - 1, j - 1))
                if top_middle_character != None:
                    if is_number(top_middle_character):
                        adjacent_numbers.append(find_digit_from(data[i - 1], i - 1, j))
                if top_right_character != None:
                    if is_number(top_right_character):
                        adjacent_numbers.append(find_digit_from(data[i - 1], i - 1, j + 1))
                if bottom_left_character != None:
                    if is_number(bottom_left_character):
                        adjacent_numbers.append(find_digit_from(data[i + 1], i + 1, j - 1))
                if bottom_middle_character != None:
                    if is_number(bottom_middle_character):
                        adjacent_numbers.append(find_digit_from(data[i + 1], i + 1, j))
                if bottom_right_character != None:
                    if is_number(bottom_right_character):
                        adjacent_numbers.append(find_digit_from(data[i + 1], i + 1, j + 1))
                # Check the digits adjacent us
                if j > 0:
                    left_character = data[i][j - 1]
                if j < len(data[i]) - 1:
                    right_character = data[i][j + 1]
                if left_character != None:
                    if is_number(left_character):
                        adjacent_numbers.append(find_digit_from(data[i], i, j - 1))
                if right_character != None:
                    if is_number(right_character):
                        adjacent_numbers.append(find_digit_from(data[i], i, j + 1))

                # Remove any duplicate adjacent numbers
                adjacent_numbers = list(set(adjacent_numbers))

                # A gear has only 2 adjacent numbers
                if len(adjacent_numbers) == 2:
                    # Calculate the gear ratio
                    gear_ratio = int(adjacent_numbers[0][0]) * int(adjacent_numbers[1][0])
                    # Add the the ALMIGHTY ACCUMULATOR
                    gear_ratios += gear_ratio

# Roll that beautiful bean footage
print(gear_ratios)