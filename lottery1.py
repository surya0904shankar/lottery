def lottery():
    import user_lottery
    import system_lottery
    import mysql.connector as f
    import random as ra
    import  tabulate 
    loop=[]
    my=f.connect(host="localhost",user="root",passwd="root",database="lottery")
    n=my.cursor() 
    num=int(input("enter 1 to continue as user enter 2 to continue as admin: "))
    if num ==1:
        print("WELCOME USER TO BINGO LOTTERY")
        print("----------------------------------------------------------------------")
        k=int(input("enter '1' to choose your number enter'2' for the system to generate a number for you: "))
        print("----------------------------------------------------------------------")
        
        if k==1:
            user_lottery.user_lottery()
        elif k==2:
            system_lottery.system_lottery()
    elif num==2:
        import mysql.connector as f 
        my=f.connect(host="localhost",user="root",passwd="root",database="lottery")
        na=input("enter your name: ")
        passwd=input("enter your password: ")
        n=my.cursor()
        n.execute("select * from access")
        x=n.fetchall()
        for i in x:
            if na==i[0] and passwd==i[1]:
                se=int(input("enter 1 to view the database enter 2 to pick the lottery: "))
                if se==1:
                    from tabulate import tabulate
                    my=f.connect(host="localhost",user="root",passwd="root",database="lottery")
                    n=my.cursor()
                    n.execute("select * from lottery")
                    x=n.fetchall()
                    h=["NAME","LOTTERY NUMBER"]
                    p=(tabulate(x,headers=h,tablefmt='pretty'))
                    print(p)
                elif se==2:
                    n.execute("select lottery_number from lottery")
                    x=n.fetchall()

                    for i in x:
                        for j in i:
                            loop.append(j)
                    winner=ra.choice(loop)
                    print("tne winner of BINGO LOTTERY is:",winner)
                else:
                    print("wrong input")
            else:
                print("invalid credentials")
    else:
        print("input not defined please try again")
        


        
lottery()
        