# CYB333 Security Automation Class Project
# Create a python tool to automate security related functions
# Automating Access

#First we need to import the libary Pandas and we are importing it "as pd" so we do not need to type out pandas each time we use it
import pandas as pd

#We are going to set our CSV to a variable PrivUsers short for Priveleged Users using pandas to read in our csv
PrivUsers = pd.read_csv('CYB333List.csv')

#We then want to read PrivUsers as a list so that it is clean and easier to work with
PrivUsers.columns.tolist()

#Set that list to a new variable ElevAccess so now we have our cleaned up version of the CSV set to our Elevated Access variable
ElevAccess = PrivUsers.columns.tolist()


#We then want to write an if statement to read our new variable ElevAccess and grant access to anyone who is listed in the list that we created earlier in the CSV,
#Anyone that is not in the list will not have access. This code will automate checking the list for proper authorization
username = "Leah"

if username in ElevAccess:

    print("You have Access")

else:

    print("User Access Denied")

