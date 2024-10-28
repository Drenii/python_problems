filepath=input("enter file path ")
file_extns=filepath.split(".")

if len(file_extns)>1:
   print("File extension is:", file_extns[-1])