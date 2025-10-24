#!/usr/bin/python3

# INET4031
# Name: Johnny Tu
# Data Created: 2024-11-19
# Date Modified: 2025-10-24

#import os is for access to modify the operating system, it is used to add users in this case
#import re is used to search for patterns within a string and modifying parts of a string
#import sys is used to access system specific parameters and functions such as the "<" to input from a file.
import os
import re
import sys

def main():
    for line in sys.stdin:

	#This line looks for a line to start with "#", the match variable is later used to see if a line is commented out
	#and should not be ran. 
        match = re.match("^#",line)

        #This line splits up the input file and strips and splits the list by first removing the whitespace if it exists, 
	#then splitting it up into a list if a ":" exists. 
        fields = line.strip().split(':')

        #The if statement below checks if match is true or if length of fields is not equal to 5. Both of the variables
	#were defined earlier above, if both either of them are true, the if statement is true and it will skip past the rest of the for loop that it is in
	#it checks for if match is true and if length of fields is not equal to 5 because, if so we want to skip the line as it does not fufill the requirements
	#to be ran.
	if match or len(fields) != 5:
            continue

        #the username line assigns username with the first item inside fields which is the username.
	#the password line assigns password with the second item inside fields which is the password.
	#the gecos line assigns the full name with the third and fourth item along with ",,," for the defaults of room number, work phone, and home phone.
        #the lines relate to what is in the passwd file as each item corrolates with how a passwd file is formatted with username:password:lastname:firstname
	username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

	#this line splits the groups so each group can be done individually later.
        groups = fields[4].split(',')

	#this print statement prints out to the terminal whenever a user is about to be created with the username shown back to the user.
        print("==> Creating account for %s..." % (username))
	#this line sets the variable cmd with adduser with the parameters --disabled-password, --gecos, '%s', "%s" 
	#with the given gecos and username but no password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

	#The first time you run the code you should comment out the os.system(cmd) to make sure that it won't affect the system at first and make sure everything working
	#If left uncommented the os.system(cmd) statement will attempt to add a user by using the cmd variable that we set earlier.
        print cmd
        os.system(cmd)

	#This print statement prints out to the terminal and tells the user that it is about to set the password for a said user.
        print("==> Setting the password for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain. You'll need to lookup what these linux commands do.
	#this line sets up the cmd variable with two different commands seperated by "|" with the "/bin/echo -ne" printing out the password twice the -ne flag 
	#allows it to use "\n" which is for a new line. The second command uses "sudo passwd username"  and uses it to update the password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #The first time you run the code you should comment out the os.system(cmd) to make sure it won't affect the system at first and make sure everything is correct
	#if left uncommented the os.system(cmd) statement will attempt to set the password with the cmd command above.
	print cmd
        os.system(cmd)

        for group in groups:
	    #this if statement is looking for "-" because if it is found it should not be added to a group
	    #if group is not "-" it will be added to the group with a adduser command.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
