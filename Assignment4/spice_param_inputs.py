def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = bin(val) - (1 << bits)        # compute negative value
    return str(bin(val))  


x = int(input("Enter the Multiplicand value: "))
y = int(input("Enter the Multiplier Value: "))

if x<-128 or x>127 or y<-128 or y>127:
	raise ValueError("Please enter valid inputs for a 8 bit multiplier!!")
x_2s = ("{0:0>8}").format(bin(x & int("1"*8, 2))[2:])
y_2s = ("{0:0>8}").format(bin(y & int("1"*8, 2))[2:])


with open("A4_Param_Inputs.txt",'w') as f:
	#for x input----
	for i in range(8):
		bit = "{VDD}" if x_2s[i]==str(1) else "0"
		f.write("v"+str(i+2)+" x"+str(7-i)+" gnd DC "+bit+"\n")
	for i in range(8):
		bit = "{VDD}" if y_2s[i]==str(1) else "0"
		f.write("v"+str(i+10)+" y"+str(7-i)+" gnd DC "+bit+"\n")
print("Text File Updated!!")

