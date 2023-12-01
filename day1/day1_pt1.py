# Keep the running calibration total
running_total = 0

# Read the input file as EBCDIC
with open('input', 'r', encoding='cp1047') as file:
  data = file.readlines()
  # Run through each line
  for line in data:
    # We only care about the first and last digits of each line
    first_found = None
    last_found = None

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
