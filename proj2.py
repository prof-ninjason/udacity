import os
def rename_files():
    #(1) get file names from folder
    flist = os.listdir(r"C:\tmp")

    #print(flist)
    saved_path = os.getcwd()
    print("cwd: " + saved_path)
    os.chdir(r"C:\tmp")
    print("cwd: " + os.getcwd())
    
    #(2) for each file, rename filename
    for file_name in flist:
        print("Old Filename: " + file_name)
        print("New Filename: " + file_name.translate("0123456789"))

        os.rename(file_name,file_name.translate("0123456789"))

    os.chdir(saved_path)

rename_files()