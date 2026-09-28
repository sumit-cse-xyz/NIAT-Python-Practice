# For Loops in Python

## 📌 What is a For Loop?

A `for` loop in Python is used to repeat a block of code for each item in a sequence or for a specific number of times.

It is commonly used with `range()`, strings, lists, and other sequences.

## 📌 Syntax

```python
for variable in sequence:
    # code to be executed
```

## 📌 Using range()

The `range()` function generates a sequence of numbers.

### Example:

```python
for i in range(1, 6):
    print(i)
```

### Output:

```text
1
2
3
4
5
```

## 📌 How It Works

```python
for i in range(1, 6):
    print(i)
```

* `range(1, 6)` generates numbers from `1` to `5`.
* `i` takes one value at a time.
* `print(i)` prints the current value.
* The loop continues until all values in the range are completed.

## 📌 For Loop with String

A `for` loop can also be used to access each character of a string.

### Example:

```python
word = "Python"

for character in word:
    print(character)
```

### Output:

```text
P
y
t
h
o
n
```

## 📌 For Loop with Step

The `range()` function can also have a step value.

### Example:

```python
for i in range(2, 11, 2):
    print(i)
```

### Output:

```text
2
4
6
8
10
```

Here:

* `2` → starting value
* `11` → ending value (not included)
* `2` → step value

## 📌 Main Points

* `for` loop is used for repetition.
* It works with sequences and `range()`.
* The loop variable gets one value at a time.
* `range()` is useful when we want to repeat code a specific number of times.
* The ending value of `range()` is not included.

## 🧠 Practice

The Python file `09_For_Loops.py` contains practice problems based on `for` loops.
