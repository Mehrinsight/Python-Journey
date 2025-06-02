import re  # Regular expression module

pattern = re.compile(r'\b[A-Z][a-z]*\b')

#\b = word boundary
#[A-Z] = capital letter
#[a-z]* = zero or more lowercase letters

text = "Alice and Bob went to Paris."
matches = pattern.findall(text)

print(matches)  # Output: ['Alice', 'Bob', 'Paris']
