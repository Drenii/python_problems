#finding average value of N numbers

num=int(input("How many numbers "))
sum=0

for i in range(num):
    numbers=float(input("enter any number "))
    sum+=numbers

avg=sum/num
print("Average of ", num, " numbers is " , avg) 