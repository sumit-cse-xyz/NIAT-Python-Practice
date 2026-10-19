# Valid Password - 3
# A password is valid if it has at least one uppercase, one lowercase, and one digit.

a = input()
has_upper = False
has_lower = False
has_digit = False

for i in a:
    if i.isupper():
        has_upper = True
    elif i.islower():
        has_lower = True
    elif i.isdigit():
        has_digit = True

if has_upper and has_lower and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
