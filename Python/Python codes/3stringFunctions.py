# Start with a sample string
string = "Sanket Chaudhari"
print("Original String:", string)

# 1. lower()
print("Lowercase:", string.lower())

# 2. upper()
print("Uppercase:", string.upper())

# 3. strip() – (example has no leading/trailing spaces, so let's add some)
strip_example = "   " + string + "   "
print("Stripped:", strip_example.strip())

# 4. replace()
print("Replace 'a' with '@':", string.replace('a', '@'))

# 5. split()
print("Split by space:", string.split())

# 6. join()
words = string.split()
print("Join with '-':", "-".join(words))

# 7. find()
print("Find 'C':", string.find('C'))

# 8. startswith()
print("Starts with 'Sanket':", string.startswith('Sanket'))

# 9. endswith()
print("Ends with 'i':", string.endswith('i'))

# 10. format()
name = "Sanket"
formatted = "Hello, {}".format(name)
print("Formatted string:", formatted)

# 11. isdigit()
print("Is Digit:", string.isdigit())  # False because it has letters

# 12. isalnum()
print("Is Alphanumeric:", string.isalnum())  # False because of space

# 13. isalpha()
print("Is Alphabet only:", string.isalpha())  # False because of '4'

# 14. count()
print("Count of 'a':", string.count('a'))
