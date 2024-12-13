try:
    tester={'Codigal':3,'is':2,'best':2,'for':2,'coding':1}
    print(tester)
    selection=int(input("enter the number you want to see the frequency of"))
    counter=0
    for value, value in tester.items():
        if selection==value:
            counter=counter+1
    print("the number of occurence of your number is",counter)
except ValueError:
    print("enter an integer please")