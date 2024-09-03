import os
# Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). The script should display the total number of items (both files and directories) present in the specified directory. Bonus Modify your script to count the number of files and directories separately. Hint: use the os module

# Submission: Please upload it to GitHub and submit the link. 

dir=input("What directory would you like to count the number of items in?: ") 
dir_list=os.listdir(dir)
file_count=0
dir_count=0

for entry in os.scandir(dir):
    if entry.is_file():
        file_count+=1
    if entry.is_dir():
        dir_count+=1

print(f"Number of directories is: {dir_count}")
print(f"Number of files is: {file_count}")



print(dir_list)