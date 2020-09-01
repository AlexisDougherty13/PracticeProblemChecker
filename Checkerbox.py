import sys
import os
from subprocess import Popen, PIPE
import subprocess
import tempfile
from colorama import Fore, Back, Style

if(len(sys.argv) < 2):
    print("Pass in the file path as the second argument.")
    print("Example: Checkerbox main.cpp")
    sys.exit()

filename = sys.argv[1]
studentOutput = ""
correctOutput = ""
input2 = ""

print("[1] Fire Tracks")
print("*more coming soon")
option = str(input("Which mission is this for? "))
if option == "1":
    input2 = b"13\n2.5"
    correctOutput = "Enter the distance, in miles: \nEnter the time, in hours: \nThe speed is 5.2 miles/hour"
else:
    print("That is not yet an option. Goodbye.")
    sys.exit()

command1 = "g++ " + filename
command2 = "./a.out"
command3 = "rm a.out"

os.system(command1 + ' >/dev/null 2>&1')

#with tempfile.TemporaryFile() as tempf:
#    proc = subprocess.Popen([command2], stdout=tempf)
#    grep_stdout = proc.communicate(input=input2)[0]
#    proc.wait()
#    tempf.seek(0)
#    studentOutput = tempf.read().decode().strip()

command = [command2]
proc = subprocess.run(command, input=input2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
studentOutput = str(proc.stdout.decode())

print()
print(Fore.BLUE + "YOUR OUTPUT____________________")
print(Fore.WHITE + studentOutput)
#print(Fore.BLUE + "_______________________________")

print()
print(Fore.BLUE + "CORRECT OUTPUT_________________")
print(Fore.WHITE + correctOutput)
#print(Fore.BLUE + "_______________________________")

os.system(command3)

print()
for i in range(0, len(correctOutput)):
    if(not (studentOutput[i] == correctOutput[i])):
        print(Fore.RED + "Failed")
        sys.exit()
print(Fore.GREEN + "Passed")

#if(studentOutput == correctOutput):
    #print(Fore.GREEN + "Passed")
#else:
    #print(Fore.RED + "Failed")

