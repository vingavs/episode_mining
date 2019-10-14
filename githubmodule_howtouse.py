for using the github module,

the function is 
w = WINEPI(random31, random42, 'serial')

random31 is a 2D list
the first element of each row is time of type int
the second element of each row the event type of type str

I have defined event type from 'A' to 'Y' in my sample code  

random42 is a 1D list
it contains all the episodes which much be searched for in the sequence
In my code, random42 is ['A'...'Y','AA','AB'...'AY'...'YY','AAA'...'YYY']

w2=w.discover_frequent_episodes(0, 2722, 20, 0.2)

There are 4 inputs, 
1st input is start time - 1
2nd input is end time + 1
3rd input is window size
4th input is frequency threshold