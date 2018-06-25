n = int(input("Enter an odd number for a beautiful pattern: "))
if n%2 != 0:
  for i in range(n):
      for j in range(n):
         print(n-min(i,j,n-1-i,n-1-j),end="")
      print()
else
  print("Not an odd number")
 
