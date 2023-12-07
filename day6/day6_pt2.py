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
# Q: Why was the snowman looking through the carrots?
# A: He was picking his nose

# Store the one race
race_time = 0
race_distance = 0

# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    for line in data:
        line = line.strip()
        # Build a dictionary of all the times and distances
        # Deal with time lines (milliseconds)
        if 'Time' in line:
            # We grab all the fields except the label field
            times = line.split()[1:]
            race_time = int("".join(times))
        # We assume theres a distance for every time and just update the record
        elif 'Distance' in line:
            # We grab all the fields except the label field
            distances = line.split()[1:]
            race_distance = int("".join(distances))

# Calculate possible record breaking times
# Store some datas
duration = race_time
record = race_distance
hold_time = 0
distance = 0

# Count the number of winning hold combos for each time
win_count = 0
for i in range(1, duration - 1):
    hold_time = i
    distance = i * (duration - hold_time)
    if distance > record:
        win_count += 1
        if win_count % 100 == 0:
            print(win_count)

print(win_count)