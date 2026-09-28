# Indivisible Number Program

## 📘 Description
This program checks whether a given number is **Indivisible** by any number from 2 to 9.  
If the number is divisible by any of them, it prints **Divisible Number**, otherwise **Indivisible Number**.

## 🧠 Logic
- Take an integer input `N`.
- Loop through numbers 2 to 9.
- If `N` is divisible by any of them, mark it as divisible.
- Print the result accordingly.

## 💻 Code
```python
a = int(input())
result = False
for i in range(2, 10):
    if a % i == 0:
        result = True
        break
if result:
    print("Divisible Number")
else:
    print("Indivisible Number")
