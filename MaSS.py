# Login Systems
def logIn():
	print("======================== Ver 0.0.1 ==========================")
	print("================= Module and Student System =================")
	print("======================= Login Page ==========================\n")
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	if password == "TEST":
		loggedIn = True
		print("Logged in successfully")
		return loggedIn
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
		print("========== Student Main Page, FULLNAME, USR TYPE ============\n")
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
					print("Password: ", "Test")
					print("\n7. Main Menu")
				elif locationSelect == 2:
					print("======================== Ver 0.0.1 ==========================")
					print("================= Module and Student System =================")
					print("============= Module Page, FULLNAME, USR TYPE ===============\n")
					print("Available Modules - \n", "Module List")
					print("\n7. Main Menu")


console(False)
# GitHub test 2
