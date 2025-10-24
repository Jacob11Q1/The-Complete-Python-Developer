# Python Operator Precedence Demonstration

print("=== 1. Parentheses ===")
print((3 + 5) * 2)   # 16

print("\n=== 2. Exponentiation ** (right-associative) ===")
print(2 ** 3 ** 2)   # 512

print("\n=== 3. Unary operators (+, -, ~) ===")
print(-5 ** 2)       # -25 (exponent runs before negation)
print(~6)            # -7 (bitwise NOT)

print("\n=== 4. Multiplicative (*, /, //, %) ===")
print(7 * 3)         # 21
print(7 / 3)         # 2.333...
print(7 // 3)        # 2
print(7 % 3)         # 1

print("\n=== 5. Additive (+, -) ===")
print(10 - 3 + 2)    # 9

print("\n=== 6. Bitwise shifts (<<, >>) ===")
print(4 << 1)        # 8
print(8 >> 2)        # 2

print("\n=== 7. Bitwise AND & ===")
print(6 & 3)         # 2 (110 & 011 = 010)

print("\n=== 8. Bitwise XOR ^ and OR | ===")
print(6 ^ 3)         # 5
print(6 | 3)         # 7

print("\n=== 9. Comparisons, is, in ===")
print(3 < 5)         # True
print(5 == 5.0)      # True
print(5 is 5)        # True (but don't rely on 'is' for numbers always!)
print(3 in [1,2,3])  # True

print("\n=== 10. Boolean NOT ===")
print(not False)     # True

print("\n=== 11. Boolean AND ===")
print(True and False) # False

print("\n=== 12. Boolean OR ===")
print(True or False)  # True

print("\n=== 13. Conditional expressions (ternary) ===")
a = 10 if True else 20
print(a)             # 10

print("\n=== 14. Lambda ===")
square = lambda x: x**2
print(square(4))     # 16

print("\n=== 15. Assignment operators ===")
x = 5
x += 3
print(x)             # 8

print("\n=== 16. Walrus operator (:=) ===")
if (n := len("hello")) > 3:
    print("Length:", n)  # 5

print("\n=== 17. Tuples, Lists, Dicts, Sets, Comprehensions ===")
a, b = 1, 2
print(a, b)          # 1 2
print([x for x in range(3)]) # [0, 1, 2]
print({'a': 1, 'b': 2})      # {'a': 1, 'b': 2}
