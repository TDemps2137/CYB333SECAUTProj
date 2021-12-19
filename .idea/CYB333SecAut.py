# CYB333 Security Automation Class Project
# Create a python tool to automate security related functions
# Automating Access

import pandas as pd

PrivUsers = pd.read_csv('CYB333List.csv')

PrivUsers.columns.tolist()

ElevAccess = PrivUsers.columns.tolist()

username = "Leah"

if username in ElevAccess:

    print("You have Access")

else:

    print("User Access Denied")