import os

def rename_files():
    #(1) Get file names from a folder
    file_list = os.listdir("/home/utibe/Desktop/Udacity/Secret_Message/prank")
    directory = "/home/utibe/Desktop/Udacity/Secret_Message/prank"
    
    #print(file_list)
    print("There are "+format(len(file_list))+" elements in the file list variable")

    #(2) For each file, rename the filename
    digits = "01234567890"
    #for file_name in file_list:
    for file_name in os.listdir(directory):
        remove_digits = str.maketrans('','',digits)
        new_file_name = file_name.translate(remove_digits)
        
        path = os.path.join(directory,file_name)
        target = os.path.join(directory,new_file_name)

        os.rename(path,target)

rename_files()
