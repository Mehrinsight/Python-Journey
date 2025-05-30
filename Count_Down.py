# Prompt the user to enter the starting number and convert it to an integer
x = int(input('start point> '))

# Loop to count down from x to 0
while x >= 0:
    print(x)  # Print the current number
    x -= 1   # Decrease x by 1 each iteration
