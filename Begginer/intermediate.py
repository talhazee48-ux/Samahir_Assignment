#Python set intermediate level exercises

#find common items in 3 sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}
common_items = set1 & set2 & set3
print(common_items)

#convert a list with duplicates into a set
numbers = [1, 2, 3, 2, 4, 5, 1]
result = sorted(set(numbers))
print(result)

#find symmetric difference between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference = set1 ^ set2
print(symmetric_difference)

#check if one set is a subset of another
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
if set1 < set2:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

#remove all vowels from a string using set
text = "This is a sample sentence with some vowels"
vowels = {'a','e','i','o','u','A','E','I','O','U'}
result = ''.join([char for char in text if char not in vowels])
print(result)

#Python list intermediate level exercises

#sort name alphabetically but ignore case
names = ["Alice", "bob", "Charlie", "dave"]
sorted_names = sorted(names, key=str.lower)
print(sorted_names)

#rotate a list to the right by one position
list1 = [1, 2, 3, 4, 5]
rotated_list = [list1[-1]] + list1[:-1]
print(rotated_list)

#modify the list without changing the original list
nums = [3,1,4,1,5,9]
sorted_nums = sorted(nums)
print("Original list:", nums)
print("Sorted list:", sorted_nums)

#flatten a nested list using list comprehension
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [item for sublist in nested for item in sublist]
print(flat)

#number in list only appears once
numbers = [1, 2, 3, 2, 4, 2, 5]
unique_numbers = [x for x in numbers if numbers.count(x) == 1]
print(unique_numbers)

#split a list into two lists by odd and even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#find all indices of a specific value in a list
numbers = [1, 2, 3, 2, 4, 2, 5]
indices = [index for index, value in enumerate(numbers) if value == 2]
print(indices)

#replace items from index in a list using slicing
numbers = [10, 20, 30, 40, 50, 60]
numbers[2:5] = [100, 200]
print(numbers)

#list comprehension that returns squares of even numbers
square = [x**2 for x in range(20) if x % 2 == 0]
print(square)

#remove duplicates from a list while preserving the order
nums = [3,1,4,1,5,9,3,4]
unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
print("Original list:", nums)
print("List without duplicates:", unique_nums)

#Python tuple intermediate level exercises

#extract last three elements from a tuple
t = (10,20,30,40,50,60)
last_three = t[-3:]
print(last_three)

#combine two tuples by adding
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined_tuple = t1 + t2
list_c = list(combined_tuple)
print(list_c)

#convert a list into a tuple and name them with variables
numbers_list = [1, 2, 3, 4, 5]
t = tuple(numbers_list)
a, b, c, d, e = t
print(a, b, c, d, e)

#multiply all elements in a tuple
t = (1, 2, 3, 4, 5)
result = t * 3
print(result)

#convert a nested tuple
t = ((1, 2), (3, 4), (5, 6))
flat = tuple(item for subtuple in t for item in subtuple)
print(flat)

#check if two tuple contains same elements
t1 = (1, 2, 3)
t2 = (3, 2, 1)
if sorted(t1) == sorted(t2):
    print("The tuples contain the same elements.")
else:
    print("The tuples do not contain the same elements.")

#pick up second element
tu = ((a,1), (b,2), (c,3), (d,4), (e,5))
second_element = [x[1] for x in tu]
print(second_element)

#store coordinates in tuple and calculate manhattan distance
point1 = (2, 3)
point2 = (5, 7)
distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
print(distance)

#find the number with the highest frequency
t = [1,2,2,3,3,3,4,2]
highest = None
max_count = 0
for item in set(t):
    if t.count(item) > max_count:
        max_count = t.count(item)
        highest = item
print(highest)

#write a function that returns multiple values
def calculate(numbers):
    return sum(numbers), max(numbers), min(numbers)

numbers = [10, 20, 30, 40, 50]
total, maximum, minimum = calculate(numbers)
print("Total:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)

#Python dictionary intermediate level exercises

#merge two dictionaries where second dictionary overwrites first
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

#find the key with the maximum value
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
max_key = max(scores, key=scores.get)
print(max_key)

#invert a dictionary where all values are unique
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {}
for key, value in original_dict.items():
    inverted_dict[value] = key
print(inverted_dict)

#group words by their first letter using a dictionary
words = ["apple", "banana", "cherry", "avocado", "blueberry"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)

#count word frequency in a sentence and store result in dictionary
sentence = "This is a sample sentence with some sample words"
words = sentence.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)

#filter dictionary to include values greater than threshold
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
result = {key: value for key, value in scores.items() if value > 80}
print(result)

#remove all keys from dictionary with None values
data = {'a': 1, 'b': None, 'c': 3, 'd': None}
result = {key: value for key, value in data.items() if value is not None}
print(result)

#combine two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = dict(zip(keys, values))
print(result)

#safely access a deeply nested key
data = {"student":{"address":{"city":"New York"}}}
city = data.get("student", {}).get("address", {}).get("city")
print(city)

#dictionary comprehension that maps numbers to cubes
cubes = {x: x**3 for x in range(1, 11)}
print(cubes)

#Python set intermediate level exercises

#find elements that are in one set but not another
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference = set1 - set2
print(difference)

#give sentence in lowercase and return unique words
sentence = "This is a sample sentence with some sample words"
words = set(sentence.lower().split())
print(words)

#using set comprehension to collect all squares
squares = {x * x for x in range(1,16) if x % 3 == 0}
print(squares)

#count how many duplicates are in a list using set
numbers = [1, 2, 3, 2, 4, 5, 1]
duplicates = len(numbers) - len(set(numbers))
print(duplicates)

#check if two sets are anagrams using set comprehension
set1 = {1, 2, 3}
set2 = {3, 2, 1}
if set(set1) == set(set2):
    print("The sets are anagrams.")
else:
    print("The sets are not anagrams.")

#Python list extra exercises

#find sum of all list elements
numbers = [5, 10, 15, 20]
total = sum(numbers)
print("Sum:", total)

#copy a list using slicing
original = [2, 4, 6, 8, 10]
copy_list = original[:]
print("Copied list:", copy_list)

#Python tuple extra exercises

#find length of tuple
values = (4, 8, 12, 16, 20)
print("Length:", len(values))

#check if value exists in tuple
if 12 in values:
    print("Value is present")
else:
    print("Value is not present")

#Python set extra exercises

#find union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b)
print("Union:", union)

#check if sets have common values
if a.isdisjoint(b):
    print("No common values")
else:
    print("There are common values")

#Python dictionary extra exercises

#display all dictionary keys
student = {"name": "Ali", "age": 20, "course": "Python"}
print(student.keys())

#display all dictionary values
print(student.values())
