I think im starting to understand "how" to do things and visualise a little bit better what is going on. But I still find myself getting stuck in syntax or just working out how to write out the script that I want to make. Perhaps I need to get better as pseudocode and diagramming

Sketchpad

It's incredible to think about how fundamental this method of creating geometries is as the basis for all of our current CAD software. I've seen a video on sketchpad before but every time I see it being used, I'm still amazed that they were doing this in 1962.

"The Future of Programming" - Bret Victor

I think once the novelty of this video wore off I started to realise just how insightful it was to thinking about where we have come from in terms of programming. Once again, the idea that the human should come first in programming languages rang true. With every example he showed, we could see increasingly accessible and more human-centric designs for machine interactions. I particularly liked that they were thinking about flowcharts to program as this seems to be the basis for grasshopper and coding blocks, which are both ways of programming that I really enjoy.

The idea that a computer can be understood however we as humans design it to be was actually quite a profound thought. I think of so many other languages, notations and diagrammatic systems that are bound by the traditions of that field

One example would be something like music. Music is written in a notation language and thus is bound by a person being able to read and interpret that language. Whereas guitar tabs notation is more on the diagrammatic side and is "easier" to read for beginners.

Interesting Quotes

technology changes quickly, peoples minds change slowly
computers will change with time - moores law - but peoples minds wont change in this same linear way
there was resistance with the changes in ways of programming - people didnt want to change from binary to soap
people had to unlearn what they knew and do things differently
the most dangerous thought you can have as a creative is thinking that you know what you're doing. becuase once you think you know what you're doing, you stop looking around for other ways of doing things - you stop being able to see what else is possible
the first step is to say - i dont know what im doing and i dont know what a computer is. once you do this then you are free to think differently
how can we represent data visually - using diagrams and visualling lists of data
representing programming spatially by using video screens
programming with flowcharts - grail 1968
interactive computing
nobody knew what programming was supposed to be
In science if you know what you are doing you should not be doing it.
In engineering if you do not know what you are doing you should not be doing it.
Of course, you seldom, if ever, see either pure state.

> > > f = open('workfile', 'w')

r = read only
w = write (old file deleted)
a = opens the file for appending - data is added to the end
r+ = opens the file for reading and writing

HOW TO FIND THE LARGEST ITEM IN A LIST

#This is Pseduocode to find the greatest element in the list

You have a List with the following number elements

A = [10 20 30 10]

to find the max value in a list like that, you can use the Max sort method.

To perform this method you need to save 1 variable => the current maximum value.

You can initialize the max as 0

MAX = 0

lets iterate over this list and see what the following code does

for x in A:
if MAX < x:
MAX = x
What happens here. Lets go over the iterations

in iteration one x = A[0] = 10 and MAX = 0

    Is 10 greater than 0? OF COURSE

    Now MAX is 10

in iteration two x = A[1] = 20 and MAX = 10

    Is 20 greater than 10? OF COURSE

    Now MAX is 20

in iteration Three x = A[2] = 30 and MAX = 20

    Is 30 greater than 20? OF COURSE

    Now MAX is 30

in iteration Four x = A[3] = 10 and MAX = 30

    Is 10 greater than 30? NOPE

    MAX REMAINS THE SAME = 30

This method only cares about the max values that it sees, so all VALUES
less than max are thrown away. Doing this you can extract the max elements
in a list.
