with open('./input.txt') as file:
  binary = file.read()
  binary = binary.split('\n')

  def getLowHighBit(binary):
    bit_length = len(binary[0])
    binary = list(''.join(binary))

    bit_count = {}
    for i in range(len(binary)):
      bit_index = i%bit_length

      bit_count[bit_index] = {0: 0, 1: 0} if bit_count.get(bit_index) is None else bit_count[bit_index]
      
      bit_count[bit_index][int(binary[i])] += 1
    
    gamma_rate = ""
    epsilon_rate = ""
    lowhigh_bit = {}
    for key, value in bit_count.items():
      countZero = value[0]
      countOne = value[1]

      lowhigh_bit[key] = {"min": None, "max": None}

      if countZero > countOne:
        lowhigh_bit[key]['max'] = 0
        lowhigh_bit[key]['min'] = 1
        gamma_rate += "0"
        epsilon_rate += "1"
      elif countOne > countZero:
        lowhigh_bit[key]['max'] = 1
        lowhigh_bit[key]['min'] = 0
        gamma_rate += "1"
        epsilon_rate += "0"
  
    # print(f"Rate : {int(gamma_rate, 2)}, {int(epsilon_rate, 2)}")
    # print(f"Power consumption : {int(gamma_rate, 2) * int(epsilon_rate, 2)}")

    return lowhigh_bit

  def determineRate(_binary=[], index=0, type='max'):
    if len(_binary) <= 1:
      return _binary[0]

    lowhigh = getLowHighBit(_binary)[index]
    filtered_bits = []
    i=0
    while(i<len(_binary)):
      if int(_binary[i][index]) == lowhigh[type] or (lowhigh[type] is None and int(_binary[i][index]) == (1 if type=='max' else 0)):
        filtered_bits.append(_binary[i])
        del _binary[i]
      else:
        i+=1
    
    return determineRate(_binary=filtered_bits, index=index+1, type=type)
    
  ox_rate = determineRate(_binary=binary.copy(), index=0, type='max')
  co2_rate = determineRate(_binary=binary.copy(), index=0, type='min')

  print(f"Rate(Ox, Co2): {ox_rate}, {co2_rate}")
  print(f"Product: {int(ox_rate, 2) * int(co2_rate, 2)}")
      