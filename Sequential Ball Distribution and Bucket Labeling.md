# Programming & Reasoning Test

There are  different buckets labelled as {1,2,3,... q}. There are a total of  number of balls, and Ali will place each ball into the aforementioned  number of buckets according to the following rule. 

1. Place the balls one at a time into the buckets starting from bucket , then to bucket , and all the way to bucket 1. If , then at this stage, all buckets would have been filled with one ball each.

2. If there are still remaining balls left, repeat the process again, placing one ball each starting from bucket  all the way to bucket 1.

3. Repeat step 2 until there are no balls left.

4. Now label each of the balls with the label of their respective buckets. For example, all balls within bucket 7 will be labelled as 7.

5. Take out all the balls in bucket  and place them in a single line. Then, take out all the balls in bucket  and place the balls at the end of that line. Continue this process all the way till bucket 1 has been emptied. Now, you would have a single line of balls that look something like this:



a) Given a label , write a python function that takes in ,  and , and outputs the total number of balls corresponding to the label .
b) Calculate, mathematically, the expected output of the python function written in a) when ,  and . (Please include clear derivation steps)
c) Then, write a python function that takes in  and  as input, and outputs a list of integers representing the line of balls in step 5.
