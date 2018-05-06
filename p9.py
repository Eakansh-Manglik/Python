import math

print "Enter Number";
a=int(input());
temp=a; t=0;

while temp!=0:
    t += math.pow(temp%10,3);
    temp/=10;

if(a==t):
    print "Number is Armstrong";
else:
    print "Number is not Armstrong";
