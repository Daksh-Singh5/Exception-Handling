trueorfalse=False
while not trueorfalse:
    try:
        num=float(input("Enter your number: "))
        while num%2==0:
            print("bye")
            trueorfalse=True
    except:
        print("your number is not divisible by 2")