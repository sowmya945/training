adj = ["red", "healthy", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


i = 1
while i < 6:
    print(i)
    i += 1

# Python program to print the multiplication table of 23 from 1 to 10
# Loop from 1 to 10
for i in range(1, 11):
    # Print the multiplication of 23 by i
    print(f"23 x {i} = {23 * i}")            