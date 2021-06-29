TODO: Reflect on what you learned this week and what is still unclear.

pyramid - create pascals triangle - if 1 replace with \* else " " (space)

F-Strings
print(f"{chosen_number} is too big or too small") # includes chosen number and number can change
print(chosen_number is too big or too small")

while True:
This is good for when you want user input. when you want the input to be correct

METHODS/FUNCTIONS FOR STRINGS
course = "my string" # typing course dot e.g. course. # print(course.upper()) - upper case # print(course.replace("string", "variable")) replace "this" with "that" - the original data must exist for this to work
will show you all the functions you can do with that string object
e.g course.upper would make it upper case

NEED TO REVISE NESTED LOOPS

binary search of sorts:
FIND THE HIGHEST NUMBER IN THE LIST
this will keep looping until its no longer true and it reaches the highest value in the list

APPEND - add something to the end of a list

numbers = [3, 8, 6, 2, 10]
max = numbers[0]
for number in numbers:
if number > max:
max = number
print(max)

Finding stuff # print(course.find("y")) - this will show you the list position of the letter "y" in your string - sensitive to lower and upper case
"in" - a key word
print("string" in course) - returns true/false - is string in course? yes or no

CONDITIONALS
indentation - python uses indentation instead of {}
so
if x > 10

WHILE LOOP
i = 1
while i <= 10
print(i)
i = i + 1 - this changes what i means - what i has been assigned to

len - number of elements within a list
abs - always return a positive number
round - rounds a float
https://docs.python.org/3/library/math.html

- print("yes")
- print("that's correct")
  will execute the code until you go out of the indent - essentially the end of the bracket

if this is true - do this
elif is true - or do this instead if this statement is true
else: - if none of the above conditions are true

CONVERTING INPUTS
e.g. input()
input function will return a string - needs to be converted using the types below
float() - convert to a float
int() - convert to integer
bool() - convert to boolean
str() - convert to string

Logical operators
not - inverts any values
and - returns true if both expressions are true
or - returns true if AT LEAST one expression is true

Arthimetic operators + - concatenate - - Subtraction
// - returns integer - whole number
/ - returns float - decimal point
% - modulus
** - to the power of e g. x to the power of y is x**y \* - multiply
== - equal to
= - assign
Augmented assignment operator
x = 10 - need to define variable
x = x + 3 therefore 13
x += 3 is 13 means the same thing as above
Comparison operators
<= >=
!= not equal to
