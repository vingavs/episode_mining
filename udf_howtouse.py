In order to use UDF, 
pass three parameters as input

1) sequence - it is a 2D numpy array of type int
-first column is time
-2nd column is the event sequence
-event sequence starts at 1

2) window_size - it is of type int

3) frequency threshold - it is a float

in the current code, individual events, their 2way combinations and 3way combinations are considered as episodes.