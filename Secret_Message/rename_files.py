import os

def rename_files():
    #(1) Get file names from a folder and set current working directory
    directory = "/home/utibe/Desktop/Udacity/Secret_Message/prank"
    file_list = os.listdir(directory)
    print("Current working directory is "+os.getcwd())
    print("Changing directory to the specified directory")
    os.chdir(directory)
    
    #(2) Get Number of files in that folder
    print("There are "+format(len(file_list))+" elements in the file list variable")

    #(3) For each file, rename the filename
    digits = "01234567890"
    for file_name in file_list:
        remove_digits = str.maketrans('','',digits)
        new_file_name = file_name.translate(remove_digits)
        os.rename(file_name, new_file_name)
        
rename_files()
