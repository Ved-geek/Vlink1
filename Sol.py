from sys import stdin
from sys import stdout

n=int(stdin.readline())
if n>=1:
    string=list(map(str,stdin.readline().split()))
    ans=''
    length=0
    # print(string)
    for i in string:
        if len(i)>length:
            length=len(i)
            ans=i
    print(ans)
else:
    print('Invalid Input')
