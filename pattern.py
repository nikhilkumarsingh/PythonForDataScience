n = int(input("Enter a odd number for a beautiful pattern: "))
for i in range(n):
   for j in range(n):
     print(n-min(i,j,n-1-i,n-1-j),end="")
   print()
 
