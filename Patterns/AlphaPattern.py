'''Print the following pattern for the given N number of rows.
 Pattern for N = 3
 A
 BB
 CCC
 '''

N=int(input()) #taking input from the user
i=1
while(i<=N):
    j=1
    start=chr(65+i-1)  # chr(z) : gives the character value associated with z
    while(j<=i):
        print(start,end='')
        j+=1
    print()
    i+=1
    
'''
-----------------------
Input:
 6
-----------------------
Output:
A
BB
CCC
DDDD
EEEEE
FFFFFF
-----------------------
'''
