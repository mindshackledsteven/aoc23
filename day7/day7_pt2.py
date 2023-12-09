# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 7   \\ *           ***  | 
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
    hand1 = hand1['original']
    # Convert to hex
    hand1 = hand1.replace('A','D')
    hand1 = hand1.replace('K','C')
    hand1 = hand1.replace('Q','B')
    hand1 = hand1.replace('T','A')
    # J is now the weakest
    hand1 = hand1.replace('J','1')
    val = int(hand1,16)
    return val

hands = []
possible_cards = ['2','3','4','5','6','7','8','9','T','Q','K','A']
# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()

    # For every hand, give it a type
    for line in data:
        hand = line.split()[0]
        bid = int(line.split()[1])

        # Determine optimal type for this hand
        if 'J' in hand:
            highest_type = 0
            # Save original hand before we replace
            original_hand = hand
            optimized_hand = hand
            # Count the Jokers
            char_count = {}
            for char in hand:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            if char_count['J'] > 1:
                print(sorted(char_count.items()))
            for pcard in possible_cards:
                # Save "optimized" hand
                test_hand = hand.replace('J', pcard)
                if is_5oak(test_hand):
                    type = 7
                    if type >= highest_type:
                        highest_type = 7
                        optimized_hand = test_hand
                elif is_4oak(test_hand):
                    type = 6
                    if type >= highest_type:
                        highest_type = 6
                        optimized_hand = test_hand
                elif is_full_house(test_hand):
                    type = 5
                    if type >= highest_type:
                        highest_type = 5
                        optimized_hand = test_hand
                elif is_3oak(test_hand):
                    type = 4
                    if type >= highest_type:
                        highest_type = 4
                        optimized_hand = test_hand
                elif is_2pair(test_hand):
                    type = 3
                    if type >= highest_type:
                        highest_type = 3
                        optimized_hand = test_hand
                elif is_1pair(test_hand):
                    type = 2
                    if type >= highest_type:
                        highest_type = 2
                        optimized_hand = test_hand
                elif is_high_card(test_hand):
                    type = 1
                    if type >= highest_type:
                        highest_type = 1
                        optimized_hand = test_hand
            # print(original_hand, optimized_hand, highest_type)
            hands.append({'original': original_hand, 'optimized': optimized_hand, 'type': highest_type, 'bid': bid, 'rank': None})
        else:
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
            hands.append({'original': hand, 'optimized': hand, 'type': type, 'bid': bid, 'rank': None})

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
hands = sorted(hands, key=lambda rank: rank['rank'], reverse=True)
for hand in hands:
    print(hand)
    accumulator += hand['rank'] * hand['bid']
print(accumulator)
