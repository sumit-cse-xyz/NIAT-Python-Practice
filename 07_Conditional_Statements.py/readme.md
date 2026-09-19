# Conditional Statements in Python

## 📌 Introduction

Conditional statements in Python are used to make decisions based on conditions. They execute a block of code when a condition is true or false.

## 📚 Topics Covered

* if statement
* if-else statement
* if-elif-else statement
* Nested if statement
* Conditions and comparisons

## 🔹 1. if Statement

The `if` statement executes a block of code only when the given condition is true.

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### Output

```text
Eligible to vote
```

## 🔹 2. if-else Statement

The `if-else` statement executes one block when the condition is true and another block when the condition is false.

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### Output

```text
Not eligible to vote
```

## 🔹 3. if-elif-else Statement

The `if-elif-else` statement is used to check multiple conditions.

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

### Output

```text
Grade B
```

## 🔹 4. Nested if Statement

A nested if statement is an if statement inside another if statement.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

### Output

```text
Entry allowed
```

## 🧠 Key Learning

* Conditional statements help programs make decisions.
* `if` checks a condition.
* `else` executes when the condition is false.
* `elif` checks another condition.
* Indentation is important in Python.

## 🛠️ Language Used

* Python

## 🎯 Conclusion

Conditional statements are an important part of Python programming because they allow programs to make decisions based on different conditions.
