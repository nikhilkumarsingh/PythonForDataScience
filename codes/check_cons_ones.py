n=input('enter the binary number: ')
k=input('enter the value of K: ')
g=0
l=int(k)
g='1'*l
if(g in n):
	print("yes there are given no. of consecutive 1's in the binary number")
else:
	print('NO')