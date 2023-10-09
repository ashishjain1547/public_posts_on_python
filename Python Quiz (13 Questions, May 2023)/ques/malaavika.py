import re

s = "Malaaavikaa"

s = re.sub("a{2}", "*", s) # Mal*avik*

print(s)