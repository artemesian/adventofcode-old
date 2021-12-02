with open('./input.txt') as file:
  depths = file.read()
  depths = depths.split("\n")

  def incCount(dps):
    inc = 0
    for i in range(len(dps) - 1):
      if int(dps[i])< int(dps[i+1]):
        inc+=1
    return inc

  print(f'increase count: {incCount(depths)}')

  i = 0
  cleanDepths = []
  while(i+2 < len(depths)):
    cleanDepths.append(int(depths[i]) + int(depths[i+1]) + int(depths[i+2]))
    i+=1 

  print(f'increase count with 3-windows : {incCount(cleanDepths)}')

        
        
      