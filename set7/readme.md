Solidworks/Python/Grasshopper - Thoughts on integrating computational processes in an industrial design setting

The problem with Solidworks

    - Industrial designers use computers but the designer is not able to get in control of the computer. They are at the whim of the software maker. Computational processes are about making tools to help realize a design. Its like being able to create your own features in solidworks. Don’t have to wait for them to release a feature in the latest version

The Strengths and Weaknesses of Solidworks and grasshopper

    - Solidworks has the feature tree and parametric data tables for dimensions. But you’re more at the whim of solidworks realising features. - With grasshopper you can create and see the connections far better but Grasshopper is slow when you're trying to make a final production part.

The middle between the two

    - ultimately the designer shouldn’t be held back by software in industry 4.0. So we need something right in between it all. Something that is designer (design process) friendly and something that is able to create functions. Basically we should be able to take control of autonomous processes and mathematics to create geometries and design. Ultimately to achieve efficiency in drafting and allowing us to spend more time focusing on designing than cad

Skeleton modelling/top down modelling process

    - A common process in solidworks modelling is the top down modelling process. This essentially creates a master sketch of key       dimensions that other parts in the assembly will reference off. This is great for assembly modelling as you can change dimensions in the master and it will parametrically update the child features.
    - Grasshopper is really great for mocking out dimensions, like a parametric rod and node system. So can we mock things up in grasshopper and then use this as the basis for the arrangement and dimensions of components? Can we use grasshopper to find the optimal layout of components by manipulating the values of a master sketch?
    - A lot of times products work like miniature systems. A system can be described as a flowchart. The product itself is really just a kind of sandwich arrangement of these system parts. If we could imbed some kind of internal logic we could arrange these parts with a computational process.

    ![alt text](https://github.com/Anthony-Fr-1/me/blob/ae2a5ba9ba984ccb363d0f10ed9c6c906191a0e5/Pictures/Skeleton%20Modelling%201.png)
    ![alt text](https://github.com/Anthony-Fr-1/me/blob/ae2a5ba9ba984ccb363d0f10ed9c6c906191a0e5/Pictures/Skeleton%20Modelling%202.png)

Potential Process

    - 1. Make a script in grasshopper to automate the boring stuff and create the data
    - 2. Then put the data into solidworks as a data table and manipulate it.
    - 3. Create lists and loops to repeat actions on solid parts.

Grasshopper is really good for getting angles and lengths really quickly and basically making a “skeleton” to use as the basis for you final model. So basically if you wanted to make some cool wavy thing in solidworks, mock it up in grasshopper, export it as a csv, run a quick if/then or for loop script in solidworks and automate the feature that would be really repetitive
