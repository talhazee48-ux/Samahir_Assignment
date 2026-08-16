#string practice

print("length of the string:")

sentence = "Learning Python can be fun when we practice different concepts and solve small problems every day."
print(len(sentence))

some_words = "Success does not always come quickly, but regular practice, patience, and a positive attitude can help us improve our skills and achieve better results."
print(len(some_words))

#upper case and lower case

print("upper case and lower case:")

print(sentence.upper())
print(sentence.lower())

print(some_words.upper())
print(some_words.lower())

#counting characters

print("counting characters:")

some_name = "Ali lives in a small city. Ali likes reading books and Ali also enjoys learning programming."

print(some_name.count("Ali"))
print(some_name.count("a"))

#bringing first and last character

print("first and last character:")

text = "Hello Python"

print("First character:", text[0])
print("Last character:", text[-1])

if text:
    print("First:", text[0])
    print("Last:", text[-1])
else:
    print("The string is empty.")

#substring

print("substring:")

bookname = "The Old Man and the Sea"

print(bookname[0:3])
print(bookname[4:7])
print(bookname[8:11])
print(bookname[0:10])
print(bookname[12:])

#string slicing

print("string slicing:")

news = "Python is used in many different fields including web development, data science, automation, and artificial intelligence."

print(news[0:6])
print(news[7:14])
print(news[15:20])
print(news[-20:-10])
print(news[:25])

#string reversal

print("string reversal:")

print(news[::-1])
print(sentence[::-1])
print(news[::-2])

#string character replacement

print("string character replacement:")

sentence2 = "The little cat is sitting near the old house."

print(sentence2.replace("cat", "dog"))
print(sentence2.replace("old", "new"))
print(sentence2.replace("little", "small"))

#split and join

print("split and join:")

sentence3 = "Python is simple and useful for beginners."

words = sentence3.split()

print(words)
print("-".join(words))
print(" ".join(words))

#strip and whitespace removal

print("strip and whitespace removal:")

sentence4 = "    Python programming is interesting.    "

print(sentence4.strip())
print(sentence4.lstrip())
print(sentence4.rstrip())

#counting vowels and consonants

print("counting vowels and consonants:")

sentence5 = "Python programming helps students learn useful skills."

vowels = 0
consonants = 0

for character in sentence5.lower():
    if character in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#palindrome check

print("palindrome check:")

word = "racecar"

cleaned_word = ""

for character in word.lower():
    if character.isalnum():
        cleaned_word += character

if cleaned_word == cleaned_word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#converting string into title without using title function

sentence6 = "tHe qUick bROwn fOX jUMps oVER tHE lAZY dOG"

new_sentence = []

for word in sentence6.split():
    new_word = word[0].upper() + word[1:].lower()
new_sentence.append(new_word)

print(" ".join(new_sentence))

#find all indices of a substring

sentence7 = "The rain is falling and the rain makes the road wet."

substring = "rain"

for i in range(len(sentence7)):
    if sentence7[i:i + len(substring)] == substring:
        print("Substring found at index:", i)

#character frequency count

sentence8 = "hello world"

frequency = {}

for character in sentence8:
    if character in frequency:
        frequency[character] += 1
else:
    frequency[character] = 1

print(frequency)

#anagram check

string1 = "listen"
string2 = "silent"

cleaned_string1 = ""
cleaned_string2 = ""

for character in string1.lower():
    if character.isalpha():
        cleaned_string1 += character

for character in string2.lower():
    if character.isalpha():
        cleaned_string2 += character

if sorted(cleaned_string1) == sorted(cleaned_string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#compress repeated characters

text = "aaabbcaaa"

count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
else:
    print(text[i], count)
count = 1

print(text[-1], count)

#longest word in a string

sentence9 = "Python makes programming easier for beginners"

words = sentence9.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)

#removing duplicate characters from a string

sentence10 = "programming"

seen = set()
result = ""

for character in sentence10:
    if character not in seen:
        seen.add(character)
result += character

print(result)

#masked username in email

email = "[pythonstudent@gmail.com](mailto:pythonstudent@gmail.com)"

parts = email.split("@")

username = parts[0]
domain = parts[1]

masked_username = username[0] + "*" * (len(username) - 2) + username[-1]

print(masked_username + "@" + domain)

#check if string starts and ends with specific characters

word = "programming"

if word.startswith("pro"):
    print("String starts with pro")

if word.endswith("ing"):
    print("String ends with ing")

#find number of words in a string

sentence11 = "Python is a popular programming language"

words = sentence11.split()

print("Number of words:", len(words))

#remove spaces from string

text2 = "Python is very easy"

without_spaces = text2.replace(" ", "")

print(without_spaces)

#find position of a word

sentence12 = "I am learning Python programming"

position = sentence12.find("Python")

print("Python starts at:", position)

#check if string contains only numbers

number_text = "123456"

if number_text.isdigit():
    print("The string contains only numbers.")
else:
    print("The string does not contain only numbers.")

#convert first letter to uppercase

name = "ahmed khan"

new_name = name[0].upper() + name[1:]

print(new_name)

#count spaces in a string

sentence13 = "Python is easy to learn"

space_count = 0

for character in sentence13:
    if character == " ":
        space_count += 1

print("Spaces:", space_count)

#remove punctuation from string

text3 = "Hello, Python! How are you?"

result = ""

for character in text3:
    if character.isalnum() or character == " ":
        result += character

print(result)

#check whether a string is empty

text4 = ""

if len(text4) == 0:
    print("The string is empty.")
else:
    print("The string is not empty.")

#capitalize each word manually

sentence14 = "python programming is very useful"

words = sentence14.split()
new_words = []

for word in words:
    new_words.append(word[0].upper() + word[1:])

print(" ".join(new_words))

#count a particular character

text5 = "banana"

print("Number of a:", text5.count("a"))

#check if two strings are equal

first_string = "Python"
second_string = "Python"

if first_string == second_string:
    print("Both strings are equal.")
else:
    print("Strings are different.")

#End of basic string practice
