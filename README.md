# INET4031 Add Users Script and User List
## Program Description
This program automates the process of adding users to a Linux system. Normally a user would use adduser, passwd, and adduser {user} {group} for each individual user. However, with this program it automates it by allowing for multiple to be done at the same time. This script uses those same commands but with Python. 
## Program User Operation
This program reads input from an input file and creates accounts based on that data. Each line represents a new user. The program will check if the line is formatted properly and if any lines are commented out using "#". If it runs into any format errors or comments it'll skip past that line and move onto the next. Otherwise, it will run the Linux commands to create a user, set the password, and assign the groups.

### Input File Format
Each line should have 5 inputs seperated by colons. For Example:

`username:password:last_name:first_name:group`

If multiple groups are to be assigned, the user should seperate them with a comma. For example:

`username:password:last_name:first_name:group01,group02`

If a user wants to skip a line in the input file they should put a "#" at the beginning of the file. For example:

`#username:password:last_name:first_name:group`

If a user wants a new user to not be assigned to any groups they should use "-" on the group input. For example:

`username:password:last_name:first_name:-`

### Command Execuction
In order to run the program, the python file needs to be executable. For example:

`chmod +x create-users.py`

Then the following command should be run to execute it.

`./create-users.py < create-users.input`

This command tells the python file to read inputs directly from the create-users.input file.
### "Dry Run"
A "dry run" is when the lines that execute the system commands are commented out, in this case it would only print out and nothing would change in the system. This allows for the user to check and make sure the program works before running the program for real. Once the program looks functional the user can uncomment the lines and it will actually run.
