# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 6   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: Why was the computer cold on Christmas?
# A: Because it left its Windows open.

# all five cards have the same label: AAAAA
def is_5oak(hand):
    if len(set(hand)) == 1:
        return True
    else:
        return False

# four cards have the same label and one card has a different label: AA8AA
def is_4oak(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (sorted(char_count.values()) == [1, 4])

# three cards have the same label, and the remaining two cards share a different label
def is_full_house(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return (sorted(char_count.values()) == [2, 3])

# three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
def is_3oak(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (sorted(char_count.values()) == [1, 1, 3])

# two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def is_2pair(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (sorted(char_count.values()) == [1, 2, 2])

# two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def is_1pair(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (sorted(char_count.values()) == [1, 1, 1, 2])

# all cards' labels are distinct: 23456
def is_high_card(hand):
    char_count = {}
    for char in hand:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return (sorted(char_count.values()) == [1, 1, 1, 1, 1])

# Returns the type of hand
def compare_hands(hand1):
    hand1 = hand1['hand']
    # Convert to hex
    hand1 = hand1.replace('A','E')
    hand1 = hand1.replace('K','D')
    hand1 = hand1.replace('Q','C')
    hand1 = hand1.replace('J','B')
    hand1 = hand1.replace('T','A')
    return int(hand1,16)

hands = []
# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()

    # For every hand, give it a type
    for line in data:
        hand = line.split()[0]
        bid = int(line.split()[1])

        type = 0
        if is_5oak(hand):
            type = 7
        elif is_4oak(hand):
            type = 6
        elif is_full_house(hand):
            type = 5
        elif is_3oak(hand):
            type = 4
        elif is_2pair(hand):
            type = 3
        elif is_1pair(hand):
            type = 2
        elif is_high_card(hand):
            type = 1
        
        hands.append({'hand': hand, 'type': type, 'bid': bid, 'rank': None})

# Sort the hands by their type
hands = sorted(hands, key=lambda type: type['type'], reverse=True)

# Sort the hands by type
types = {}
for hand in hands:
    if hand['type'] not in types:
        types[hand['type']] = []
    types[hand['type']].append(hand)

# Rank the types
current_rank = len(hands)
print(current_rank)
for hands_of_type in types.items():
    type = hands_of_type[0]
    this_type = hands_of_type[1]
    this_type = sorted(this_type, key=compare_hands, reverse=True)
    for _ in this_type:
        _['rank'] = current_rank
        current_rank -= 1

accumulator = 0
for hand in hands:
    accumulator += hand['rank'] * hand['bid']
print(accumulator)
