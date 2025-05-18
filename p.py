# Number guessing
print("This is a list of numbers: 15, 35, 45, 85, 95, 105")
num=int(input("Guess the right number."))

if num==85:
    print("You have guessed the right number.")
if num<85:
      print("Wrong number and it is smaller than the number")

else:
     print("Wrong number and it is greater than the number")

    



# list
list = ['Toyota', 'Mercedes Benz', 'Volkswagen', 'BMW', 'Kia']

print("Length of list:", len(list))
print("First Element:", list[0])
print("Last Element:", list[-1])

list.append('Toyota')
print("Updated List: ", list)

list.remove('Volkswagen')
print("Updated List: ", list)

list.sort()
print("Sorted List: ", list)

list.pop(1)
print("Updated List: ", list)

list.reverse()
print("Reversed List: ", list)

print("Multiplication on List :", list*2)

list = list[:4]
print("Sliced list :", list)

list.clear()
print("Updated List :", list)




# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 39
print(my_dict)

# add item
my_dict['address'] = 'Juja'
print(my_dict)

# remove particular element
my_dict.pop('age')
print(my_dict)

# access a particular element
print("Address :", my_dict.get('address'))

# remove all the elements
my_dict.clear()
print(my_dict)



#List to Dictionary
def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Joan', 'VI'], [2, 'Lola', 'VII'], [3, 'Lynette', 'VIII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))