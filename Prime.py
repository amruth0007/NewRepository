num=int(input("Enter the the to check : "))
for i in range(2,num):
    if num%2==0:
        print(num,"is not prime")
        break
else:
    print(num,"is prime")
