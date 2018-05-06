f=input("Enter a 1st");
s=input("Enter a 2nd");
t=input("Enter a 3rd");
n=input("Enter no of times you want to print series");
i=0;
print f,s,t
for i in range(n):
    u=f+s+t;
    print u,
    f,s,t=s,t,u;
