print "Enter Number";
a=int(input());
temp=a;
t=0;
while a!=0:
    t= t*10+a%10;
    a=a/10;

if(t==temp):
    print "Number is Palindrome";
else:
    print "Number is not palindrome";
