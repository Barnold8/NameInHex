##Your name in HEX
import math
import string
Hex_Table = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
a = 0
b = a
Default_Value = "AF" #10x16^1 + 10x16^0
alphabet = list(string.ascii_lowercase)

def NameToNum(Name, debug= False):
  N_list = list(Name.lower())
  Conv_List = []
  for i in range(len(N_list)):
    Conv_List.append(alphabet.index(N_list[i])+1)
  if debug: 
    print(f"Name: {N_list}\n\nNumber representation of name: {Conv_List}")
  return Conv_List
    

def HexConv(T_Type,Value):
  global a, b
  new_value = 0
  powcounter = 0
  if T_Type.upper() == "H2D":
    x =  list(Value)
    y = 0
    for i in range(len(x)-1,-1,-1):

      if x[i] in Hex_Table:
        y += Hex_Table[x[i]] * pow(16,powcounter)
        powcounter += 1
      else:
        y+= int(x[i]) * pow(16,powcounter)
        powcounter += 1

    return y
  
  if T_Type.upper() == "D2H":
    f = [0,0]

    if type(Value) == list:

      for i in range(len(Value)):
        new_value += Value[i]
        a = 0
        b = 0
    elif type(Value) == int:
      new_value = Value
    else:
      print(type(Value))
    while new_value >=1:

       if new_value >=16:
         a += int(new_value / 16)
         f[0] = a
         new_value -= a * 16
         
       elif new_value <16:
         b = new_value
         new_value  -= b
         
    f[1] = b
    f[0] = a
    
    for i in range(len(f)):
      if f[i] >= 9:
         listOfKeys = [key  for (key, value) in Hex_Table.items() if value == f[i]]
         f[i] = listOfKeys[0]
    return f
         

x = NameToNum("Brandon")

new_name = []

for i in range(len(x)):
  new_name.append(HexConv("D2H",x[i]))
print(new_name)



