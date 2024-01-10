while True:
	num = int (input("\n\tEnter first number: "))
	num2 = int(input("\tEnter second number: "))
	op = str (input("\tEnter an operator [exit]: "))
	if op == "exit":
		break

	if op == "+":
		print( "\n", num, " + ", num2, " = ", num+num2)
	elif op == "-":
		print("\n", num, " - ", num2, " = ", num-num2)
	elif op == "/":
		print("\n", num, " / ", num2, " = ", num/num2)
	elif op == "*":
		print("\n", num, " * ", num2, " = ", num*num2)
	else:
		print("Lol")