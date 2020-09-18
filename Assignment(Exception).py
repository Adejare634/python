Test_List = ['shoe', 'bag', 'hat', 'cloth']
try:
    test = Test_List[4]
    print(test)
except IndexError as error:
    print('Only Three arguments are found')


try:
    print(x)
except NameError as error:
    print('X not found')

