print("Enter 1st set of values \n")
x1 = int(input("Enter the Multiplicand value: "))
y1 = int(input("Enter the Multiplier Value: "))

print("\n Enter 2nd set of values \n")
x2 = int(input("Enter the Multiplicand value: "))
y2 = int(input("Enter the Multiplier Value: "))

if x1<-128 or x1>127 or y1<-128 or y1>127 or x2<-128 or x2>127 or y2<-128 or y2>127:
	raise ValueError("Please enter valid inputs for a 8 bit multiplier!!")

x1_2s = ("{0:0>8}").format(bin(x1 & int("1"*8, 2))[2:])
y1_2s = ("{0:0>8}").format(bin(y1 & int("1"*8, 2))[2:])

x2_2s = ("{0:0>8}").format(bin(x2 & int("1"*8, 2))[2:])
y2_2s = ("{0:0>8}").format(bin(y2 & int("1"*8, 2))[2:])


with open("A4_Param_Inputs_Pulse.txt",'w') as f:
	#for x input----
	for i in range(8):
		bit1 = "{VDD}" if x1_2s[i]==str(1) else "0"
		bit2 = "{VDD}" if x2_2s[i]==str(1) else "0"
		f.write("v"+str(i+2)+" x"+str(7-i)+" gnd PWL (0 0 {10p+2*Tc} 0 {20p+2*Tc} "+bit1+" {10p+3*Tc} "+bit1+" {20p+3*Tc} "+bit2+" 3n "+bit2+")"+"\n")
	for i in range(8):
		bit1 = "{VDD}" if y1_2s[i]==str(1) else "0"
		bit2 = "{VDD}" if y2_2s[i]==str(1) else "0"
		f.write("v"+str(i+10)+" y"+str(7-i)+" gnd PWL (0 0 {10p+2*Tc} 0 {20p+2*Tc} "+bit1+" {10p+3*Tc} "+bit1+" {20p+3*Tc} "+bit2+" 3n "+bit2+")"+"\n")
print("Text File Updated!!")

