# How does it work?  
Plot a circle. We are going to add several lines to that cirle. 
The ends of each lines are on the circle. 

The idea works as follow: 
- choose a point on the circle. That will be the first end of the first line. 
- the other end of the line will be on the other side of the circle (first point + $\pi$)
- draw the line linking the two ends 
- the second line again has two ends. To locate the beginning of the line, take the first line's beginning, add an angle $\theta$
- to locate the end of the second line, take the first line's end, add an angle $\alpha * \theta$
- repeat the process for the third line, fourth line... 

Basically, each line has two ends which are moving at a different speed. By overlapping the different lines we get 
the figures.

To use this project, first run `plotting_func.py` to generate the pictures. 
Then run `plots.ipynb` to create the gif 

# Result
![Final result](optimized_curves.gif)

# Sources
The idea was inspired from [this video (in French)](https://www.youtube.com/watch?v=-X49VQgi86E). 
I took some liberties to code program, so the logic may look different by the results look similar