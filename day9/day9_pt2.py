# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 9   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: How does a snowman get around?
# A: On his "icicle".

# Read the input data
with open('input', 'r', encoding='cp1047') as file:
    data = file.readlines()
    
    accumulator = 0
    # Factor each one to zero
    for line in data:
        line = line.strip()

        # Strip the line into integer values
        values = [int(val) for val in line.split()]

        # Make a list of all the factors for this reading
        factors = []
        # Add initial list to the factors
        factors.append(values)
        step_size = -1
        factors_added = 0
        # Calculate until the step size is 0
        last_value = None
        while step_size != 0:
            new_values = []
            for i in range(len(values)):
                if i + 1 < len(values):
                    step_size = values[i + 1] - values[i]
                    new_values.append(step_size)
            factors.append(new_values)
            factors_added += 1
            # Assign step size to the largest of the values in this new range
            for value in new_values:
                if value != 0:
                    step_size = value
                    break
            values = new_values
            last_value = new_values
        print(last_value)
        # Run through the factors and predict the first number
        # We can skip the 0 factor
        for i in range(len(factors) - 2, -1, -1):
            # Subtract the previous last value to our last value
            previous_value = factors[i+1][0]
            this_value = factors[i][0]
            factors[i].insert(0, this_value - previous_value)
        # Pop any added factors
        for i in range(factors_added):
            factors.pop(len(factors)-1)
        # print("FINAL",factors)
        for factor in factors:
            accumulator += factor[0]
    print(accumulator)