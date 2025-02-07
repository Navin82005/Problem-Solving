import re

text = "hai this is naveen from navin82005@gmail.com. You can talk to me using your own email address (eg. myemail@gmail.com)"
text = "this:is@my@gmail.com.ismy@gmail.com:"

# Finding email
tmp = re.findall(r"[a-zA-Z0-9]+@[a-z0-9.-]+[.][a-z0-9]+", text)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# print(tmp)
# print(emails)
print("apple".__hash__())