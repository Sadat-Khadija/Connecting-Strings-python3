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



Fixing TypeError (Data Type Mismatch)
❗ What is the problem?

A TypeError happens when Python tries to combine data types that don’t work together.

In this case, the code tries to add a string and an integer, which Python cannot do.

❌ Example (causes TypeError)
# The following code causes a type error between a string 
# and an integer:

print("5 * 1 = " + 5*1)


Python sees:

"5 * 1 = " → string

5*1 → integer (5)

And this combination is not allowed.

✅ How to Fix It: Use Explicit Conversion

To fix the error, we must convert the integer to a string using str().

✔ Corrected Code:
print("5 * 1 = " + str(5*1))

🧠 Why This Works

The str() function changes the result of 5 * 1 (which is 5) into a string, so Python can safely join:

"5 * 1 = "  +  "5"