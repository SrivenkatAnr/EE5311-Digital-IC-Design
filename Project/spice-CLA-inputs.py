x = int(input("Enter the augend value: "))
y = int(input("Enter the addend Value: "))

if x<0 or x>15 or y<0 or y>15:
	raise ValueError("Please enter valid inputs for a 4 bit adder!!")
x_bin = ("{0:0>4}").format(bin(x)[2:])
y_bin = ("{0:0>4}").format(bin(y)[2:])

with open("Project_Param_CLA.txt",'w') as f:
	#for x input----
	for i in range(4):
		bit = "{VDD}" if x_bin[i]==str(1) else "0"
		f.write("v"+str(i+3)+" A["+str(3-i)+"] gnd DC "+bit+"\n")
	for i in range(4):
		bit = "{VDD}" if y_bin[i]==str(1) else "0"
		f.write("v"+str(i+7)+" B["+str(3-i)+"] gnd DC "+bit+"\n")
print("Text File Updated!!")

