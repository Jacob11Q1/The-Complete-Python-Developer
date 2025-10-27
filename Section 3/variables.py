# -----------------------------
# Variables and Basic Printing
# -----------------------------
user_iq = 180
user_name = "Jacob"
user_age = 29

print("Basic variable printout:")
print(user_iq)                       # 180
print(user_name)                     # Jacob
print(user_age)                      # 29
print()  # blank line for readability

# -----------------------------
# Arithmetic with variables
# -----------------------------
print("Arithmetic examples:")
print(user_iq + 20)                  # Addition → 200
print(user_iq - 30)                  # Subtraction → 150
print(user_iq * 2)                   # Multiplication → 360
print(user_iq / 2)                   # Division → 90.0
print(user_iq ** 2)                  # Exponentiation → 32400
print(user_iq // 7)                  # Floor division → 25
print(user_iq % 7)                   # Modulus (remainder) → 5
print()

# -----------------------------
# Assignment Shorthands
# -----------------------------
print("Assignment shorthand examples:")
user_score = 100
print("Starting score:", user_score)

user_score += 50
print("After += 50:", user_score)

user_score -= 20
print("After -= 20:", user_score)

user_score *= 2
print("After *= 2:", user_score)

user_score //= 3
print("After //= 3:", user_score)
print()

# -----------------------------
# String Formatting with f-strings
# -----------------------------
print("String formatting examples:")
print(f"{user_name}'s IQ is {user_iq}, and age is {user_age}.")
print(f"In 5 years, {user_name} will be {user_age + 5}.")
print()

# -----------------------------
# Conditions
# -----------------------------
print("Conditional example:")
if user_iq > 150:
    print(f"{user_name} is a genius with IQ {user_iq}!")
elif user_iq >= 100:
    print(f"{user_name} is above average with IQ {user_iq}.")
else:
    print(f"{user_name} has IQ {user_iq}, keep grinding!")
print()

# -----------------------------
# Tiny User Profile System (Dictionary)
# -----------------------------
print("User profile system:")
user_profile = {
    "name": user_name,
    "age": user_age,
    "iq": user_iq,
    "skills": ["Python", "JavaScript", "HTML", "CSS"]
}

# Access values
print("Name:", user_profile["name"])
print("Age:", user_profile["age"])
print("IQ:", user_profile["iq"])
print("Skills:", ", ".join(user_profile["skills"]))
print()

# Update dictionary
user_profile["age"] += 1
user_profile["skills"].append("Django")

print("Updated profile:", user_profile)
print()

# -----------------------------
# Looping through skills
# -----------------------------
print("Loop through skills:")
for skill in user_profile["skills"]:
    print(f"- {skill}")
