try:
   num = int(input("Enter your number:"))
except ValueError as x:
   print(x)
finally:
   print("This will always work")