n=int(input())
s=0
temp=n
while (temp>0):
	e=temp%10
	s+=e**3
	temp//=10
if (n==s):
	print("yes")
else:
	print("no")
	
	