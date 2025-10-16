# ==========================
# BASIC PYTHON DATA TYPES
# ==========================

# 1. int (integer numbers)
age = 25
print(age)              # 25
print(age + 5)          # 30 → integers support math operations
print(type(age))        # <class 'int'>

# 2. float (decimal numbers)
price = 19.99
print(price)            # 19.99
print(price * 2)        # 39.98 → floats also support math
print(type(price))      # <class 'float'>

# 3. bool (True/False values)
is_logged_in = True
print(is_logged_in)     # True
print(5 > 3)            # True → comparison gives a boolean
print(type(is_logged_in))  # <class 'bool'>

# 4. str (strings / text)
name = "Jacob"
print(name)             # Jacob
print(name.upper())     # JACOB → strings have methods
print(len(name))        # 5 → length of string
print(type(name))       # <class 'str'>


# ==========================
# COLLECTION TYPES
# ==========================

# 5. list (ordered, changeable, allows duplicates)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")     # add item
print(fruits)               # ['apple', 'banana', 'cherry', 'orange']
print(fruits[1])            # banana → access by index
print(type(fruits))         # <class 'list'>

# 6. tuple (ordered, unchangeable, allows duplicates)
coordinates = (10.5, 20.3)
print(coordinates)          # (10.5, 20.3)
print(coordinates[0])       # 10.5
print(type(coordinates))    # <class 'tuple'>

# 7. set (unordered, unique items, no duplicates)
unique_numbers = {1, 2, 2, 3}
print(unique_numbers)       # {1, 2, 3} → duplicate "2" removed
print(type(unique_numbers)) # <class 'set'>

# 8. dict (key : value pairs, like a mini database)
person = {"name": "Jacob", "age": 25, "city": "Bethlehem"}
print(person)               # {'name': 'Jacob', 'age': 25, 'city': 'Bethlehem'}
print(person["name"])       # Jacob → access value by key
print(type(person))         # <class 'dict'>


# ==========================
# CUSTOM TYPES (Classes)
# ==========================

class SuperCar:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def turbo(self):
        return f"{self.brand} goes {self.speed * 2} km/h with turbo!"

car = SuperCar("Ferrari", 200)
print(car.turbo())          # Ferrari goes 400 km/h with turbo!
print(type(car))            # <class '__main__.SuperCar'>


# ==========================
# SPECIAL DATA TYPES
# ==========================

# Modules (extra tools you can import)
import math
print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.141592653589793

# None (represents “nothing” / empty value)
result = None
print(result)               # None
if result is None:
    print("No result yet...")  # This will print


# --- Challenge 1 ---
# Ask the user for their name
name = input("What is your name? ")
# Ask the user for their age (note: input always returns a string by default)
age = input("How old are you? ")
# Print a friendly greeting using f-strings
print(f"Hello {name}, you are {age} years old!")


# --- Challenge 2 ---
# Ask for the age (convert to integer for numeric comparison)
adult_age = int(input("How old are you? "))
# If/else check
if adult_age < 18:
    print(f"{adult_age}, you are still young! You can't enter.")
else:
    print(f"{adult_age}, welcome to adulthood! Yes, you can enter.")

# --- Challenge 3 ---
# Convert input to int so you can compare numbers
your_age = int(input("How old are you? "))

if your_age < 18:
    print(f"You are {your_age} years old, still young! No entry.")
elif your_age >= 18 and your_age < 65:
    print(f"You are {your_age} years old, welcome to adulthood! You may enter.")
else:
    print(f"You are {your_age} years old, wow, retirement club! Take a seat, elder legend.")

# --- Challenge 4 ---
age_color = int(input("How old are you? "))
fav_color = input("What is your favorite color? ")

if age_color < 18 and fav_color.lower() == "blue":
    print(f"You're young and love {fav_color} — future coding legend alert!")
elif age_color >= 18 and fav_color.lower() == "red":
    print(f"Mature and fiery with {fav_color} — unstoppable energy!")
else:
    print(f"Interesting combo: {age_color} years old and favorite color {fav_color}!")
