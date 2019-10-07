#Buildatm/ussdapp
#ADD dictionary that holds name and account numbers----- use a for loop to loop through for transfers

pin = int(input("enter your pin: "))
def atm():
	kayode_acc = 0
	Balance = 10000
	if pin == 1234:
		print("Pin ok!")	
		task = input("withdrawal = 'w', transfer = 't' or deposit = 'd': ").lower()
		while True:
	 		if task == 'w' or 't' or 'd':
	 			if task == 'w':
	 				amount = int(input("Enter amount for withdrawal: "))
	 				if amount%5 == 0:
	 					if Balance >= amount:
	 						Balance = Balance - amount
	 						print("Successful! Please take your cash.\nYour account Balance is ", Balance,'naira' )
	 					else:
	 						print('Insufficient Funds! Ole! Please deposit money')
	 				else:
	 					print("Cannot dispense that amount... Enter amount divisible by 5")

	 			elif task == 't':
	 				amount = int(input("Enter amount for transfer: "))
	 				if Balance >= Bamount:
	 					Balance = Balance - amount
	 					trans = input("Enter beneficiary's first name: ")
	 					if trans == 'kayode':
	 						kayode_acc = kayode_acc + amount
	 						print("Transfer Successful!. Your account Balance is ", Balance,'naira', "\nKayode's account balance is ", kayode_acc, 'naira')
	 				else:
	 						print('Insufficient Funds! Ole! Please deposit money')
	 					
	 			elif task == 'd':
	 				amount = int(input("Enter amount for deposit:"))
	 				Balance = Balance + amount
	 				print("Cash Deposited! Your account balance is ", Balance, 'naira' )

		 	end = input("would you like to perform any other transactions? enter 'yes'  or 'no':")
				if end == 'y':
				task = input("withdrawal = 'w', transfer = 't', deposit = 'd'or enter 'b for balance: ").lower()
			elif task == 'b':
				print(Balance)

				else:
	 				print("Thank you for Banking with us.\nGoodbye!")

	 			

		


			 	




	else:
		print ("Incorrect pin,Try again")





atm()



