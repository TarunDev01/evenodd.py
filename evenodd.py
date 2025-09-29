num=int(input("Enter a number:"))
if num%2==0:
   print("the number is Even")
else:
   print(num,"the number is Odd")

# Check if a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
