import os

# Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). The script should display the total number of items (both files and directories) present in the specified directory. Bonus Modify your script to count the number of files and directories separately. Hint: use the os module

# Submission: Please upload it to GitHub and submit the link. 

# dir=input("What directory would you like to count the number of items in?: ") 
# dir_list=os.listdir(dir)
# file_count=0
# dir_count=0

# for entry in os.scandir(dir):
#     if entry.is_file():
#         file_count+=1
#     if entry.is_dir():
#         dir_count+=1

# print(f"Number of directories is: {dir_count}")
# print(f"Number of files is: {file_count}")


# print(dir_list)


    

def find_files_with_ext(Directory, Extension):
    if not Extension.startswith("."):
        Extension = "." + Extension

    matching_files = [ ]
    for root, __, files in os.walk(Directory):
        for file in files:
            if file.endswith(Extension):
                matching_files.append(os.path.join(root, file))
    return matching_files

Directory = input("Give me the Directory path: ").strip()
Extension = input("And give me the extension you are looking for: ").strip()
  
files = find_files_with_ext(Directory, Extension)

if files:
    print("\nFound Files: ")
    for index, file in enumerate(files, start = 1):
            print(f"{index}. {file}")
else:
    print(f"No file with '{Extension} in '{Directory}!")