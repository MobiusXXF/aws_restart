# Introducing System Administration with Python
# Use os.system() to run a Bash command
# Use subprocess.run() to run Bash commands

import os
import subprocess

# The function os.system() takes a string
os.system("ls")
print("")

# The function subprocess.run(), recommended to use as it is more powerful than os.system()
subprocess.run(["ls"]) # -- Single Arguement
print("")

# Using subprocess.run with two arguments
subprocess.run(["ls","-l"]) # -- Double Argument
print("")

# Retrieving system information
# The subprocess.run() function is powerful because you can use it to run any Bash command
# Using "uname" command to get system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Retrieving information about disk space
# df or ps?
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
