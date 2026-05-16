while True:
    account=100000
    card="c"
    pwd=1234
    b=input("insert the card")
    if b==card:
        print("welcome ramya")   
        a=int(input("enter the pwd"))
        if a==pwd:
            print('''choose options
              1.bal enq
              2.withdraw''')
            e=int(input(""))
            if e==1:
                print(account)
            elif 2==e:
                d=int(input("withdraw amount"))
                print(account-d)
            else:
                print("invalid options")
        else:
            print("invalid password")
            
        
    else:
        print("invalid card")
        
     
