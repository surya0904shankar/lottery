

def user_lottery():
    import mysql.connector as f 
    my=f.connect(host="localhost",user="root",passwd="root",database="lottery")
    n=my.cursor()
    loop=[]

    user=input("enter a 6 DIGIT NUMBER for BINGO LOTTERY selection")
    flag=0
    while True:
        if len((user))!=6:
            print("invalid digit entered, digit count is not 6 please choose again!")
            user_lottery()
            break
                
        elif len((user))==6:
            n.execute("select lottery_number from lottery")
            x=n.fetchall()

            for i in x:
                for j in i:
                    loop.append(j)
        
            if user in loop:
                print("the number already exists please choose another number")
                user_lottery()
                break
            
            elif user not in loop:
                    print("the number is available")
                    name=input("please enter your name: ")
                    val="insert into lottery values(%s,%s)"
                    n.execute(val,(name,user))
                    my.commit()
                    print(name+" your lottery number is "+user)
                    break
