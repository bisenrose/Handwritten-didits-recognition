import mysql.connector
import re
import random
import time
import sys
import csv
import os
import string
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
from tabulate import tabulate
mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="class12b")
cursor=mycon.cursor()
cursor.execute("drop table if exists winter")
cursor.execute("drop table if exists summer")
cursor.execute("drop table if exists fall")
cursor.execute("drop table if exists spring")

#INPUT ID'S
names=['Rose']
usernames=['xxRosexx']
passwords=['12345']
addresses=['Lnt Raintree']
phnos=['9901522733']
mails=['rosesinghbisen@gmail.com']

#date
todays_date = date.today()
winter_l=[11,12,1]
spring_l=[2,3,4]     
summer_l=[5,6,7]
autumn_l=[8,9,10]
td= todays_date.month
def display():
        if td in winter_l:
                print('*'*45,"THE WINTER COLLECTION",'*'*47)
                cursor.execute("select * from winter")
                data=cursor.fetchall()
                headers=['Retail No.','Candle Name','Scent','Colour','Size','Price','Stock','Sold']
                print(tabulate(data,headers=headers,tablefmt="rounded_outline"))
        elif td in autumn_l:
                print('*'*45,"THE AUTUMN COLLECTION",'*'*47)
                cursor.execute("select * from fall")
                data=cursor.fetchall()
                headers=['Retail No.','Candle Name','Scent','Colour','Size','Price','Stock','Sold']
                print(tabulate(data,headers=headers,tablefmt="rounded_outline"))
        elif td in summer_l:
                print('*'*45,"THE SUMMER COLLECTION",'*'*47)
                cursor.execute("select * from summer")
                data=cursor.fetchall()
                headers=['Retail No.','Candle Name','Scent','Colour','Size','Price','Stock','Sold']
                print(tabulate(data,headers=headers,tablefmt="rounded_outline"))
        elif td in spring_l:
                print('*'*45,"THE SPRING COLLECTION",'*'*47)
                cursor.execute("select * from spring")
                data=cursor.fetchall()
                headers=['Retail No.','Candle Name','Scent','Colour','Size','Price','Stock','Sold']
                print(tabulate(data,headers=headers,tablefmt="rounded_outline"))
                    

def winter():
        cursor.execute("drop table if exists winter")
        cursor.execute("create table winter(pnum int,product varchar(30),scent varchar(50),colour varchar(20),size varchar(10),price float,quantity int,purchased int)")
        cursor.execute("insert into winter values(01,'Frosted cranberry','Cranberry','Violet','Small',299.00,50,0)")
        cursor.execute("insert into winter values(02,'Frosted cranberry','Cranberry','Violet','Medium',499.00,50,0)")
        cursor.execute("insert into winter values(03,'Frosted cranberry','Cranberry','Violet','Large',699.00,50,0)")
        cursor.execute("insert into winter values(04,'Ash','Charcoal, Coconut & Beeswax','Black','Small',299.00,50,0)")
        cursor.execute("insert into winter values(05,'Ash','Charcoal, Coconut & Beeswax','Black','Medium',499.00,50,0)")
        cursor.execute("insert into winter values(06,'Ash','Charcoal, Coconut & Beeswax','Black','Large',699.00,50,0)")
        cursor.execute("insert into winter values(07 ,'Boulangerie Jar','Whipped cream & Apple peel','Beige','Large',699.00,50,0)")
        cursor.execute("insert into winter values(08 ,'Boulangerie Jar','Whipped cream & Apple peel','Beige','Large',699.00,50,0)")
        cursor.execute("insert into winter values(09 ,'Boulangerie Jar','Whipped cream & Apple peel','Beige','Large',699.00,50,0)")
        cursor.execute("insert into winter values(10,'Ivy','Cinnamon, Sandalwood','Burnt Orange','Small',299.00,50,0)")
        cursor.execute("insert into winter values(11,'Ivy','Cinnamon, Sandalwood','Burnt Orange','Medium',499.00,50,0)")
        cursor.execute("insert into winter values(12,'Ivy','Cinnamon, Sandalwood','Burnt Orange','Large',699.00,50,0)")
        cursor.execute("insert into winter values(13,'Holiday','Vanilla','White','Small',299.00,50,0)")
        cursor.execute("insert into winter values(14,'Holiday','Vanilla','White','Medium',499.00,50,0)")
        cursor.execute("insert into winter values(15,'Holiday','Vanilla','White','Large',699.00,50,0)")
        cursor.execute("insert into winter values(16,'Illumine','Juniper berry, Tobacco','Maroon','Small',299.00,50,0)")
        cursor.execute("insert into winter values(17,'Illumine','Juniper berry, Tobacco','Maroon','Medium',699.00,50,0)")
        cursor.execute("insert into winter values(18,'Illumine','Juniper berry, Tobacco','Maroon','Large',699.00,50,0)")
        mycon.commit()

def fall():
        cursor.execute("create table fall(pnum int,product varchar(30),scent varchar(20),colour varchar(20),size varchar(10),price float,quantity int,purchased int)")
        cursor.execute("insert into fall values(01,'Pumpkin Spice','pumpkin','orange','Small',299.00,50,0)")
        cursor.execute("insert into fall values(02,'Pumpkin Spice','pumpkin','orange','Medium',499.00,50,0)")
        cursor.execute("insert into fall values(03,'Pumpkin Spice','pumpkin','orange','Large',699.00,50,0)")
        cursor.execute("insert into fall values(04,'Mahogany apple','Red Mahogany','lime','Small',299.00,50,0)")
        cursor.execute("insert into fall values(05,'Mahogany apple','Red Mahogany','lime','Medium',499.00,50,0)")
        cursor.execute("insert into fall values(06,'Mahogany apple','Red Mahogany','lime','Large',699.00,50,0)")
        cursor.execute("insert into fall values(07,'Leaves','Clove Mint','Sap green','Small',299.00,50,0)")
        cursor.execute("insert into fall values(08,'Leaves','Clove Mint','Sap green','Medium',499.00,50,0)")
        cursor.execute("insert into fall values(09,'Leaves','Clove Mint','Sap green','Large',699.00,50,0)")
        cursor.execute("insert into fall values(10,'Champagne Toast','Vanilla','White','Small',299.00,50,0)")
        cursor.execute("insert into fall values(11,'Champagne Toast','Vanilla','White','Medium',499.00,50,0)")
        cursor.execute("insert into fall values(12,'Champagne Toast','Vanilla','White','Large',699.00,50,0)")
        mycon.commit()

def summer():
        cursor.execute("create table summer(pnum int,product varchar(30),scent varchar(20),colour varchar(20),size varchar(10),price float,quantity int,purchased int)")
        cursor.execute("insert into summer values(01,'Iced dragonfruit tea','Tropical dragonfruit','White','Small',299.00,50,0)")
        cursor.execute("insert into summer values(02,'Iced dragonfruit tea','Tropical dragonfruit','White','Medium',499.00,50,0)")
        cursor.execute("insert into summer values(03,'Iced dragonfruit tea','Tropical dragonfruit','White','Large',699.00,50,0)")
        cursor.execute("insert into summer values(04,'Watermelon Lemonade','Sugared Lemon','Crimson','Small',299.00,50,0)")
        cursor.execute("insert into summer values(05,'Watermelon Lemonade','Sugared Lemon','Crimson','Medium',499.00,50,0)")
        cursor.execute("insert into summer values(06,'Watermelon Lemonade','Sugared Lemon','Crimson','Large',699.00,50,0)")
        cursor.execute("insert into summer values(07,'Sunrise Woods','Sandalwood','Light orange','Small',299.00,50,0)")
        cursor.execute("insert into summer values(08,'Sunrise Woods','Sandalwood','Light orange','Medium',499.00,50,0)")
        cursor.execute("insert into summer values(09,'Sunrise Woods','Sandalwood','Light orange','Large',699.00,50,0)")
        cursor.execute("insert into summer values(10,'Summertime smores','Chocolate','Black','Small',299.00,50,0)")
        cursor.execute("insert into summer values(11,'Summertime smores','Chocolate','Black','Medium',499.00,50,0)")
        cursor.execute("insert into summer values(12,'Summertime smores','Chocolate','Black','Large',699.00,50,0)")
        mycon.commit()

def spring():
        cursor.execute("create table spring(pnum int,product varchar(30),scent varchar(25),colour varchar(20),size varchar(10),price float,quantity int,purchased int)")
        cursor.execute("insert into spring values(01,'Cucumber and lily','Lily','Light green','Small',299.00,50,0)")
        cursor.execute("insert into spring values(02,'Cucumber and lily','Lily','Light green','Medium',499.00,50,0)")
        cursor.execute("insert into spring values(03,'Cucumber and lily','Lily','Light green','Large',699.00,50,0)")
        cursor.execute("insert into spring values(04,'Rose water & ivy','Rose','Pink','Small',299.00,50,0)")
        cursor.execute("insert into spring values(05,'Rose water & ivy','Rose','Pink','Medium',499.00,50,0)")
        cursor.execute("insert into spring values(06,'Rose water & ivy','Rose','Pink','Large',699.00,50,0)")
        cursor.execute("insert into spring values(07,'Georgia Peach','Floral peach blossom','Vibrant orange','Small',299.00,50,0)")
        cursor.execute("insert into spring values(08,'Georgia Peach','Floral peach blossom','Vibrant orange','Medium',499.00,50,0)")
        cursor.execute("insert into spring values(09,'Georgia Peach','Floral peach blossom','Vibrant orange','Large',699.00,50,0)")
        cursor.execute("insert into spring values(10,'Black cherry','Cherry','Red','Small',299.00,50,0)")
        cursor.execute("insert into spring values(11,'Black cherry','Cherry','Red','Medium',499.00,50,0)")
        cursor.execute("insert into spring values(12,'Black cherry','Cherry','Red','Large',699.00,50,0)")
        mycon.commit()

def add():
    n=int(input("Enter product number:"))
    p=input("Enter product:")
    s=input("Enter scent:")
    c=input("Enter colour:")
    si=input("Enter size:")
    pr=float(input("Enter price:"))
    q=int(input("Enter Stock Quantity:"))
    so=int(input('Enter Stock Sold:'))
    if td in winter_l:
      cursor.execute("insert into winter values({},'{}','{}','{}','{}',{},{},{})".format(n,p,s,c,si,pr,q,so))
    elif td in autumn_l:
      cursor.execute("insert into fall values({},'{}','{}','{}','{}',{},{},{})".format(n,p,s,c,si,pr,q,so))
    elif td in summer_l:
      cursor.execute("insert into summer values({},'{}','{}','{}','{}',{},{},{})".format(n,p,s,c,si,pr,q,so))
    else:
      cursor.execute("insert into spring values({},'{}','{}','{}','{}',{},{},{})".format(n,p,s,c,si,pr,q,so))
    mycon.commit()
    print("Added Successfully.")
    
def delete():
    pn=int(input("Enter product number to be deleted: "))
    if td in winter_l:
        cursor.execute("select pnum from winter")
    elif td in autumn_l:
       cursor.execute("select pnum from fall")
    elif td in summer_l:
        cursor.execute("select pnum from summer")
    else:
        cursor.execute("select pnum from spring")
    data=cursor.fetchall()
    data=list(data)
    l=[]
    for i in data:
        n=int(i[0])
        l.append(n)
    if pn in l:
      if td in winter_l:
        cursor.execute("delete from winter where pnum='{}'".format(pn))
      elif td in autumn_l:
        cursor.execute("delete from fall where pnum='{}'".format(pn))
      elif td in summer_l:
        cursor.execute("delete from summer where pnum='{}'".format(pn))
      else:
        cursor.execute("delete from spring where pnum='{}'".format(pn))
      mycon.commit()
      print("Deleted Successfully.")
    else:
        print("Product with product no.",pn,"not found.")
        
def edit():
    pn=int(input("Enter product number:"))
    s=input("Enter scent:")
    c=input("Enter colour:")
    si=input("Enter size:")
    p=float(input("Enter price:"))
    q=int(input("Enter stock quantity:"))
    if td in winter_l:
      cursor.execute("update winter set scent='{}',price={},size='{}',colour='{}',quantity={} where pnum={}".format(s,p,si,c,q,pn))
    elif td in autumn_l:
      cursor.execute("update fall set scent='{}',price={},size='{}',colour='{}',quantity={} where pnum={}".format(s,p,si,c,q,pn))
    elif td in summer_l:
      cursor.execute("update summer set scent='{}',price={},size='{}',colour='{}',quantity={} where pnum={}".format(s,p,si,c,q,pn))
    else:
      cursor.execute("update spring set scent='{}',price={},size='{}',colour='{}',quantity={} where pnum={}".format(s,p,si,c,q,pn))
    mycon.commit()
    print("Updated successfully.")

def wishlist():
        c=0
        el=[]
        f1=open("wish.csv","w",newline='')
        w=csv.writer(f1)
        pn=int(input("Enter Retail number of product: "))
        todays_date = date.today()
        winter_l=[11,12,1]
        spring_l=[2,3,4]     
        summer_l=[5,6,7]
        autumn_l=[8,9,10]
        td= todays_date.month
        if td in winter_l:
          cursor.execute("select * from winter where pnum={}".format(pn))
        elif td in autumn_l:
          cursor.execute("select * from fall where pnum={}".format(pn))
        elif td in summer_l:
          cursor.execute("select * from summer where pnum={}".format(pn))
        else:
          cursor.execute("select * from spring where pnum={}".format(pn))
        dwish=cursor.fetchall()
        ind=usernames.index(username)
        name=names[ind]
        for i in dwish:
            el.append(i)
        d[name]=el
        w.writerow(d)  
        f1.close()
        f2=open("wish.csv","r",newline='')
        r=csv.reader(f2)
        for rec in r:
            k=d.keys()
            for v in k:
                if v==name:
                    for x in d[v]:
                        print('Item:',x[1],",",'Price:',x[5])
                        c+=1
        f2.close()
        print(c,"items in wishlist")
d={}        
def buy():
      l=[]
      ind=usernames.index(username)
      name=names[ind]
      f2=open("wish.csv","r",newline='')
      r=csv.reader(f2)
      k=d.keys()
      for rec in r:
            k=d.keys()
            for v in k:
                if v==name:
                    for x in d[v]:
                        print('Product No.:',x[0],',','Item:',x[1],",",'Price:',x[5])
                        l.append(x)
      f2.close()
      pn=int(input("Enter Product to transfer to cart:"))
      for i in l:
          if pn==i[0]:
              var=i
              l.remove(i)
      f1=open("wish.csv","w",newline='')
      w=csv.writer(f1)
      w.writerows(l)
      f1.close()
      return var

def buy_wish(bill2):
    random_id = random.randrange(10000,99999)
    ind=usernames.index(username)
    add=addresses[ind]
    n=names[ind]
    total=0
    tax=0
    amt=0
    for i in range(len(bill2)):
        total+=(bill2[i][5])
    tax=total*0.13
    rtax=round(tax,2)
    amt=rtax+total
    a=input("Do you have a voucher?(Yes/No)")
    if a=="Yes":
        x=input("Enter voucher code:")
        print()
        if x=="Clover10":
          amt=0.9*amt
          d="10% discount applied"
        else:
          print("Voucher",x,"doesn't exist!")
          d=''
    else:
        d=''
    print("Processing...")
    print()
    time.sleep(2)
    print('*********************** Lavender West ***********************')
    print('                            Invoice                                ')
    print('Date: ',date.today())
    print('Purchase ID:', random_id)
    for i in bill2:
        print('Item:',i[1],'₹',i[5])
    print('Amount:₹', total)
    print('Tax:   ₹', rtax)
    print('TOTAL: ₹', amt)
    print(d)
    print('*'*67)
    print('                         Payment Successful')
    print()
    print('To be received by: ',n)
    print('\nHow do you wish to collect your items?\n\n1. By courier delivery \n2. By in-store pickup')
    choice= int(input('\nI wish to collect by (1/2): '))
    if choice==1:
            print("Order will be delivered to Address:",add)
    elif choice==2:
            print("Please make sure to carry a printed or digital copy of the bill for in-store pickup")
    time.sleep(2)
    type('\nThank you for servicing with Lavender West & Co.!\n')
    
def cust():
  main.destroy()
  
def type(str): #function to type words
  for letter in str:
        print(letter,end='')
        sys.stdout.flush()
        time.sleep(0.05)
       
def adm():
  main.destroy()
  print('\n')
  print()
  f=input('Enter Username:')
  g=input('Enter Password:')
  if f=="Admin" and g=="123456":
      messagebox.showinfo('Login', 'Welcome Back Admin')
      while True:
          print("\n1. Add\n2. Delete\n3. Edit\n4. Display\n5. Exit")
          ch=int(input("Enter choice:"))
          if ch==1:
              add()
          elif ch==2:
              delete()
          elif ch==3:
              edit()
          elif ch==4:
              display()
          else:
              print('Redirecting to Customer Menu to exit')
              break
      
  else:
      print("Invalid Username/Password!!")
      messagebox.showinfo('Redirecting','Redirecting to Customer Menu')

def get_response(user_input):
    split_msg=re.split(r'\s+|[,:;?!.$-]\s*',user_input.lower())  # r used to make it a raw string,here we check for spaces and punctuation 
    response=check_msgs(split_msg)   # check_msgs is another fn.
    return response

def msg_probability(user_msg,recognised_words,single_response=False,req_words=[]):
    msg_certainity=0
    has_req_words=True
    
    for word in user_msg:
        if word in recognised_words:
            msg_certainity+=1
            
    percentage=float(msg_certainity)/float(len(recognised_words)) #calculates the % of recognised words in the user msg

    for word in req_words:
        if word not in user_msg:
            has_req_words=False
            break
        
    if has_req_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_msgs(msg):
    highest_probability_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_probability_list
        highest_probability_list[bot_response]=msg_probability(msg,list_of_words,single_response,required_words)
    
    #Responses--------------------------------------------------------------------------------------
        
    response('Items can be returned within 30 days of purchase if they have not been already used.',['what','is','your','return','policy','can','i','return','my','order'],required_words=['return'])
    response('To return your item please call custumer service at :9567224466 ',['how','to','return','my','candle','item','can','i'],required_words=['how','return'])
    response('Orders take 5-7 business days to arrive depending on you location.',['when','will','my','order','arrive','reach'],required_words=['when'])
    response('We are currently selling our products in the Indian Subcontinent only.',['can','do','you','ship','deliver','to','america','india','asia','australia','africa','europe','where','which'],required_words=['ship','to'])
    response('Hello!',['hey','hi','hello','sup','wassup'],single_response=True)
    response('See You Later',['bye','byebye','see you later','buhbye','goodbye'],single_response=True)

    #------------------------------------------------------------------------------------------------

    best_match=max(highest_probability_list,key=highest_probability_list.get)
    # this returns the highest probable response if 2 different response based keywords are recognised

    if highest_probability_list[best_match]<1:
        return unknown()
    else:
        return best_match

def unknown():
    response=['Could you rephrase that ?','I wonder...','...','What does that mean ?','I do not understand ...'][random.randrange(5)]
    return response


#colours
co1 = "white"
co2 = "black"
co3 = "#6074FF"
def login():
    global e_name
    global e_password
    global frame_up
    global frame_down

    window = Tk()
    window.title("Lavender West & Co.")
    window.geometry('310x300')
    window.resizable(0,0)
    window.configure(bg=co1)

    frame_up = Frame(window, width=310, height=50, bg=co1)
    frame_up.grid(row=0, column=0)

    frame_down = Frame(window, width=310, height=300, bg=co1)
    frame_down.grid(row=1, column=0)

    #frame_up widgets
    heading = Label(frame_up, text = "LOGIN", bg = co1, font=('Poppins 23'))
    heading.place(x=5, y=5)
    line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
    line.place(x=10, y=45)

    #frame_down widgets

    user = Label(frame_down, text="Username:", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
    user.place(x=10, y=10)
    e_name = Entry(frame_down, width=25, justify='left', font=("", 15), highlightthickness=1)
    e_name.place(x=14, y=48)

    password = Label(frame_down, text="Password:", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
    password.place(x=10, y=95)
    e_password = Entry(frame_down, width=25, justify='left',show = '*', font=("", 15), highlightthickness=1)
    e_password.place(x=14, y=130)

    #button

    button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"), command=check_password)
    button_confirm.place(x=15, y=180)

    window.mainloop()

def check_password():
    global username
    username = str(e_name.get())
    password = str(e_password.get())
    if username not in usernames:
        messagebox.showwarning('Error', 'Invalid username or password\nDidn\'t register yet?Sign Up!')

    elif password==passwords[usernames.index(username)]:
        messagebox.showinfo('Login', 'Welcome Back ' + names[usernames.index(username)])
        
def Payment(bill2,bill):
    random_id = random.randrange(10000,99999)
    ind=usernames.index(username)
    add=addresses[ind]
    n=names[ind]
    total=0
    tax=0
    amt=0
    for i in range(len(bill2)):
        total+=(bill2[i][0][1]*bill[i][1])
    tax=total*0.13
    rtax=round(tax,2)
    amt=rtax+total
    a=input("Do you have a voucher?(Yes/No)")
    if a=="Yes":
        x=input("Enter voucher code:")
        print()
        if x=="Clover10":
          amt=0.9*amt
          d="10% discount applied"
        else:
          print("Voucher",x,"doesn't exist!")
          d=''
    else:
        d=''
    print("Processing...")
    print()
    time.sleep(2)
    print('*********************** Lavender West ***********************')
    print('                            Invoice                                ')
    print('Date: ',date.today())
    print('Purchase ID:', random_id)
    for i in range(len(bill2)):
        print('Item:',bill2[i][0][0],'₹',bill2[i][0][1],'Qty:',bill[i][1])
    print('Amount:₹', total)
    print('Tax:   ₹', rtax)
    print('TOTAL: ₹', amt)
    print(d)
    print('*'*67)
    print('                         Payment Successful')
    print()
    print('To be received by: ',n)
    print('\nHow do you wish to collect your items?\n\n1. By courier delivery \n2. By in-store pickup')
    choice= int(input('\nI wish to collect by (1/2): '))
    if choice==1:
            print("Order will be delivered to Address:",add)
    elif choice==2:
            print("Please make sure to carry a printed or digital copy of the bill for in-store pickup")
    time.sleep(2)
    type('\nThank you for servicing with Lavender West & Co.!\n')
    

def luckydraw(): #function for lucky draw
  print('-'*10)
  print('Lucky Draw')
  print('-'*10)
  myenter = int(input('\nInsert an integer from 1 to 10: '))
  print('\nThe system is choosing a number. This shall not take more than  a minute.\nChoosing number....\n')
  
  for i in range(4,-1,-1):
    i += 1
    print(i, 'seconds more')
    time.sleep(0.5)

  randomize = random.randrange(1,11)
  print(f"\nThe number chosen by the system is {randomize}!")
  
  if randomize == myenter:
    print('\nYay you won! Your reward is a 10% discount voucher! Use it while you shop online with us!.')
    return True
    print('\nVoucher: 10% discount on all items. No min spend required.')

    
  else:
    print("\nIt's okay! Better luck next time!")
    return False
         
winter()
summer()
spring()
fall()
def register():
    global vars
    global frame_up
    global name
    global phno
    global mail
    global usern
    global pass1
    global pass2
    global address

    base = Tk()  
    base.geometry("500x500")  
    base.title("Lavender West & Co.")
    phno=StringVar()
    name= StringVar()
    usern= StringVar()
    mail= StringVar()
    address= StringVar()
    pass1= StringVar()
    pass2= StringVar()

    frame_up = Frame(base, width=310, height=50, bg='white')
    frame_up.grid(row=0, column=0)

    heading = Label(frame_up, text = "REGISTER", bg ='white', font=('Poppins 23'))
    heading.place(x=5, y=5)
    line = Label(frame_up, width=40, text="", height=1, bg="#6074FF", anchor=NW)
    line.place(x=10, y=45)
    
    lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
    lb1.place(x=20, y=80)
    en1= Entry(base,textvariable = name)  
    en1.place(x=200, y=80)

    lb2= Label(base, text="Enter Username", width=15, font=("arial",12))  
    lb2.place(x=20, y=120)
    en2= Entry(base,textvariable = usern)  
    en2.place(x=200, y=120)
      
    lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
    lb3.place(x=19, y=160)
    en3= Entry(base,textvariable = mail)  
    en3.place(x=200, y=160)  
      
    lb4= Label(base, text="Contact Number", width=13,font=("arial",12))  
    lb4.place(x=19, y=200)
    en4= Entry(base,textvariable = phno)  
    en4.place(x=200, y=200)
      
    lb5= Label(base, text="Select Gender", width=15, font=("arial",12))  
    lb5.place(x=5, y=240)  
    vars = [] 
    Radiobutton(base, text="Male", padx=5,variable=vars, value=[1]).place(x=180, y=240)  
    Radiobutton(base, text="Female", padx =10,variable=vars, value=[2]).place(x=240,y=240)  
    Radiobutton(base, text="others", padx=15, variable=vars, value=[3]).place(x=310,y=240)

    lb8= Label(base, text="Address", width=13,font=("arial",12))  
    lb8.place(x=19, y=280)
    en8= Entry(base,textvariable = address)  
    en8.place(x=200, y=280)
      
    lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
    lb6.place(x=19, y=320)
    en6= Entry(base, show='*',textvariable = pass1)  
    en6.place(x=200, y=320)  
      
    lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
    lb7.place(x=21, y=360)
    e_password = Entry(base, show='*',textvariable = pass2)
    e_password.place(x=200, y=360)  
 
    button_confirm = Button(base, text="Register", bg="#6074FF", fg='White', width=39, height=2, font=("Ivy 9 bold"), command=check)
    button_confirm.place(x=200, y=400)  
    base.mainloop()
    
def check():
    global n
    global un
    global a
    global m
    global pn
    global p1
    global p2
    n=name.get()
    un=usern.get()
    m=mail.get()
    pn=phno.get()
    a=address.get()
    p1=pass1.get()
    p2=pass2.get()
    if n!='' and un!='' and m!='' and pn!='' and a!='' and p1!='' and p2!='' and vars!=0:
        register1()
    else:
        messagebox.showwarning('Error','Please fill all fields before proceeding!') 
        
def register1():
  q=0
  names.append(n)
  phnos.append(pn)
  if un not in usernames:
    q+=1
  else:
    messagebox.showwarning('Error','Username taken!\nTry a new variation.')
  if '@gmail.com' not in m:
    messagebox.showwarning('Error','Enter a valid mail-id!')
  else:
    q+=1
  if q==2:
    passwd()
    
def passwd():
  if p1 == p2:
    usernames.append(un)
    addresses.append(a)
    mails.append(m)
    passwords.append(p1)
    messagebox.showinfo('Login','Proceed to Login!')
    print()
    print("DETAILS:")
    print('Name:',n)
    print('Username:',un)
    print('Emial:',m)
    print('Phno:',pn)
    print('Address:',a)
    
  else:
    messagebox.showwarning('Error', 'Re-Enter Password doesn\'t match entered Password.\n Retry!')

def cart():
    global bill2
    global bill
    global it
    op=int(input('Enter Retail no. of product to add to cart: '))
    q=int(input("Quantity:"))
    if td in winter_l:
      cursor.execute("select product,price,quantity from winter where pnum={}".format(op))
    elif td in autumn_l:
      cursor.execute("select product,price,quantity from fall where pnum={}".format(op))
    elif td in summer_l:
      cursor.execute("select product,price,quantity from summer where pnum={}".format(op))
    else:
      cursor.execute("select product,price,quantity from shop where pnum={}".format(op))
    data1 = cursor.fetchall()#was written cursor.fetchone
    data=data1[0][0]
    quantity=data1[0][2]
    if quantity==0:
      print("No Items Left.")
    else:
      bill2.append(data1)
      bill.append((data,q))
      it+=q
      if td in winter_l:
        cursor.execute("update winter set quantity=quantity-{} where pnum='{}'".format(q,op))
        cursor.execute("update winter set purchased=purchased+{} where pnum='{}'".format(q,op))
      elif td in autumn_l:
        cursor.execute("update fall set quantity=quantity-{} where pnum='{}'".format(q,op))
        cursor.execute("update fall set purchased=purchased+{} where pnum='{}'".format(q,op))
      elif td in summer_l:
        cursor.execute("update summer set quantity=quantity-{} where pnum='{}'".format(q,op))
        cursor.execute("update summer set purchased=purchased+{} where pnum='{}'".format(q,op))
      else:
        cursor.execute("update spring set quantity=quantity-{} where pnum='{}'".format(q,op))
        cursor.execute("update spring set purchased=purchased+{} where pnum='{}'".format(q,op))


"""
print('                                      |===============|\n                                      | LAVENDER WEST | \n                                      |===============|')
time.sleep(1)
print('                                     ',end='')
type("Style With Fragrence")
print('')
print('                                 ',end='')
"""
type('Welcome to Lavender West & Co.')

main=Tk()
main.geometry("1366x932")
main.title("Lavender West & Co.")
main.resizable(0,0)

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

label1=Label(main)
label1.place(relx=0, rely=0, width=1366, height=943)
img=PhotoImage(file=r"C:\Users\vicky\OneDrive\Documents\Diya\main pic.png")
label1.configure(image=img)

button1=Button(main)
button1.place(relx=0.5, rely=0.55, width=100, height=100)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file=r"C:\Users\vicky\OneDrive\Documents\Diya\12th projects\emp.png")#change
button1.configure(image=img2)
button1.configure(command=cust)

button2=Button(main)
button2.place(relx=0.5, rely=0.7, width=100, height=100)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file=r"C:\Users\vicky\OneDrive\Documents\Diya\12th projects\admin.png")#change
button2.configure(image=img3)
button2.configure(command=adm)

main.mainloop()

while True:
    print()
    print('Main Menu:')
    print("1. Begin Shopping\n2. Lucky Draw\n3. Customer Support\n4. Access Admin Interface\n5. Exit")
    cha=int(input("Enter choice:"))
    if cha==1:
        xx=""
        while True:
            print()
            xx=input("1. Sign Up\n2. Login and Shop\n3. Back to Main Menu...\nEnter choice:")
            if xx=="1":
                register()
            elif xx=="2":
                login()
                el=[]
                y=True
                if y:
                    print()
                    print()
                    display()
                    it=0
                    print()
                    bill2=[]
                    bill=[]
                    while True:
                      cho=int(input("\n1. Add to cart\n2. Show cart\n3. Delete from cart\n4. Wishlist\n5. Back to Log-in menu... \nEnter your choice:"))
                      print()
                      if cho==1:
                          cart()
                          print(it,r"item/s in cart.")  
                          y=int(input(" Press 1: To procced to checkout\n Press 2: To continue shopping\n Enter Choice:"))
                          if y==1:
                              if bill==[]:
                                  print("Cart Empty.")
                              else:
                                  Payment(bill2,bill)
                                  break
                          elif y==2:
                              continue
                      elif cho==2:
                          print("Cart:")
                          for i in bill:
                              print("Item:",i[0],', Quantity:',i[1])
                      elif cho==3:
                          print("Cart:")
                          for i in range(len(bill2)):
                              print('Item:',bill2[i][0][0],'₹',bill2[i][0][1],'Qty:',bill[i][1])
                          print()
                          el=input('Enter Product Name to delete product:')
                          for i in bill:
                              if el==i[0]:
                                  z=bill.index(i)
                                  bill.remove(i) 
                          bill2.pop(z)
                          print()
                          print("Cart:")
                          for i in range(len(bill2)):
                              print('Item:',bill2[i][0][0],'₹',bill2[i][0][1],'Qty:',bill[i][1])
                          print('Deleted Successfully.')
                      elif cho==4:
                        while True:
                          xo=int(input("\n1. Add to wishlist\n2. Proceed to payment\n3. Back to cart...\nEnter Choice:"))
                          if xo==1:
                              wishlist()
                          elif xo==2:
                              t=buy()
                              print(t)
                              bill2.append(t)
                              buy_wish(bill2)
                          else:
                              break
                        
                      elif cho==5:
                              break
                              
                              

            elif xx=="3":
                break
    elif cha==2:
           f=luckydraw()
           if f:
                   print("Voucher code: Clover10")
        
    elif cha==3:
        print()
        print()
        print("FAQ\'S :")
        print('1. What is your return policy?')
        print('2. How to return my item?')
        print('3. Do you ship to ...?')
        print('4. When will my order arrive?')
        print('Enter Bye to Exit.')
        print()
        O='Yes'
        while O=='Yes':
            a=get_response(input('You:'))
            print('Bot:'+ a)
            print()
            if a=="See You Later":
                    break
    elif cha==4:
        print()
        f=input("Enter Username:")
        g=input("enter password:")
        if f=="Admin" and g=="123456":
                print('Welcome back Admin')
                while True:
                        print("\n1.Add\n2.Delete\n3.Edit\n4.Display\n5.Exit")
                        ch=int(input('Enter choice:'))
                        if ch==1:
                                add()
                        elif ch==2:
                                delete()
                        elif ch==3:
                                edit()
                        elif ch==4:
                                display()
                        else:
                                print('Redirecting to Customer Menu to exit') 
                                break
                
        else:
                print("Invalid Username/Password!!")
                print('Redirecting','Redirecting to Customer')
    elif cha==5:
           break
