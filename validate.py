# regular expression is a pattern and this Library the re library
# in Python is going to let us to define some of these patterns
import re


email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# # if (username) and ("." in domain):
# if (username) and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")