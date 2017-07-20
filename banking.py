friends_account = {
	
	'Ross': {'Name': 'Ross', 'ID': 1234567890, 'Checking': 4009.98, 'Savings': 2334.90},
	'Chandler': {'Name': 'Chandler', 'ID': 1223456789, 'Checking': 5678.98, 'Savings': 87.90},
	'Joey': {'Name': 'Joey', 'ID': 1029384756, 'Checking': .98, 'Savings': 599.87},
	'Monica': {'Name': 'Monica', 'ID': 1111111111, 'Checking': 657.11, 'Savings': 3134.43},
	'Rachel': {'Name': 'Rachel', 'ID': 2345678900, 'Checking': 45.98, 'Savings': 1000.21},
	'Phoebe': {'Name': 'Phoebe', 'ID': 2098766543, 'Checking': 100.22, 'Savings': 23.90},

}

if __name__ == "__main__":

	score = 0

	input_path = raw_input("Ross wants you to update his savings account balance c500 \n")
	input_path = input_path.replace(" ","")
	if(input_path != "Ross['Savings']=500"):
		print ('Incorrect update to account')
	else:
		print ('Account Updated \n')
		score += 1
		print ('Your score is: ' + str(score) + '/1 \n')

	input_path = raw_input("Joey wants you to update his checking account balance to 600 \n")
	input_path = input_path.replace(" ","")
	if(input_path != "Joey['Checking']=600"):
		print ('Incorrect update to account')
	else:
		print ('Account Updated \n')
		score += 1
		print ('Your score is: ' + str(score) + '/2 \n')

	input_path = raw_input("Chandler wants you to update Monica's name to 'Mon' \n")
	input_path = input_path.replace(" ","")
	if(input_path != "Monica['Name']='Mon'"):
		print ('Incorrect update to account')
	else:
		print ('Account Updated \n')
		score += 1
		print ('Your score is: ' + str(score) + '/' + '3 \n')
		
	input_path = raw_input("Phoebe wants you to update Rachel's savings account balance to 0 \n")
	input_path = input_path.replace(" ","")
	if(input_path != "Rachel['Savings']=0"):
		print ('Incorrect update to account')
	else:
		print ('Account Updated \n')
		score += 1
		print ('Your score is: ' + str(score) + '/' + '4 \n')

	input_path = raw_input("Phoebe wants you to update her ID 1312466070 \n")
	input_path = input_path.replace(" ","")
	if(input_path != "Phoebe['ID']=1312466070"):
		print ('Incorrect update to account')
	else:
		print ('Account Updated \n')
		score += 1
		print ('Your score is: ' + str(score) + '/' + '5 \n')

	
	


