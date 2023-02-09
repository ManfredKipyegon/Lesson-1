#ask input check if neg, if neg then wrong input if pos check greater than 50 if greater than 50 div by 2 if less than 50 say less than 50
num = eval(input("Enter age:"))
if num <= 0:
    print("Wrong input")
else:  
     if num > 50:
         x = num/2
         print(x)
     else:
        print("Number is less than 50")
         
    