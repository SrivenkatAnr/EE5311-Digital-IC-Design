x = int(input("Enter the Multiplicand value: "))
y = int(input("Enter the Multiplier Value: "))
t = float(input("Enter the time (in ns) at which inputs should transistion: "))

if x<-128 or x>127 or y<-128 or y>127:
	raise ValueError("Please enter valid inputs for a 8 bit multiplier!!")
x_2s = ("{0:0>8}").format(bin(x & int("1"*8, 2))[2:])
y_2s = ("{0:0>8}").format(bin(y & int("1"*8, 2))[2:])
t_str = str(t)+'n'
t_1_str = str(t+0.1)+'n'

with open("Param_Inputs_Delay.txt",'w') as f:
	#for x input----
	for i in range(8):
		bit = "{VDD}" if x_2s[i]==str(1) else "0"
		f.write("v"+str(i+2)+" x"+str(7-i)+" gnd PWL(0 0 "+t_str+" 0 "+t_1_str+" "+bit+" 3n "+bit+")\n")
	for i in range(8):
		bit = "{VDD}" if y_2s[i]==str(1) else "0"
		f.write("v"+str(i+10)+" y"+str(7-i)+" gnd PWL(0 0 "+t_str+" 0 "+t_1_str+" "+bit+" 3n "+bit+")\n")
print("Text File Updated!!")

