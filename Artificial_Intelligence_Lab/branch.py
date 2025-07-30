choice1=input("Enter a first choice when student is selected :")
choice2=input("Enter a second choice when student is selected :")

if((choice1=="math" and choice2=="physics") or (choice1=="physics" and choice2=="math")):
	print("Mechanical engineering")

elif((choice1=="programming" and choice2=="math") or (choice1=="math" and choice2=="programming")):
	print("Comouter engineering")
	
elif((choice1=="physics" and choice2=="chemistry") or (choice1=="chemistry" and choice2=="physics")):
	print(" engineering science")		

elif((choice1=="biology" and choice2=="chemistry") or (choice1=="chemistry" and choice2=="biology")):
	print("Biotechnology")
	
elif((choice1=="circuit" and choice2=="math") or (choice1=="math" and choice2=="circuit")):
	print("Electronics Engineering")
	
elif((choice1=="programming" and choice2=="statistic") or (choice1=="statistic" and choice2=="programming")):
	print("Artificial intelligence and Data science engineering")

elif((choice1=="programming" and choice2=="AI concept") or (choice1=="AI concept" and choice2=="programming")):
	print("Artificial intelligence and Machine Learning engineering")

else:
	print("NO engineering")
