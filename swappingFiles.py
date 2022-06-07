def Swap():
    file1 = input('Enter the 1st file: ')
    file2 = input('Enter the 2nd file: ')

    with open(file1) as f1:
        data_a = f1.read()
    
    with open(file2) as f2:
        data_b = f2.read()

    with open(file1,'w') as abcd:
        abcd.write(data_b)
    
    with open(file2,'w') as xyz:
        xyz.write(data_a)

Swap()