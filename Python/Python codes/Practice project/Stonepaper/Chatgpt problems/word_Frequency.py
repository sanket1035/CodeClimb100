'''Question 2: Word Frequency from File

🧾 Topics used: File handling, String methods, Dictionary, Loops

📄 Task:

Create a .txt file with a paragraph (or take user input and write it to a file)

Read the file and:

Count total number of words
Count frequency of each word (ignore case, use .lower())

Print top 3 most frequent words
🔁 Bonus: Use sorted() with lambda to sort dictionary values'''


with open("sanket.txt","w") as f:
    f.write("Hey Man are you you are is you are you alive Man If man kills its Good for all of us ")

with open("sanket.txt",) as f:
    content=f.read()
    newcontent=content.lower()
    print(newcontent)

words = newcontent.split()  
freq = {}  

for word in words:
    if word in freq:           # If word is already in dictionary
        freq[word] = freq[word] + 1
    else:                      # If word is not in dictionary
        freq[word] = 1

# Sort the dictionary by values (frequencies), in descending order
sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)

# Print top 3 most frequent words
print("Top 3 frequent words:")
for word, count in sorted_words[:3]:
    print(f"{word} -> {count}")
 