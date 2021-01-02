import mysql.connector
import datetime
con=mysql.connector.connect(host='localhost',user='root',password='',database='deepak')
cur=con.cursor()
print("press 1 for create account")
print("press 2 for withdraw")
print("press 3 for Deposit")
print("press 4 for fund transfor")
print("press 5 for blance enquary")
print("press 6 for change password")
print("press 7 for summary")

n=int(input("enter youe choice"))
date=datetime.date.today()

if n==1:
     na=input("enter your password")
     name=input("enter your name")
     ad=input("enter address")
     ga=input("enter your genger")
     phone=input("enter your phoneno")
     email=input("enter your email")
     c=input("enter your country")
     s=input("enter your state")
     ct=input("enter your city")
     ca=int(input("enter your currentamount"))

     ac="SBI"
     x=0
     sql="select * from account "
     cur.execute(sql)
     for row in cur:
          x=x+1
     if x>0:
        x=x+1
        x=x+100
        ac=ac+str(x)
     else:
        ac="PNB101"

     s="insert into account values('"+ac+"','"+na+"','"+name+"','"+ad+"','"+ga+"',"+str(phone)+",'"+email+"','"+c+"','"+s+"','"+ct+"',"+str(ca)+")" 
     cur.execute(s)
     con.commit()
     print("BADHI HO SIR JEE AAPKA ACCOUNT KHUL GAIYA PAISA DE KE JAA")
     con.close()
elif n==2:
     a=input("enter account number")
     p=input("enter pin")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
          wamt=int(input("enter amount to withdraw"))
          if wamt<=camt:
               camt=camt-wamt
               s="update account set currentamount="+str(camt)+" where account='"+a+"'"
               cur.execute(s)
               con.commit()
               s="insert into summary (account,tranction,date,action,Blance) values('"+a+"','"+str(wamt)+"','"+str(date)+"','withdraw','"+str(camt)+"')"
               cur.execute(s)
               con.commit()
               print("after withdraw ",wamt," your current balence is =",camt)
          else:
               print("GARIB HAI RE TU")
     else:
                print("SACH SACH BOL TERA HI HAI ACCOUNT OR PIN")
               
elif n==3:
     a=input("enter account number")
     p=input("enter pin")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
          damt=int(input("enter amount to Deposite"))
          if damt<50000:
               camt=camt+damt
               s="update account set currentamount="+str(camt)+" where account='"+a+"'"
               cur.execute(s)
               con.commit()
               s="insert into summary (account,tranction,date,action,Blance) values('"+a+"','"+str(damt)+"','"+str(date)+"','deposite','"+str(camt)+"')"
               cur.execute(s)
               con.commit()
               print("after Deposite ",damt," your current balence is =",camt)
          else:
               print("GARIB HAI RE TU")
     else:
                print("SACH SACH BOL TERA HI HAI ACCOUNT OR PIN")
               
elif n==5:
     a=input("enter account number")
     p=input("enter pin")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
         print("your Deposit blance is:=",camt)
              
     else:
          print("GARIB HAI RE TU")
          

               
elif n==4:
     a=input("enter account number")
     p=input("enter pin")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
          camt=int(d[10])
     if x>0:
          fund=int(input("enter amount to transfor"))
          if fund<=camt and fund>0:
               camt=camt-fund
               
          else:
               print("GARIB HAI RE TU")
     else:
                print("SACH SACH BOL TERA HI HAI ACCOUNT OR PIN")
     ac1=input("enter account no where you transfor")
     b="select * from account where account='"+ac1+"'"
     cur.execute(b)
     camt1=0
     x1=0
     for row in cur:
          x1=x1+1
          camt1=int(row[10])
     if x1>0 and x>0:
          camt1=camt1+fund
          d="update account set currentamount='"+str(camt1)+"'where account='"+ac1+"'"
          cur.execute(d)
          con.commit()
          w="update account set currentamount='"+str(camt1)+"'where account='"+ac1+"'"
          cur.execute(w)
          con.commit()
          s="insert into summary (account,tranction,date,action,Blance) values ('"+a+"','"+str(fund)+"','"+str(date)+"','transfor','"+str(camt)+"')"
          cur.execute(s)
          con.commit()
          print("your amount is transfor")
     else:
          print("you have enter the worng amount")

elif n==6:
     a=input("enter account number")
     p=input("enter password")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
     if x>0:
          v=input("enter new password")
          s="update account set password='"+v+"'where password='"+p+"'"
          cur.execute(s)
          con.commit()
          print("password change sucssfull")
     else:
          print("enter worng password")

elif n==7:
     a=input("enter account number")
     p=input("enter pin")
     s="select * from account where account='"+a+"' and password='"+p+"'"
     camt=0
     x=0
     cur.execute(s)
     for d in cur:
          x=x+1
     if x>0:
          s="select * from summary where account='"+a+"'"
          cur.execute(s)
          print("account\t","tranction\t","date\t","action\t","Balance")
          for d in cur:
               print(d[0],"\t",d[1],"\t",d[2],"\t",d[3],"\t",d[4],)
          
     else:
          print("enter account is invalid")
     

