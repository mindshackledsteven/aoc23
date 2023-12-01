# Keep the running calibration total
running_total = 0

# Keep track of the valid numbers as words
valid_numwords = [ ('nine', '9'), ('eight', '8'),
                   ('seven', '7'), ('six', '6'),
                   ('five', '5'), ('four', '4'),
                   ('three', '3'), ('two', '2'),
                   ('one', '1') ]

# Read the input file as EBCDIC
with open('input', 'r', encoding='cp1047') as file:
  data = file.readlines()
  # Run through each line
  for line in data:
    # Strip whitespace off line
    line = line.strip()

    # We only care about the first and last digits of each line
    first_found = None
    last_found = None

    # Prepare to brute force this
    leftmost_index = -1
    leftmost_value = ""
    leftmost_word = ""
    rightmost_index = -1
    rightmost_value = ""
    rightmost_word = ""

    # Skip looking for a leftmost word if the first character is a number
    # This could probably be smarter, but it's late
    if not line[0].isnumeric():
      # Find the leftmost word
      for word, value in valid_numwords:
        # Locate the leftmost word
        first_index = line.find(word)
        if first_index != -1:
          if leftmost_value == "":
            leftmost_index = first_index
            leftmost_value = value
            leftmost_word = word
          if first_index < leftmost_index:
            leftmost_index = first_index
            leftmost_value = value
            leftmost_word = word

      # Replace the located word
      if leftmost_index != -1:
        line = line[:leftmost_index] + leftmost_value + line[leftmost_index + len(leftmost_word):]

    # Skip looking for the rightmost word if the last character is a number
    # Same as above
    if not line[len(line) - 1].isnumeric():
      # Find the rightmost word
      for word, value in valid_numwords:
        # Locate the rightmost word
        last_index = line.rfind(word)
        if last_index != -1:
          if rightmost_value == "":
            rightmost_index = last_index
            rightmost_value = value
            rightmost_word = word
          if last_index > rightmost_index:
            rightmost_index = last_index
            rightmost_value = value
            rightmost_word = word

      if rightmost_index != -1:
        line = line[:rightmost_index] + rightmost_value + line[rightmost_index + len(rightmost_word):]

    # Run through each character of each line
    for character in line:
      # Only process numbers
      if character.isnumeric():
        # Only store the first and last digits as numbers
        if first_found is None:
          first_found = character
        else:
          last_found = character
 
    # Combine the digits
    final_num = first_found
    # Duplicate the first number if there is no second
    if last_found is not None:
      final_num += last_found
    else:
      final_num += first_found

    # Convert to a digit and add to total
    final_num = int(final_num)
    running_total += final_num

print(running_total) 
