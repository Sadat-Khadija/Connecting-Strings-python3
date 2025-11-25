🧵 Printing Multiple Strings on One Line
1. Output multiple string variables on a single line 📝

You can print several string variables together to form a full sentence.

Example:
first = "Python"
second = "is"
third = "fun!"
print(first, second, third)


👉 Output: Python is fun!

2. Use the plus (+) connector or commas to connect strings ➕ ,

There are two ways to connect strings in the print() function:

A. Using the plus (+) operator ➕

Only works with strings

You must add spaces manually

first = "Python"
second = "is"
third = "awesome"
print(first + " " + second + " " + third)

B. Using commas in print() ,

Automatically adds a space between items

Easier and cleaner for beginners

print(first, second, third)

3. Create spaces between variables in a print() function 🧩

You can add spaces in two ways:

A. Add a space inside the string
print(first + " " + second + " " + third)

B. Use commas (Python adds spaces for you)
print(first, second, third)

C. Customize spacing using the sep parameter 🛠️
print(first, second, third, sep=" ")


Or remove all spaces:

print(first, second, third, sep="")
