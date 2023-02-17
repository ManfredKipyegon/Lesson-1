nums = []

list_length = 5

for i in range(list_length):
    number = eval(input("Enter a number"))
    nums.append(number)

for num in nums:
    print(num)   
    nums[-2]