I had my first sort of coding problem and solution moment. I really had to think this one through like a programmer. Perhaps quite a simple problem, but for me it was quite challenging to get my head around. But I think it plays into that idea of not repeating yourself or doing something that is unnecessary

Basically I needed something that refers to a reference table of the 203 unique longitude and latitudes and adds them to the larger data frame which contains the 82000 entries. So it doesn’t call the API for each record.

    1. Creates a shortened list of only the unique cities
    2. Runs the script and finds the long/lat of the 203 unique cities
    3. Creates a dictionary of this data
    4. Writes this dictionary to a file
    5. Appends the data frame with details from a dictionary

Essentially i'm creating a look-up table like in excel but in python.

python/grasshopper lecture

I really enjoyed the lecture that we had on python and grasshopper. I think a lot of things clicked into place when i saw and heard about how it could be used. I always thought it would be used to create geometries but it's interesting that it is mainly used for data manipulation. I think it sort of peels back the curtain a bit about what is going on with a component in grasshopper - the way it takes inputs, runs a script and then produces an output.

notes from python grasshopper lecture

python is good for data manipulation more than for creating geometries
grasshopper uses ironpython so it doesnt support some of the latest features like requests
python is often used for joining the dots between data.
good for doing a quick list comprehension on a list
Vectorised operations that is used in pandas is the same mindset that is happening in grasshopper - get a pattern of trues/falses - grasshopper is different because it uses a tree data structure - very similar to dictionaries - work basically the same but theyre different
update cycle in grasshopper - it keeps recalculating and re-updating - wait until something happens and then make a change to the cycle
a directed acyclic graph - if i change a component, everything is down stream from that - its all downstream - the information keeps flowing down the components
display - canvas widgets - profiler - this shows how long things are taking in grasshopper - shows where the really sluggish parts of your script are

I think i need to look more into creating efficient algorithms in grasshopper. Ben mentioned a few concepts but I think i need to go back over the recording and write them down
