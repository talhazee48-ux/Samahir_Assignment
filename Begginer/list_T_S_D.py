#list practice

numbers = [2, 8, 15, 32]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

#list length

colors = ["red", "blue", "green"]

print(len(colors))

colors.append("yellow")
print(colors)

#insert into list

fruits = ["apple", "orange"]

fruits.insert(1, "banana")
print(fruits)

#remove from list

fruits.remove("orange")
print(fruits)

#remove from list using pop

items = ["pen", "pencil", "eraser"]

items.pop(1)
print(items)

#check if an item is in the list

numbers = [1, 2, 3, 4, 5]

print(3 in numbers)
print(7 in numbers)

#list slicing

num2 = [10, 20, 30, 40, 50]

print(num2[1:4])
print(num2)

num2[num2.index(30)] = 35
print(num2)

#count the number of occurrences of an item

list2 = [1, 2, 2, 3, 2, 4, 5]

print(list2.count(2))

#list sorting

marks = [45, 12, 67, 34, 89]

marks.sort()

print(marks)

#list reverse

items2 = ["a", "b", "c", "d"]

items2.reverse()

print(items2)

#tuple practice

numbers_tuple = (10, 20, 30, 40)

print(numbers_tuple[1])
print(len(numbers_tuple))

#tuple unpacking

someone = ("khan", 22)

name, age = someone

print(name)
print(age)

#tuple concatenation

tuple1 = (20, 30, 50)
tuple2 = (60, 70, 80)

tuple3 = tuple1 + tuple2

print(tuple3)

#checking item in tuple

tuple_num = (20, 30, 50, 60)

print(20 in tuple_num)
print(100 in tuple_num)

#empty tuple

empty_tuple = ()

print(type(empty_tuple))

#repeat a tuple

numbers2 = (7,)

print(numbers2 * 3)

#tuple index

numbers3 = (1, 2, 3, 4, 5, 6, 7)

print(numbers3.index(1))
print(numbers3.index(4))

#tuple count

print(numbers3.count(2))

#tuple with one element

numbers4 = (5,)

print(type(numbers4))

#tuple slicing

numbers5 = (10, 20, 30, 40, 50)

print(numbers5[1:4])

#set practice

set1 = {1, 2, 3, 4, 5}

print(set1)

#adding elements to a set

set1.add(6)

print(set1)

#removing elements from a set

set1.remove(3)

print(set1)

#checking if an element is in a set

print(4 in set1)
print(10 in set1)

#length of set

print(len(set1))

#clearing a set

set1.clear()

print(set1)

#adding multiple elements to a set

set2 = {"a", "b", "c"}

set2.update(["d", "e"])

print(set2)

#removing elements using discard

set2.discard("b")

print(set2)

#convert list into set

numbers6 = [1, 2, 3, 3, 4, 5, 5]

unique_numbers = set(numbers6)

print(unique_numbers)

#union and intersection

set3 = {1, 2, 3}
set4 = {3, 4, 5}

print(set3.union(set4))
print(set3.intersection(set4))

#difference between sets

print(set3.difference(set4))

#dictionary practice

my_dict = {
"name": "Alice",
"age": 30,
"city": "New York"
}

print(my_dict["name"])
print(my_dict["age"])

#adding a key value pair

my_dict["book"] = "Python Programming"

print(my_dict)

#updating a value

my_dict["age"] = 31

print(my_dict)

#removing a key

del my_dict["city"]

print(my_dict)

#checking a key in dictionary

print("salary" in my_dict)
print("name" in my_dict)

#dictionary keys

print(my_dict.keys())

#dictionary values

print(my_dict.values())

#dictionary items

for key, value in my_dict.items():
    print(key, value)

#get method in dictionary

print(my_dict.get("score", 0))

#creating dictionary using dict constructor

my_dict = dict(zip(["name", "age"], ["Bob", 25]))

print(my_dict)

#dictionary length

print(len(my_dict))

#add another value

my_dict["course"] = "Python"

print(my_dict)

#check dictionary value

if "name" in my_dict:
    print("Name is present")
else:
    print("Name is not present")

#End of basic practice of list, tuple, set and dictionary
