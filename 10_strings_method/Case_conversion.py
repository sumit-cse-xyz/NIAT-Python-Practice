## 🧩 Question
Given a string, write a program to modify the string as given below.  
- Add a hyphen (`-`) before each upper‑case character.  
- Convert upper‑case characters into lower‑case characters.  

Print the modified string.

### 📥 Input
The input will be a single line containing a string.

### 📤 Output
Print the modified string.

### 💻 Code
```python
a = input()
result = ""
for i in a:
    if i.isupper():
        result = result + "-" + i.lower()
    else:
        result = result + i
print(result)
