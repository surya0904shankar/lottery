


def system_lottery():
    import mysql.connector as f 
    my=f.connect(host="localhost",user="root",passwd="root",database="lottery")
    n=my.cursor() 
    sys_loop=[]
    import random as r
    num=r.randint(100000,999999)
    sys=str(num)
    n.execute("select lottery_number from lottery")
    x=n.fetchall()

    while True:
        for i in x:
            for j in i:
                sys_loop.append(j)
            
        if sys in sys_loop:
            print("the number already exixts fetching an another number")
            system_lottery()
            break
                
        elif sys not in sys_loop:                
            print("the number selected by the system is: ",sys)
            name=input("please enter your name: ")
            val="insert into lottery values(%s,%s)"
            n.execute(val,(name,sys))            
            my.commit()
            print(name+" your lottery number is "+sys)
            break
