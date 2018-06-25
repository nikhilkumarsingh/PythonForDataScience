import re
n="981127588"
pattern = re.compile("[789]")
if pattern.match(n)!=None and len(n)==10:
	print("Valid")
else:
	print("Invalid")
