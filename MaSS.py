import csv

# variable init
global username
global password
global firstName
global secondName
global accountType
global accountStatus
global rowPlace

password = ""
username = ""
firstName = ""
secondName = ""
accountType = ""
accountStatus = ""
rowPlace = 0

# CSV rows and fields
userFields = []
userRows = []

moduleFields = []
moduleRows = []

userModuleFields = []
userModuleRows = []
myModules = []

# csv readers
userFile = open("User.csv", 'r')
userReader = csv.reader(userFile)
userFields = next(userReader)
for userRow in userReader:
	userRows.append(userRow)

moduleFile = open("Module.csv", 'r')
moduleReader = csv.reader(moduleFile)
moduleFields = next(moduleReader)
for moduleRow in moduleReader:
	moduleRows.append(moduleRow)

userModules = open("UserModule.csv", 'r')
userModuleReader = csv.reader(userModules)
userModuleFields = next(userModuleReader)
for userModuleRow in userModuleReader:
	userModuleRows.append(userModuleRow)


# Login Systems
def logIn():
	print("======================== Ver 0.0.1 ==========================")
	print("================= Module and Student System =================")
	print("======================= Login Page ==========================\n")
	global username
	global password
	global firstName
	global secondName
	global accountType
	global accountStatus
	global rowPlace

	username = input("Enter your username: ")
	password = input("Enter your password: ")
	for i in range(len(userRows)):
		if userRows[i][0] == username and userRows[i][1] == password:
			username = userRows[i][0]
			password = userRows[i][1]
			firstName = userRows[i][2]
			secondName = userRows[i][3]
			accountType = userRows[i][4]
			accountStatus = userRows[i][5]
			rowPlace = i

			if accountStatus == "Blocked":
				print("Account is blocked! Please contact a lecturer.")
				logIn()
			loggedIn = True
			print("Logged in successfully")
			return loggedIn
	else:
		print("Incorrect Username or Password!")
		logIn()


def fileChange(editedfile, fileread):
	with open(editedfile, 'w', newline='') as filewritten:
		writer = csv.writer(filewritten)
		writer.writerows(fileread)


# Main application condensed to a function to allow recursion (logging in and out within program)
def console(loggedIn):
	locationSelect = int(0)
	global username
	global password
	global firstName
	global secondName
	global accountType
	global accountStatus
	global rowPlace

	while not loggedIn:

		loggedIn = logIn()
		loggedIn = True

	else:
		# student main page
		print("======================== Ver 0.0.4 ==========================")
		print("================= Module and Student System =================")
		print("============ Main Page,", firstName, secondName, ",", accountType, "============\n")
		print("1. View User Profile\n"
			  "2. View All Modules\n"
			  "3. Change Password\n"
			  "4. My Modules\n"
			  "5. Withdraw From a Module\n"
			  "6. Apply to a Module\n"
			  "10. Exit")
		while loggedIn:
			# Student Pages
			if (locationSelect == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 10) and accountType == "Student":
				locationSelect = int(input("\nWhere would you like to go?: "))
				for x in range(len(userModuleRows)):
					if username == userModuleRows[x][0]:
						module = userModuleRows[x][1]
						for y in range(len(moduleRows)):
							if module == moduleRows[y][0]:
								myModules.append(moduleRows[y][1])
				if locationSelect == 7:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Main Page,", firstName, secondName + ",", accountType, "============\n")
					print("1. View User Profile\n"
						  "2. View All Modules\n"
						  "3. Change Password\n"
						  "4. My Modules\n"
						  "5. Withdraw From a Module\n"
						  "6. Apply to a Module\n"
						  "10. Exit")
				elif locationSelect == 10:
					console(False)
				elif locationSelect == 1:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ User Page,", firstName, secondName + ",", accountType, "============\n")
					print("First Name: ", firstName)
					print("Second Name: ", secondName)
					print("User Type: ", accountType)
					print("Username: ", username)
					print("Password: ", password)
					print("\n7. Main Menu")

				elif locationSelect == 2:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Module Page,", firstName, secondName + ",", accountType, "============\n")
					print("Available Modules - \n")
					for i in range(len(moduleRows)):
						print(moduleRows[i][1], "\n")

					print("\n7. Main Menu")
				elif locationSelect == 3:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Change Password Page,", firstName, secondName + ",", accountType, "=======\n")
					print("Username: ", username)
					print("Password: ", password)
					passChange = input("Would you like to change your password? (Y/N)")
					if passChange == "N":
						print("Exiting...")
						print("1. View User Profile\n"
							  "2. View All Modules\n"
							  "3. Change Password\n"
							  "4. My Modules\n"
							  "5. Withdraw From a Module\n"
							  "6. Apply to a Module\n"
							  "10. Exit")
					if passChange == "Y":
						passUnchanged = 1
						while passUnchanged == 1:
							print("Current Password: ", password)
							print("\n", "=============================", "\n")
							newPassword = input("New Password: ")
							newPasswordCheck = input("Re-enter New Password: ")
							if newPasswordCheck == newPassword:
								userRows[rowPlace][1] = newPassword
								fileChange('user.csv', userRows)
								print("1. View User Profile\n"
									  "2. View All Modules\n"
									  "3. Change Password\n"
									  "4. My Modules\n"
									  "5. Withdraw From a Module\n"
									  "6. Apply to a Module\n"
									  "10. Exit")
								break



				elif locationSelect == 4:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= My Modules Page,", firstName, secondName + ",", accountType, "=======\n")
					print("My Modules -")
					for x in range(len(userModuleRows)):
						if username == userModuleRows[x][0]:
							module = userModuleRows[x][1]
							for y in range(len(moduleRows)):
								if module == moduleRows[y][0]:
									print(moduleRows[y][1])
					print("\n7. Main Menu")
				elif locationSelect == 5:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Withdraw Modules Page,", firstName, secondName + ",", accountType, "=======\n")
				elif locationSelect == 6:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("==== Apply to Modules Page,", firstName, secondName + ",", accountType, "====\n")

			# Lecturer Pages
			elif (locationSelect == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 10) and accountType == "Lecturer":
				locationSelect = int(input("\nWhere would you like to go?: "))
				if locationSelect == 7:
					print("======================== ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Main Page,", firstName, secondName + ",", accountType, "============\n")
					print("1. View User Profile\n"
						  "2. View All Modules\n"
						  "3. Change Password\n"
						  "10. Exit")
				elif locationSelect == 10:
					console(False)
				elif locationSelect == 1:
					print("======================== ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ User Page,", firstName, secondName + ",", accountType, "============\n")
					print("First Name: ", firstName)
					print("Second Name: ", secondName)
					print("User Type: ", accountType)
					print("Username: ", username)
					print("Password: ", password)
					print("\n7. Main Menu")
				elif locationSelect == 2:
					print("======================== ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Module Page,", firstName, secondName + ",", accountType, "============\n")
					print("Available Modules - \n")
					for i in range(len(moduleRows)):
						print(moduleRows[i][1], "\n")

					print("\n7. Main Menu")
				elif locationSelect == 3:
					print("======================== ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Change Password Page,", firstName, secondName + ",", accountType, "=======\n")


console(False)
