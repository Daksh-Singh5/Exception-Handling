try:
   num=float(input("Enter your number: "))
   num2=float(input("Enter your number: "))
   result = num/num2
   print("Answer is",result)
   print("Answer is",result1)

except ZeroDivisionError:
   print("no number is divisible by 0")
except ValueError:
   print("enter only numbers")
except NameError as ex:
   print("there is an exsiption that is",ex)

except:
   print("there is some error in the code")
finally:
   print("I will be there no matter what error showes up")

