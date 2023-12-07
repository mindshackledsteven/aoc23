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

# Store all those races
races = []

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
            for i in range(len(times)):
                # Times come first so add them to the list
                races.insert(i, {'time':times[i]})
                print(i, times[i])
        # We assume theres a distance for every time and just update the record
        elif 'Distance' in line:
            # We grab all the fields except the label field
            distances = line.split()[1:]
            for i in range(len(distances)):
                races[i]['distance'] = distances[i]

# Calculate possible record breaking times
for race in races:
    # Store some datas
    duration = int(race['time'])
    record = int(race['distance'])
    hold_time = 0
    distance = 0

    # Count the number of winning hold combos for each time
    race['winning_holds'] = []
    for i in range(1, duration - 1):
        hold_time = i
        distance = i * (duration - hold_time)
        if distance > record:
            race['winning_holds'].append(hold_time)

result = 1
for race in races:
    result = result * len(race['winning_holds'])
print(result)