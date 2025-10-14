# --- Simple Greeting Program ---

# Ask the user for their name
user_name = input("What is your name? ")

# Greet them with proper spacing and style
print(f"Hello, {user_name}! Welcome aboard.")  # Pro: f-strings

# Ask the user for their age
age = input("How old are you? ")
print(f"{user_name}, you are {age} years old. That's awesome!")

# Example: respond differently depending on the name
if user_name.lower() == "jacob":
    print("Wow, we have the same name as the coder of this program!")
else:
    print(f"Nice to meet you, {user_name}.")


# --- Challenge 1: Favorite Color ---
fav_color = input("What is your favorite color? ")

if fav_color.lower() == "blue":
    print("Wow, blue is my favorite too!")
else:
    print(f"{fav_color}? That's a nice choice!")


# --- Challenge 2: Introduction Generator ---
intro_name = input("What is your name?: ")
intro_age = input("How old are you?: ")
intro_city = input("Where are you from?: ")

print(f"Hello, my name is {intro_name}. "
      f"I'm {intro_age} years old and I live in {intro_city}.")


# --- Challenge 3: Age Validation (Refined Version Only) ---
age_input = input("How old are you? ")

if not age_input.isdigit():
    print("Please enter a valid age.")
else:
    your_age = int(age_input)
    if your_age < 18:
        print(f"{your_age}? You are still young! You can't enter the club.")
    else:
        print(f"{your_age}, welcome to adult life! You can enter the club!")


# --- Challenge 4: Personality Test ---
fav_animal = input("What is your favorite animal? ")
fav_hobby = input("What is your favorite hobby? ")
fav_food = input("What is your favorite food? ")

if fav_animal.lower() == "dog":
    print(f"You are loyal and energetic like a {fav_animal}, "
          f"who loves {fav_hobby} and can't resist {fav_food}.")
elif fav_animal.lower() == "cat":
    print(f"You are independent and clever like a {fav_animal}, "
          f"who enjoys {fav_hobby} and can't resist {fav_food}.")
else:
    print(f"You are unique for choosing {fav_animal}, "
          f"a soul who loves {fav_hobby} and can't resist {fav_food}.")


# --- Challenge 5: Age Gate with Validation Loop ---
while True:  # Loop until we explicitly "break"
    age_input = input("How old are you? ")

    # Check if the input is a number
    if age_input.isdigit():
        break
    else:
        print("Please enter numbers only (e.g., 18).")

# Convert to integer after validation
age = int(age_input)

# Decide based on age
if age == 0:
    print("Freshly born coder detected! 🍼")
elif age < 18:
    print(f"You are {age}. You are still young! Come back later.")
elif age > 100:
    print(f"Whoa, {age}? Are you sure you're human?! 👽")
else:
    print(f"Welcome, {age}-year-old! You are allowed in!")
