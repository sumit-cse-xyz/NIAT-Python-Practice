# Loop Control Statements in Python

## 📌 Introduction
Loop control statements are used to change the normal execution of a loop. They help us control how a loop runs.

Python has three main loop control statements:

1. `break`
2. `continue`
3. `pass`

## 1. Break Statement
The `break` statement is used to stop the loop immediately when a given condition is satisfied.

**Example:**
```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

**Output:**
```text
1
2
3
```

**Explanation:** When `i` becomes 4, the loop stops.

## 2. Continue Statement
The `continue` statement skips the current iteration and moves to the next iteration of the loop.

**Example:**
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**
```text
1
2
4
5
```

**Explanation:** When `i` becomes 3, that iteration is skipped.

## 3. Pass Statement
The `pass` statement does nothing. It is used as a placeholder when a statement is required syntactically but no action is needed yet.

**Example:**
```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

**Output:**
```text
1
2
3
4
5
```

**Explanation:** The `pass` statement does nothing, so the loop continues normally.

## 📊 Difference Between Loop Control Statements

| Statement | Purpose |
|---|---|
| `break` | Stops the loop completely. |
| `continue` | Skips the current iteration. |
| `pass` | Does nothing; acts as a placeholder. |

## 🎯 Key Takeaways
- `break` terminates the loop.
- `continue` skips the current iteration.
- `pass` does not change the loop's execution.
- These statements can be used with both `for` and `while` loops.

## 👨‍💻 Practice
Practice these statements with different conditions to understand how they work.

**Language:** Python  
**Topic:** Loop Control Statements
