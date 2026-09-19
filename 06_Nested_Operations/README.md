# Nested Operations

## Topic

Nested Operations in Python

## Description

Nested operations means using multiple operations or conditions together in a Python program.

Nested operations can be used with:

* Arithmetic operators
* Comparison operators
* Logical operators
* Conditional statements

## Operators Used

### Arithmetic Operators

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `%` Modulus

### Comparison Operators

* `>` Greater than
* `<` Less than
* `>=` Greater than or equal to
* `<=` Less than or equal to
* `==` Equal to
* `!=` Not equal to

### Logical Operators

* `and`
* `or`
* `not`

## Conditional Statements

### if

The `if` statement executes a block of code when a condition is True.

### elif

The `elif` statement checks another condition when the previous condition is False.

### else

The `else` statement executes when all the above conditions are False.

## Example

### Code

```python
marks = int(input())

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

### Input

```text
75
```

### Output

```text
Grade B
```

## Another Example of Nested Operations

```python
a = int(input())
b = int(input())

if a > b:
    result = (a - b) * 2
    print(result)
elif a == b:
    result = (a + b) * 2
    print(result)
else:
    result = (b - a) * 2
    print(result)
```

### Input

```text
10
6
```

### Output

```text
8
```

## What I Learned

* How to use multiple operations together.
* How `if`, `elif`, and `else` work.
* How conditions can be combined with operations.
* How Python executes nested operations step by step.
