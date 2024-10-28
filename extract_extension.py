filepath=input("enter file path ")
file_extns=filepath.split(".")
print("Enter file extension ",file_extns, type(file_extns))
if len(file_extns)>1:
   print("File extension is:", file_extns[-1])