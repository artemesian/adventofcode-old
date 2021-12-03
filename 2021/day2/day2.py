with open('./input.txt') as file:
  instructions = file.read()
  instructions = instructions.split('\n')
#             x, y          
  position = [0, 0]

  for i in range(len(instructions)):
    instruct = instructions[i].split(' ')
    if instruct[0] == 'forward':
      position[0] += int(instruct[1])
    elif instruct[0] == 'down':
      position[1] += int(instruct[1])
    elif instruct[0] == 'up':
      position[1] -= int(instruct[1])
    else:
      pass
  
  print(f"1st Submarine co-ordinates:  {position}")
  print(f"1st product:  {position[0] * position[1]}")

#             x, y, aim          
  position = [0, 0, 0]
  
  for i in range(len(instructions)):
    instruct = instructions[i].split(' ')
    if instruct[0] == 'forward':
      position[0] += int(instruct[1])
      position[1] += position[2] * int(instruct[1])
    elif instruct[0] == 'down':
      position[2] += int(instruct[1])
    elif instruct[0] == 'up':
      position[2] -= int(instruct[1])
    else:
      pass
  
  print(f"2nd Submarine co-ordinates:  {position}")
  print(f"2nd product:  {position[0] * position[1]}")