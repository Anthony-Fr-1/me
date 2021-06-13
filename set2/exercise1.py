"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#  defines a list of words
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# will print a word from the list
for word in some_words:
    print(word) # goes down the list and print the words in order
# prints the list number of the word
for x in some_words:
    print(x) # goes down the list and print the words in order
# prints list of words
print(some_words) # prints list of words
# If list has more than 3 words in it, it will print
if len(some_words) > 3:
    print('some_words contains more than 3 words') # printed list because there are more than 3 words

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
