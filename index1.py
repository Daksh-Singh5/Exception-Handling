try:
   num=float(input("Enter your number: "))
   num2=float(input("Enter your number: "))
   if num2==0:
        raise ZeroDivisionError
   print(num/num2)
except:
    print("error")

