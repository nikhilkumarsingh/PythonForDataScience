import re
n=input()
pattern = re.compile("[789]")
if pattern.match(n)!=None and len(n)==10:
	print("Valid")
else:
	print("Invalid")
