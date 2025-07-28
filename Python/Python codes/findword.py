with open("mine.txt","r") as f:
    lines=f.readlines()

lineNo=1
for line in lines:
    if("Saa" in line):
        print(f"word is in file. Line no:{lineNo} ")
        break
    lineNo+=1
else:
    print("word is not in file ")
    