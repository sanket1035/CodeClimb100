with open("donkey.txt","r") as f:
    content=f.read()

with open("mine.txt","r") as f:
    contentNew=f.read()

if(content==contentNew):
    print("Files is Identical")
else:
    print("Files is Not Identical")

