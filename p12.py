s=input("Enter a String");
ss=input("Enter substring");

if(s.find(ss)>-1):
    print "Substring is at index",s.find(ss);
else:
    print "Not found"
