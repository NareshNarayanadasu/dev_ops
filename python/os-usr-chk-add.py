'''#!/usr/bin/python3
import os 
usr_list =[ "naresh", "narendra"]
print ( "adding users to system ")
print("############################################")
for usr in usr_list:
    exitcode = os.system("id {}".format(usr))
    if  exitcode != 0:
        print ("user {} is not existed in this system ".format(usr))
        print("adding user to this system")
        print("####################################")
        sleep(5)
        os.system("sudo useradd {}".format(usr))
    else:
        print("user {} is already exist".foram(usr))
        print("continue you'r work")
    
f
'''
"""
#!/usr/bin/python3
import os
import subprocess
from time import sleep

usr_list = ["naresh", "narendra"]
print("Adding users to system")
print("############################################")

for usr in usr_list:
    try:
        # Check if user exists
        result = subprocess.run(["id", usr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exitcode = result.returncode
        
        if exitcode != 0:
            print(f"User {usr} does not exist in this system")
            print("Adding user to this system")
            print("####################################")
            sleep(5)
            os.system(f"sudo useradd {usr}")
        else:
            print(f"User {usr} already exists")
            print("Continue your work")
    except Exception as e:
        print(f"An error occurred: {e}")

"""