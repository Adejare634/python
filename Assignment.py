#creating file
New_file = open("Alphanumeric_nums.txt","w+")
New_file.write('64ja')
New_file.close()

num = int(input('Enter Number: '))
if num % 4 == 0:
    print('Number is divisible by 4')
else:
    print('Number is not divisible by 4')