with open("this.txt","r") as f:
    file=f.read()
print(file)



with open("this.txt","w") as f:
    f.write("Hello! This file is created now.")