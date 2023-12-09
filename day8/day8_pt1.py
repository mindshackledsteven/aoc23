# *      /\    *         *
#   *   //\\        *  
#      //  \\           *     ***  | 
#  *  //    \\   *            * *  |      S e v e n 9 s
#    //      \\     *         ***  | Modern Mainframe Culture
#  *//        \\                *  | 
#  //  Day 8   \\ *           ***  | 
# //____________\\   *
#       ||||  *
#   *   ||||     *    Seven9s.com - Buy a shirt or something
#--------------------------------------------------------------
# Q: Why was Santa afraid to go down the chimney?
# A: Because he was Claus-trophobic!

da_map = []
instructions = None
# Read the input file as EBCDIC
with open('input', 'r', encoding='cp1047') as file:
  data = file.readlines()

  # Run through each line
  for line in data:
    # Remove any extra crap
    line = line.strip()

    # Ignore the blank lines
    if len(line) > 0:
      # Handle a node line
      if '=' in line:
          line = line.split('=')
          start = line[0].strip()
          left = line[1].split(',')[0].replace('(','').strip()
          right = line[1].split(',')[1].replace(')','').strip()
          da_map.append({'source': start, 'left': left, 'right': right})
      else:
         instructions = line.strip()
current_node = 'AAA'
instruction = 0
step_count = 0
while current_node != 'ZZZ':
  # Reset to the beginning
  if instruction > len(instructions) - 1:
    instruction = 0
  print(instructions[instruction])
  print(current_node)
  map_node = next((item for item in da_map if item['source'] == current_node))
  if instructions[instruction] == 'R':
    current_node = map_node['right']
  else:
    current_node = map_node['left']
  step_count += 1
  instruction += 1
print(step_count)