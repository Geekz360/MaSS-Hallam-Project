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
# userFields = next(userReader) -- DISABLED DUE TO BREAKING CHANGING CSV
for userRow in userReader:
	userRows.append(userRow)

moduleFile = open("Module.csv", 'r')
moduleReader = csv.reader(moduleFile)
# moduleFields = next(moduleReader) -- DISABLED DUE TO BREAKING CHANGING CSV
for moduleRow in moduleReader:
	moduleRows.append(moduleRow)

userModules = open("UserModule.csv", 'r')
userModuleReader = csv.reader(userModules)
# userModuleFields = next(userModuleReader) -- DISABLED DUE TO BREAKING CHANGING CSV
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
	# Go through the userRows function (User CSV) and check if they are applicable for a log in
	for i in range(len(userRows)):

		if userRows[i][0] == username and userRows[i][1] == password:
			username = userRows[i][0]
			password = userRows[i][1]
			firstName = userRows[i][2]
			secondName = userRows[i][3]
			accountType = userRows[i][4]
			accountStatus = userRows[i][5]
			rowPlace = i

			# Ensure an account cant log in if they're blocked
			if accountStatus == "Blocked":
				print("Account is blocked! Please contact a lecturer.")
				logIn()
			loggedIn = True
			print("Logged in successfully")
			return loggedIn
		# Stop the user inputting Username and Password as log in information
		elif username == "Username":
			print("Nice Try ^_^")

		elif i + 2 > len(userRows):
			print("Incorrect Username or Password")


# Initialise my function to write over the CSV files to be able to update information
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
		if loggedIn:
			console(True)

	else:
		while loggedIn:
			# Student Pages
			if (locationSelect == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 10) and accountType == "Student":
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
				locationSelect = int(input("\nWhere would you like to go?: "))
				'''The following block will re-read the user module files,to ensure that they are consistently updated throughout'''
				for x in range(len(userModuleRows)):
					if username == userModuleRows[x][0]:
						module = userModuleRows[x][1]
						for y in range(len(moduleRows)):
							if module == moduleRows[y][0]:
								myModules.append(moduleRows[y][1])
				if locationSelect == 7:
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 10:
					console(False)
				elif locationSelect == 1:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ User Page,", firstName, secondName + ",", accountType, "============\n")
					password = userRows[rowPlace][1]
					print("First Name: ", firstName)
					print("Second Name: ", secondName)
					print("User Type: ", accountType)
					print("Username: ", username)
					print("Password: ", password)
					print("\n7. Main Menu")

					locationSelect = input("Where would you like to go?: ")

				elif locationSelect == 2:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Module Page,", firstName, secondName + ",", accountType, "============\n")
					print("Available Modules - \n")
					for i in range(len(moduleRows)):
						print(moduleRows[i][1], "\n")

					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 3:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Change Password Page,", firstName, secondName + ",", accountType, "=======\n")
					print("Username: ", username)
					for l in range(len(userRows)):
						if username == userRows[l][0]:
							password = userRows[l][1]

					print("Password: ", password)
					passChange = input("Would you like to change your password? (Y/N)")
					if passChange == "N":
						print("Exiting...")
						break
					if passChange == "Y":
						passUnchanged = 1
						# Change user passwords, this will enable the user to enter a new password, check it then finalise it.
						while passUnchanged == 1:
							print("\n", "=============================", "\n")
							oldPassword = input("Enter your OLD password: ")
							if oldPassword == password:
								newPassword = input("New Password: ")
								newPasswordCheck = input("Re-enter New Password: ")
								if newPasswordCheck == newPassword:
									userRows[rowPlace][1] = newPassword
									fileChange('user.csv', userRows)
									break
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 4:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= My Modules Page,", firstName, secondName + ",", accountType, "=======\n")
					print("My Modules -")
					# Present the user with their enrolled modules
					for x in range(len(userModuleRows)):
						if username == userModuleRows[x][0]:
							module = userModuleRows[x][1]
							for y in range(len(moduleRows)):
								if module == moduleRows[y][0]:
									print(moduleRows[y][1])
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 5:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Withdraw Modules Page,", firstName, secondName + ",", accountType, "=======\n")
					print("My Modules - ")
					# Allow a user to leave a module
					for x in range(len(userModuleRows)):
						if username == userModuleRows[x][0]:
							module = userModuleRows[x][1]
							for y in range(len(moduleRows)):
								if module == moduleRows[y][0]:
									print(moduleRows[y][0], " - ", moduleRows[y][1], "\n")

					moduleLeave = input("Would you like to withdraw from a module? (Y/N)").upper()
					if moduleLeave == "Y":
						moduleLeaveSelect = input("Enter the module ID you would like to leave: ")
						for p in range(len(userModuleRows)):
							if moduleLeaveSelect == userModuleRows[p][1]:
								del userModuleRows[p]
								fileChange('UserModule.csv', userModuleRows)
								break
					elif moduleLeave == "N":
						break
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")

				elif locationSelect == 6:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("==== Apply to Modules Page,", firstName, secondName + ",", accountType, "====\n")
					print("My Modules -")
					# Allow a user to apply to a module
					for x in range(len(userModuleRows)):
						if username == userModuleRows[x][0]:
							module = userModuleRows[x][1]
							for y in range(len(moduleRows)):
								if module == moduleRows[y][0]:
									print(moduleRows[y][0], " - ", moduleRows[y][1], "\n")

					print("Available Modules - ")
					for i in range(len(moduleRows)):
						print(moduleRows[i][0], " - ", moduleRows[i][1], "\n")

					moduleAdd = input("Would you like to apply for a module? (Y/N) ").upper()
					if moduleAdd == "Y":
						moduleAddSelect = str(input("Enter the Module ID you wish to apply for: "))
						for f in range(len(moduleRows)):
							if moduleAddSelect == moduleRows[f][0]:
								userModuleRows.append([username, moduleAddSelect])
								fileChange('UserModule.csv', userModuleRows)
								break
					elif moduleAdd == "N":
						break
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")

			# Lecturer Pages
			elif (locationSelect == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 10) and accountType == "Lecturer":
				print("======================== Ver 0.0.4 ==========================")
				print("================= Module and Student System =================")
				print("============ Main Page,", firstName, secondName + ",", accountType, "============\n")
				print("1. View User Profile\n"
					  "2. View All Modules\n"
					  "3. Change Password\n"
					  "4. My Modules\n"
					  "5. Create a Module\n"
					  "10. Exit")
				locationSelect = int(input("\nWhere would you like to go?: "))
				if locationSelect == 7:
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 10:
					console(False)
				elif locationSelect == 1:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ User Page,", firstName, secondName + ",", accountType, "============\n")
					password = userRows[rowPlace][1]
					print("First Name: ", firstName)
					print("Second Name: ", secondName)
					print("User Type: ", accountType)
					print("Username: ", username)
					print("Password: ", password)
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 2:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("============ Module Page,", firstName, secondName + ",", accountType, "============\n")
					print("Available Modules - \n")
					for i in range(len(moduleRows)):
						print(moduleRows[i][1], "\n")

					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 3:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Change Password Page,", firstName, secondName + ",", accountType, "=======\n")
					print("Username: ", username)
					for l in range(len(userRows)):
						if username == userRows[l][0]:
							password = userRows[l][1]

					print("Password: ", password)
					passChange = input("Would you like to change your password? (Y/N)")
					if passChange == "N":
						print("Exiting...")
						print("\n7. Main Menu")
						locationSelect = input("Where would you like to go?: ")
					if passChange == "Y":
						passUnchanged = 1
						# Change user passwords, this will enable the user to enter a new password, check it then finalise it.
						while passUnchanged == 1:
							print("\n", "=============================", "\n")
							oldPassword = input("Enter your OLD password: ")
							if oldPassword == password:
								newPassword = input("New Password: ")
								newPasswordCheck = input("Re-enter New Password: ")
								if newPasswordCheck == newPassword:
									userRows[rowPlace][1] = newPassword
									fileChange('user.csv', userRows)
									break
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")

				elif locationSelect == 4:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= My Modules Page,", firstName, secondName + ",", accountType, "=======\n")
					print("My Modules -")
					# Present the user with their enrolled modules
					for x in range(len(userModuleRows)):
						if username == userModuleRows[x][0]:
							module = userModuleRows[x][1]
							for y in range(len(moduleRows)):
								if module == moduleRows[y][0]:
									print(moduleRows[y][1])
					print("\n7. Main Menu")
					locationSelect = input("Where would you like to go?: ")
				elif locationSelect == 5:
					print("======================== Ver 0.0.4 ==========================")
					print("================= Module and Student System =================")
					print("======= Create Modules Page,", firstName, secondName + ",", accountType, "=======\n")
					print("Modules - ")
					# Allow a lecturer to create modules
					print("Module ID - Module Name")
					for x in range(len(moduleRows)):
						print(moduleRows[x][0], " - ", moduleRows[x][1])

					moduleCreate = input("Would you like to create a module? (Y/N)").upper()
					if moduleCreate == "Y":
						moduleCreateID = input("Enter the new module ID: ")
						moduleCreateName = input("Enter the new module name: ")
						moduleRows.append([moduleCreateID, moduleCreateName])
						fileChange('Module.csv', moduleRows)
					elif moduleCreate == "N":
						print("\n7. Main Menu")
						locationSelect = input("Where would you like to go?: ")








console(False)
