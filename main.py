name=input("Enter Your name:")
string=name
palindrome=''
for word in name[::-1]:
  palindrome+=word 
if palindrome== string:
  print("Palindrome")
else:
   print("Not Palindrome")