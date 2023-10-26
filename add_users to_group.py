import subprocess
import os
 
def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE, shell=True).communicate()[0].decode()
    print("Enter a list of groups to add the user to.")
    print("The list should be separated by spaces, for example: group1 group2 group3")
    print("The available groups are:\n" + output)
    chosenGroups = input("Groups: ")
 
    output = output.split()
    chosenGroups = chosenGroups.split()
    
    print("Add To:")
    found = False
    groupString = ""
 
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
        if found == False:
            print("- New Group: " + grp)
            groupString = groupString + grp + ","
        else:
            print("- Existing Group: " + grp)
            groupString = groupString + grp + ","
        found = False
 
    groupString = groupString[:-1] + " "
    confirm = ""
    while confirm != "Y" and confirm != "N":
        print("Add user '" + username + "' to these groups? (Y/N)")
        confirm = input().upper()
        
    if confirm == "N":
        print("User '" + username + "' not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username)
        print("User '" + username + "' added")
 
add_user_to_group()