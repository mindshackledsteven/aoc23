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

import math


def all_nodes_finished(check):
  retval = True
  for node in nodes_ending_a:
    if node['current']['source'][2] != 'Z':
      retval = False
  return retval

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
         
# Find all nodes that end in A
nodes_ending_a = []
index = 0
for node in da_map:
  if node['source'][2] == 'A':
    nodes_ending_a.append({'index': index, 'current': node})
  index += 1

step_counts = []
# Advance each and track the number of steps
for node in nodes_ending_a:
  current = node['current']
  instruction = 0
  step_count = 0
  while current['source'][2] != 'Z':
    if instruction > len(instructions) - 1:
      instruction = 0
    if instructions[instruction] == 'R':
      map_node = next((i for i, item in enumerate(da_map) if item['source'] == node['current']['right']))
      node['index'] = map_node
      node['current'] = da_map[map_node]
      current = node['current']
    else:
      map_node = next((i for i, item in enumerate(da_map) if item['source'] == node['current']['left']))
      node['index'] = map_node
      node['current'] = da_map[map_node]
      current = node['current']
    instruction += 1
    step_count += 1
  node['step_count'] = step_count
  step_counts.append(step_count)

# Reduce the step counts set
step_counts = list(set(step_counts))

result = step_counts[0]
# Calculate the Lowest common multiple
for val in step_counts[1:]:
  result = math.lcm(result, val)

print(result)

# # Check if all nodes are currently ending in Z
# instruction = 0
# step_count = 0
# while not all_nodes_finished(nodes_ending_a):
#   # Reset to the beginning
#   if instruction > len(instructions) - 1:
#     instruction = 0
#   # Advance each node
#   for node in nodes_ending_a:
#     if instructions[instruction] == 'R':
#       # Get the index of the map node we're going to
#       map_node = next((i for i, item in enumerate(da_map) if item['source'] == node['current']['right']))
#       node['index'] = map_node
#       node['current'] = da_map[map_node]
#     else:
#       map_node = next((i for i, item in enumerate(da_map) if item['source'] == node['current']['left']))
#       node['index'] = map_node
#       node['current'] = da_map[map_node]
#   step_count += 1
#   instruction += 1
#   if step_count % 100 == 0:
#     print(step_count)
# print(step_count)