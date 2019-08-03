/** Counting valleys. 
Given a string of size n having letters 'U' for Up 1 units and 'D' for down 1 units
find the number of times you will leave a valley at level zero, considering your starting level is 0.

Example : "UUDDUDDDUU"

  /\
_/  \/\    _
       \  /
	    \/
		

Result will be 1, as you leave a valley at level 0 only once
*/

def countingValleys(n, s):
    h = 0 # Initial level
    c = 0 # Counter to keep track of no of valleys visited
    for j in range(n):
        i = s[j]
        if i == 'U':
            h += 1
        elif i == 'D':
            h -= 1
        if h == 0 and i == 'U':
            c = c+1
    return c
	
a = input("Enter the data : ");
n = len(a)
print(countingValleys(n,a))