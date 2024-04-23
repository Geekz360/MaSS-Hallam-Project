import csv
from prompt_toolkit import prompt

# variable init
global username
global password
global firstName
global secondName
global accountType
global accountStatus
global rowPlace
global verNumber

password = ""
username = ""
firstName = ""
secondName = ""
accountType = ""
accountStatus = ""
rowPlace = 0
verNumber = "======================== Ver 1.0.1 =========================="

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
	print(verNumber)
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
	password = prompt("Enter your password: ", is_password=True)
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


# User menu functions. I have made these as I was repeatedly copying and pasting code snippets
def userMenu():
	global username
	global password
	global firstName
	global secondName
	global accountType
	global accountStatus
	global rowPlace
	global verNumber

	print(verNumber)
	print("================= Module and Student System =================")
	print("============ User Page,", firstName, secondName + ",", accountType, "============\n")
	password = userRows[rowPlace][1]
	print("First Name: ", firstName)
	print("Second Name: ", secondName)
	print("User Type: ", accountType)
	print("Username: ", username)
	print("Password: ", password)

	locationSelect = input("Press return to exit to main menu. ")


def availableModules():
	global firstName
	global secondName
	global accountType
	print(verNumber)
	print("================= Module and Student System =================")
	print("============ Module Page,", firstName, secondName + ",", accountType, "============\n")
	print("Available Modules - \n")
	for i in range(len(moduleRows)):
		print(moduleRows[i][1], "\n")

	locationSelect = input("Press return to exit to main menu. ")


def changePassword():
	global username
	global password

	print(verNumber)
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

	if passChange == "Y":
		passUnchanged = 1
		# Change user passwords, this will enable the user to enter a new password, check it then finalise it.
		while passUnchanged == 1:
			print("\n", "=============================", "\n")
			oldPassword = prompt("Enter your OLD password: ", is_password=True)
			if oldPassword == password:
				newPassword = prompt("New Password: ", is_password=True)
				newPasswordCheck = prompt("Re-enter New Password: ", is_password=True)
				if newPasswordCheck == newPassword:
					userRows[rowPlace][1] = newPassword
					fileChange('user.csv', userRows)
					break
	locationSelect = input("Press return to exit to main menu. ")


def myMods():
	print(verNumber)
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
	locationSelect = input("Press return to exit to main menu. ")


def leaveModules():
	print(verNumber)
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
		print("\nExiting...")
	locationSelect = input("Press return to exit to main menu. ")


def applyModules():
	print(verNumber)
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
		print("\nExiting...")
	locationSelect = input("Press return to exit to main menu. ")


def createModules():
	print(verNumber)
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
		locationSelect = input("Press return to exit to main menu. ")


def editStudent():
	print(verNumber)
	print("================= Module and Student System =================")
	print("======= Edit Student Page,", firstName, secondName + ",", accountType, "=======\n")
	print("Students -")
	for p in range(len(userRows)):
		if userRows[p][4] == "Student":
			print(userRows[p][2], userRows[p][3])

	confirmStuEdit = input("Would you like to edit a student profile? (Y/N): ").upper()
	if confirmStuEdit == "N":
		print("\n7. Main Menu")
	if confirmStuEdit == "Y":
		studentFirstName = input("Enter the students FIRST name: ").upper()
		studentSecondName = input("Enter the students SECOND name: ").upper()
		for r in range(len(userRows)):
			if studentFirstName == userRows[r][2].upper() and studentSecondName == userRows[r][3].upper():
				stuUser = userRows[r][0]
				stuPass = userRows[r][1]
				stuFirstName = userRows[r][2]
				stuSecondName = userRows[r][3]
				stuStatus = userRows[r][5]

				print("Student Details - "
					  "\n1. Name - ", stuFirstName, stuSecondName,
					  "\n2. Username - ", stuUser,
					  "\n3. Password - ", stuPass,
					  "\n4. Status - ", stuStatus)
				studentEditSelect = int(input("What would you like to edit?: "))
				if studentEditSelect == 1:
					newFirstName = input("Enter new first name: ")
					newSecondName = input("Enter new second name: ")
					userRows[r][2] = newFirstName
					userRows[r][3] = newSecondName
					fileChange('User.csv', userRows)

				elif studentEditSelect == 2:
					newUser = input("Enter new username: ")
					userRows[r][0] = newUser
					fileChange('User.csv', userRows)

				elif studentEditSelect == 3:
					print("Password has been reset to - %Pa55w0rd")
					userRows[r][1] = "%Pa55w0rd"
					fileChange('User.csv', userRows)

				elif studentEditSelect == 4:
					if stuStatus == "Active":
						userRows[r][5] = "Blocked"
						print(stuUser, "- account has been blocked")
					elif stuStatus == "Blocked":
						userRows[r][5] = "Active"
						print(stuUser, "- account has been unblocked")

	locationSelect = input("Press return to exit to main menu. ")


# Main application condensed to a function to allow recursion (logging in and out within program)
def console(loggedIn):
	locationSelect = ""
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
			if (locationSelect == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "10") and accountType == "Student":
				print(verNumber)
				print("================= Module and Student System =================")
				print("============ Main Page,", firstName, secondName, ",", accountType, "============\n")
				print("1. View User Profile\n"
					  "2. View All Modules\n"
					  "3. Change Password\n"
					  "4. My Modules\n"
					  "5. Withdraw From a Module\n"
					  "6. Apply to a Module\n"
					  "10. Exit")
				locationSelect = input("\nWhere would you like to go?: ")
				'''The following block will re-read the user module files,to ensure that they are consistently 
				updated throughout'''
				for x in range(len(userModuleRows)):
					if username == userModuleRows[x][0]:
						module = userModuleRows[x][1]
						for y in range(len(moduleRows)):
							if module == moduleRows[y][0]:
								myModules.append(moduleRows[y][1])
				if locationSelect == "7":
					locationSelect = input("You are already on the main menu. Press return to continue.")
				elif locationSelect == "10":
					console(False)
				elif locationSelect == "1":
					userMenu()

				elif locationSelect == "2":
					availableModules()

				elif locationSelect == "3":
					changePassword()

				elif locationSelect == "4":
					myMods()

				elif locationSelect == "5":
					leaveModules()

				elif locationSelect == "6":
					applyModules()

			# Lecturer Pages
			elif (locationSelect == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "10") and accountType == "Lecturer":
				print(verNumber)
				print("================= Module and Student System =================")
				print("============ Main Page,", firstName, secondName + ",", accountType, "============\n")
				print("1. View User Profile\n"
					  "2. View All Modules\n"
					  "3. Change Password\n"
					  "4. My Modules\n"
					  "5. Create a Module\n"
					  "6. Edit a Student\n"
					  "10. Exit")
				locationSelect = input("\nWhere would you like to go?: ")
				if locationSelect == "7":
					locationSelect = input("You are already on the main menu. Press return to continue.")
				elif locationSelect == "10":
					console(False)
				elif locationSelect == "1":
					userMenu()
				elif locationSelect == "2":
					availableModules()

				elif locationSelect == "3":
					changePassword()

				elif locationSelect == "4":
					myMods()

				elif locationSelect == "5":
					createModules()

				elif locationSelect == "6":
					editStudent()


console(False)
