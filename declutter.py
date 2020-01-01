import os
import time
import shutil

def create_list(list):
    for file in os.listdir(directory):
        list.append(file)
        

def create_directories(newDirectory):
    try:
        os.mkdir(newDirectory + "/Applications")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    try:
        os.mkdir(newDirectory + "/Photos")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    try:
        os.mkdir(newDirectory + "/Videos")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    try:
        os.mkdir(newDirectory + "/Music")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    try:
        os.mkdir(newDirectory + "/Documents")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    try:
        os.mkdir(newDirectory + "/Misc")
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

def organize(file, directory, newDirectory):
    extension = file[-4:]
    print(extension)
        
    if extension in (".exe", ".tar", ".zip"):
        src = directory + "/" + file
        dst = newDirectory + "/Applications/" + file
        os.rename(src, dst)

    elif extension in (".mp4", ".vid", "webm", ".avi", ".mkv"):
        src = directory + "/" + file
        dst = newDirectory + "/Videos/" + file
        shutil.move(src, dst)

    elif extension in (".jpg", "jpeg", ".png"):
        src = directory + "/" + file
        dst = newDirectory + "/Photos/" + file
        os.rename(src, dst)

    elif extension in (".mp3", ".wav", ".aac"):
        src = directory + "/" + file
        dst = newDirectory + "/Music/" + file
        os.rename(src, dst)

    elif extension in (".txt", "docx", ".doc", ".pdf"):
        src = directory + "/" + file
        dst = newDirectory + "/Documents/" + file
        os.rename(src, dst)

    else:
        src = directory + "/" + file
        dst = newDirectory + "/Misc/" + file
        os.rename(src, dst)

def detect(list):
    for file in os.listdir(directory):
        file not in list and organize(file, directory, newDirectory)

if __name__ == "__main__":
    directory = input("Enter the location of the directory that you want to declutter: ")
    print("Please make sure there are no folders in this directory and all files are closed (7 seconds break)")
    time.sleep(7)
    list = []
    create_list(list)
    newDirectory = input("Enter the new directory with sorted files(New Directory cannot be same as the old one): ")
    create_directories(newDirectory)
    for file in os.listdir(directory):
        print(file)
        organize(file, directory, newDirectory)
    f= open("instructions.txt","w+")
    f.write("All exe/tar/zip files were moved to applications folder \n All mp4/vid/webm/avi/mkv files were moved to videos folder \n All jpg/jpeg/png files were moved to photos folder \n all mp3/wav/aac files were moved to music folder \n All txt/docx/doc/pdf files were moved to documents folder \n All other files were moved to misc folder ")
    print("All exe/tar/zip files were moved to applications folder \n All mp4/vid/webm/avi/mkv files were moved to videos folder \n All jpg/jpeg/png files were moved to photos folder \n all mp3/wav/aac files were moved to music folder \n All txt/docx/doc/pdf files were moved to documents folder \n All other files were moved to misc folder ")
    f.close()
    while True:
        detect(list)
        time.sleep(60)

