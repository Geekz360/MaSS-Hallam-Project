import csv

# variable init
password = ""
username = ""

# CSV rows and fields
userFields = []
userRows = []

moduleFields = []
moduleRows = []

userModuleFields = []
userModuleRows = []

# csv readers
userFile = open("User.csv", 'r')
userReader = csv.reader(userFile)
userFields = next(userReader)
for userRow in userReader:
	userRows.append(userRow)

with open("Module.csv", 'r') as moduleFile:
	moduleReader = csv.reader(moduleFile)
	moduleFields = next(moduleReader)
	for moduleRow in moduleReader:
		moduleRows.append(moduleRow)

with open("UserModule.csv", 'r') as userModules:
	userModuleReader = csv.reader(userModules)
	userModuleFields = next(userModuleReader)
	for userModuleRow in userModuleReader:
		userModuleRows.append(userModuleRow)


# Login Systems
def logIn():
	print("======================== Ver 0.0.1 ==========================")
	print("================= Module and Student System =================")
	print("======================= Login Page ==========================\n")
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	for i in range(len(userRows)):
		if userRows[i][0] == username and userRows[i][1] == password:
			print(userRows[i][0], userRows[i][1], userRows[i][2], userRows[i][3], userRows[i][4], userRows[i][5])
			loggedIn = True
			print("Logged in successfully")
			return loggedIn and password and username
	else:
		print("Incorrect Username or Password!")
		logIn()


# Main application condensed to a function to allow recursion (logging in and out within program)
def console(loggedIn):
	locationSelect = int(0)
	while not loggedIn:

		loggedIn = logIn()

	else:
		# student main page
		print("======================== Ver 0.0.1 ==========================")
		print("================= Module and Student System =================")
		print("========== Student Main Page", username, "USR TYPE ============\n")
		print("1. View User Profile\n"
			  "2. View All Modules\n"
			  "3. Change Password\n"
			  "10. Exit")
		while loggedIn:
			while locationSelect == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 10:
				locationSelect = int(input("\nWhere would you like to go?: "))
				if locationSelect == 7:
					print("======================== Ver 0.0.1 ==========================")
					print("================= Module and Student System =================")
					print("========== Student Main Page, FULLNAME, USR TYPE ============\n")
					print("1. View User Profile\n"
						  "2. View All Modules\n"
						  "3. Change Password\n"
						  "10. Exit")
				elif locationSelect == 10:
					console(False)
				elif locationSelect == 1:
					print("======================== Ver 0.0.1 ==========================")
					print("================= Module and Student System =================")
					print("============== User Page, FULLNAME, USR TYPE ===============\n")
					print("First Name: ", "TEST")
					print("Second Name: ", "TESTERSON")
					print("User Type: ", "ADMIN")
					print("Username: ", "TTESTERSON")
					print("Password: ", )
					print("\n7. Main Menu")
				elif locationSelect == 2:
					print("======================== Ver 0.0.1 ==========================")
					print("================= Module and Student System =================")
					print("============= Module Page, FULLNAME, USR TYPE ===============\n")
					print("Available Modules - \n", "Module List")
					print("\n7. Main Menu")
				elif locationSelect == 3:
					print("======================== Ver 0.0.1 ==========================")
					print("================= Module and Student System =================")
					print("========= Change Password Page, FULLNAME, USR TYPE ==========\n")


console(False)
