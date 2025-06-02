import re  # Regular expression module

pattern = re.compile(r',\s*')

text = "apple, banana,  cherry,grape"
parts = pattern.split(text)

print(parts)  # Output: ['apple', 'banana', 'cherry', 'grape']
