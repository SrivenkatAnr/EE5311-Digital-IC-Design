x = int(input("Enter the augend value: "))
y = int(input("Enter the addend Value: "))

if x<0 or x>255 or y<0 or y>255:
	raise ValueError("Please enter valid inputs for a 8 bit adder!!")
x_bin = ("{0:0>8}").format(bin(x)[2:])
y_bin = ("{0:0>8}").format(bin(y)[2:])

with open("Project_Param_CLA_Cascaded.txt",'w') as f:
	#for x input----
	for i in range(8):
		bit = "{VDD}" if x_bin[i]==str(1) else "0"
		f.write("v"+str(i+3)+" A["+str(7-i)+"] gnd DC "+bit+"\n")
	for i in range(8):
		bit = "{VDD}" if y_bin[i]==str(1) else "0"
		f.write("v"+str(i+11)+" B["+str(7-i)+"] gnd DC "+bit+"\n")
print("Text File Updated!!")

