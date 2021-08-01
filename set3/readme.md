Notes from guest lecture

I really enjoyed this lecture. It really got me thinking about how computers can be used to create designs that are more flexible and fluid and allow us to make changes later down the track. The idea of trust was really interesting. We put so much faith in these decisions and then spend no time reflecting on whether it was correct.

Doubt and trust
I doubt this is the answer - the hard bit is then trusting yourself to make it better
The tension of desigining -
Distributed work. What is collaboration?
What is geography?
Asynchronous working
Security and access
Competing monoliths and vendor lock-in. Who is really doing the designing?
Data value
Fighting against the revit way of making - you need to have your own vision, not the corporate vision that autodesk gives us - similar to solidworks
Patrick macleamy curve
Daniel Davis regnier curve
We are able to make decisions easily in the drafting phase - but you actually want to make changes when you are constructuing - but that’s too late
How do you make something where you can change your at the expensive part of the process

...changes occur because design is a knowledge generating process. Often it is only through iteration, exploration, and reflection that the problem - much less the design response - becomes known.

You start to understand when you have designed it, but its too late to change it
You essentially need to deisgn two buildings - one as a full draft and then the second as an improved design once you’ve finnally designed it
Flexibility could come from code
Apps update weekly - they are able to change the code as the app is out in theworld
Set your projexts up well so you can change your mind later on
Above all else, coding allows you to get into the nitty gritty and the deep down of the tool

![alt text](https://github.com/Anthony-Fr-1/me/blob/58fd513adb3462e989215d7e91af20b14a70bcbc/Week%203%201161%20Diagram.png)

REFLECTION ON - Tom Griffiths and Brian Christian on “Algorithms to Live By” Rationally Speaking.

As I was working (struggling) to understand python, I realised I had to step back and work out what I needed to do to get my head around it. So over the weekend I tried to watch as much "beginner" content as I could, just to see it being typed out and hear the same things over and over again so I could start to recognise the patterns. I think after doing this I got the faintest sense of a "click" in my brain that I might be understanding what is actually going on.

The reason I brought this up is because I think part of the click occurred whilst listening to the podcast. One of the last things I desperately struggled with was when I was trying to learn formal logic and argument mapping for a philosophy course a few years ago. I think the reason it was so difficult was that I couldn't relate it back to anything I had learnt previously. I thought about dropping the course for a while. But instead of giving up, I really tried to involve myself in learning the basics repeatedly until I understood it.

Obviously there is a correlation between formal logic and learning to program however a lot of my issues was getting tied up in syntax.

I think this course really changed the way I saw the world. To try to see things from a rational perspective. what is true, what is valid and what is just persuasion. I had actually heard of the book "algorithms to live by" earlier and I think I read the first chapter. I don't think I had the mindset that I do now after taking that philosophy course to see the world as being very irrational, we can learn to navigate it by being rational and logical with our decisions. Changing our perspective from seeing what is directly in front of us to taking a step back and looking at our problems from a higher level. I think trusting in logic, maths and reason is an alleviator for stress.

I'm not sure if this reflection made any sense, but I think it was important to me so oh well hahaha

The pyramid Code

My thinking:
pyramid - create pascals triangle - if 1 replace with \* else " " (space) - wont work - but looked into some of the logic behind pascals triangle

I think the better code were the ones that used words that "made sense" and were readable - I think the ones that used words like "dots" or "stars" or "spaces" were more successful in terms of readability. The ones that just used letters and numbers were hard to read and visualise what each line of code was doing. The ones with useful names seemed to work better and be more elegant solutions to the problem, even if they function in the same way. There is that quote that "beautiful objects work better" I think there is definetly something to creating beautiful looking code

I'm realising more and more in coding that the quote "there are many ways to skin a cat" continues to ring true.

Notes:

below are some notes that I took this week as I took a few beginner course in python. I feel im lagging in the class so I'm doing my best to catchup by doing some extra work

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

guard = 0
while guard < 1000 - this acts as a guard against running forever
guard += 1 - will keep working in the while loop until it reaches 1000

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
