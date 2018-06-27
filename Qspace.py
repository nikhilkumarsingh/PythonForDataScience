f=str(input("Name:"))
f=f+".txt"
f=open(f,'r')
y=str(f.read())
l=[]
l=y.split(' ')
print(len(l)-1)