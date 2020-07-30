from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
import os
import csv
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import Color, black, blue, red
import mysql.connector
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Rect
#from reportlab.lib.colors import Color, black, blue, red
from reportlab.lib.units import inch
import datetime
import pyqrcode 
import png 
from pyqrcode import QRCode 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


root=Tk()
width_window=1000
height_window=500
width1=root.winfo_screenwidth()
height1=root.winfo_screenheight()
x_cordinate=(width1/2)-(width_window/2)
y_cordinate=(height1/2)-(height_window/1.4)
root.geometry("%dx%d+%d+%d" % (width1/1.5,height1/1.2,x_cordinate,y_cordinate))
root.resizable(0,0)
root.title("Id Gen")
#database connectivity
hostname="127.0.0.1"
username='root'
passward='0089'
databasename='arshdb'

imagepath=StringVar()
Name=StringVar()
fname2=StringVar()
mname2=StringVar()
D_O_B=StringVar()
Registration_no=StringVar()
#Designation=StringVar()
var=StringVar()
Mobile_no=StringVar()
Email_id=StringVar()
joindate1=StringVar()
qrlink=StringVar()
Name1=StringVar()

def empty():
    imagepath.set("")
    Name.set("")
    fname2.set("")
    mname2.set("")
    D_O_B.set("")
    Registration_no.set("")    
    var.set("")
    Mobile_no.set("")
    Email_id.set("")
    joindate1.set("")
    deg_box.set('')
    qual_box.set('')
    addr_entry.delete(1.0,END)



def select_image():
    global result
    global path1
    global path2
    global path3
    global i
    global j

    result= filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    i = result.rfind("/")
    # j=result.rfind(".")
    # path1 =result[:i+1]
    path2 = result[i + 1:]
    # path3= result[j:]
    photo_entry=imagepath.set(path2)





def calander():
    def print_sel():
        D_O_B.set(cal.selection_get())
        top.destroy()
    top = Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def calander1():
    def print_sel():
        joindate1.set(cal.selection_get())
        top.destroy()
    top = Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()



def write_file(data):
    # Convert binary data to proper format and write it on Hard Disk
    with open("photo/"+regno+".jpg", 'wb') as file:
        file.write(data)



def qrpdf():
    c=canvas.Canvas(regno+ ' ' + name1+".pdf")
    c.setTitle("documentTitle")
    d = datetime.datetime.now()
    cd=d.strftime("%Y-%m-%d")
    pdfmetrics.registerFont(TTFont('Vera', 'Sabatons Script DEMO.ttf'))
    c.setFont('Vera', 32)
    c.rect(0.15*inch,0.5*inch,8*inch,10.5*inch, fill=0)
    c.setFillColorRGB(0, 0.252,0.842)
    c.rect(0.15*inch,9.5*inch,8*inch,1.5*inch, fill=1)
    c.setFillColorRGB(0,0,0)
    c.setFont('Vera', 74)
    c.drawString(1.5*inch,10.3*inch,"Samarpan")
    c.setFont('Vera', 50)
    c.setFillColor("yellow")
    c.drawString(3.5*inch,9.7*inch,"ek nayi pahal")
    image="img2.png"
    c.drawImage(image,5.2*inch,10.1*inch,width=50,height=50)
    c.setFillColorRGB(0,0,0)
    c.setFont('Helvetica-Oblique', 16)

    c.drawString(1.1*inch,6.8*inch,"Gender :   "+ var1)
    c.drawString(1.1*inch,7.1*inch,"D.O.B :   "+ str(dateofbirth1))
    #c.drawString(140,595,name)
    c.drawString(1.1*inch,6.5*inch,"join Date :   "+ str(jdate1))
    c.drawString(1.1*inch,6.2*inch,"Registration date :   "+  str(cd))
    c.drawString(1.1*inch,5.9*inch,"Registration no :   "+ regno)
    c.drawString(1.1*inch,5.6*inch,"Mob :   "+ mobno)
    c.drawString(1.1*inch,5.3*inch,'Email Id :   '+ mail)
    c.drawString(1.1*inch,7.7*inch,'Father Name :    '+ fname1)
    c.drawString(1.1*inch,7.4*inch,'Mother Name :    '+ mname1)

    c.setFont('Helvetica-Oblique', 22)
    c.drawString(6*inch,1*inch,'Department')


    c.setFont('Helvetica-Oblique', 22)
    c.drawString(1.1*inch,8.5*inch,name1)

    c.setFont('Helvetica-Oblique', 16)
    c.drawString(1.1*inch,8*inch,"Designation :   "+ deg1)
    image="photo/"+regno+".jpg"
    c.drawInlineImage(image,6*inch,7.2*inch,width=100,height=120)
    c.save()



def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb', buffering=0) as file:
        binaryData = file.read()
    return binaryData


#for submit informatio


def submit_info():
    global regno
    global deg1
    global name1
    global fname1
    global mname1
    global dateofbirth1
    global jdate1
    global addr
    global var1
    global mobno
    global qual1
    global mail
    img=imagepath.get()
    name1=Name.get()
    name1=name1.title()
    fname1=fname2.get()
    fname1=fname1.title()
    mname1=mname2.get()
    mname1=mname1.title()
    dateofbirth1=D_O_B.get()
    regno=Registration_no.get()
    deg1=deg_box.get()
    jdate1=joindate1.get()    
    addr=addr_entry.get('1.0',END)
    var1=var.get()
    mobno=Mobile_no.get()
    qual1=qual_box.get()
    mail=Email_id.get()
    
    if name1!='':
        if fname1!='':
            if mname1!='':
                if deg1!='':
                    if dateofbirth1!='':
                        if regno!='' :
                            if var!='':
                                if mobno.isdigit() and len(mobno)==10 :
                                    if mail.endswith("@gmail.com"):
                                        if deg1 == "Student":
                                            try:
                                                mydb=mysql.connector.connect(host=hostname,user=username,passwd=passward,database=databasename,auth_plugin='mysql_native_password')
                                                if(mysql):
                                                    print("connection successful")
                                                else:
                                                    print("connection unsuccessful")
                                                mycursor=mydb.cursor()                                               

                                                photo=convertToBinaryData(result)                                                
                                                msg=messagebox.showinfo("Confirmation","Do You Want To Save It..")
                                                if msg=="ok":                                        
                                                    data="insert into student(RegistrationNO,Name,FatherName,MotherName,Designation,DateOfBirth,Gender,ContactNo,Email,Joindate,Address,Qualification,profilepic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                    records=[(regno,name1,fname1,mname1,deg1,dateofbirth1,var1,mobno,mail,jdate1,addr,qual1,photo)]
                                                    mycursor.executemany(data,records)
                                                    mydb.commit()  
                                                    write_file(photo)                                                  
                                                    qrpdf() 
                                                    gauth = GoogleAuth()
                                                    # Create local webserver and auto handles authentication.
                                                    gauth.LocalWebserverAuth()                                               
                                                    # Create GoogleDrive instance with authenticated GoogleAuth instance.
                                                    drive = GoogleDrive(gauth)
                                                    #Create GoogleDriveFile instance with title 'Hello.txt'.
                                                    file1 = drive.CreateFile({"title":regno+ ' ' + name1+".PDF"})
                                                    #file1.SetContentString('Hello World ! My name is md arshad ali')
                                                    file1.SetContentFile(regno+ ' ' + name1+".pdf")
                                                    file1.Upload() # Upload the file.
                                                    messagebox.showinfo("Confirmation","Registration Successfull")
                                                    empty()
                                            except mysql.connector.DatabaseError as e:
                                                if mydb:
                                                    mydb.rollback()                                           
                                                if 'Duplicate entry' in str(e):
                                                    messagebox.showerror("Opps","Registration No. already present")
                                                else:
                                                    messagebox.showerror("Opps","Connection Error")
                                                    print(e)
                                            finally:
                                                if mycursor:
                                                    mycursor.close()
                                                if mydb:
                                                    mydb.close()
                                            
                                            
                                        elif deg1=="Teacher":
                                            try:
                                                mydb=mysql.connector.connect(host=hostname,user=username,passwd=passward,database=databasename,auth_plugin='mysql_native_password')
                                                if(mysql):
                                                    print("connection successful")
                                                else:
                                                    print("connection unsuccessful")
                                                mycursor=mydb.cursor()

                                                photo=convertToBinaryData(result)
                                                
                                                msg=messagebox.showinfo("Confirmation","Do You Want To Save It..")
                                            
                                                if msg=="ok":
                                                    data="insert into teacher(RegistrationNO,Name,FatherName,MotherName,Designation,DateOfBirth,Gender,ContactNo,Email,Joindate,Address,Qualification,profilepic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                    records=[(regno,name1,fname1,mname1,deg1,dateofbirth1,var1,mobno,mail,jdate1,addr,qual1,photo)]
                                                    mycursor.executemany(data,records)
                                                    mydb.commit()
                                                    write_file(photo)
                                                    qrpdf()
                                                    gauth = GoogleAuth()
                                                    # Create local webserver and auto handles authentication.
                                                    gauth.LocalWebserverAuth()                                               
                                                    # Create GoogleDrive instance with authenticated GoogleAuth instance.
                                                    drive = GoogleDrive(gauth)
                                                    #Create GoogleDriveFile instance with title 'Hello.txt'.
                                                    file1 = drive.CreateFile({"title":regno+ ' ' + name1+".PDF"})
                                                    #file1.SetContentString('Hello World ! My name is md arshad ali')
                                                    file1.SetContentFile(regno+ ' ' + name1+".pdf")
                                                    file1.Upload() # Upload the file.
                                                    messagebox.showinfo("Confirmation","Registration Successfull")
                                                    empty()                                                                            
                                            except mysql.connector.DatabaseError as e:
                                                if mydb:
                                                    mydb.rollback()
                                                    if e=='Duplicate entry' in str(e):
                                                        messagebox.showerror("Opps","Registration No. already present")
                                                    else:
                                                        messagebox.showerror("Opps","Connection Error")
                                            finally:
                                                if mycursor:
                                                    mycursor.close()
                                                if mydb:
                                                    mydb.close()                                        
                                        else:
                                            messagebox.showerror("Opps", "Please enter correct designation")
                                    else:
                                        messagebox.showerror("Opps","Invalid Email Id")
                                else:
                                    messagebox.showerror("Opps", "Invalid Mobile No.")
                            else:
                                messagebox.showerror("Opps", "Please select Gender")
                        else:
                            messagebox.showerror("Opps", "Please Enter Registration No. ")
                    else:
                        messagebox.showerror("Opps", "Please Enter Date of birth")
                else:
                    messagebox.showerror("Opps", "Please Enter Designation")
            else:
                messagebox.showerror("Opps", "Please Enter Mother name")
        else:
            messagebox.showerror("Opps", "Please Enter Father name")
    else:
        messagebox.showerror("Opps", "Please Enter name")




color="#c7f57d"
font="Candara"
#for Registration form
def registration_form():
    global deg_box
    global qual_box
    global addr_entry


    rframe=Frame(width=width1/1.5,height=height1/1.2,bg=color)
    rframe.place(x=0,y=0)

    registration_label=Label(rframe,text="Registration Form",font=("ALGERIAN",30,"bold"),fg="#1bb7f5",width=35)
    registration_label.place(x=0,y=0)

    name=Label(rframe,text="Name :",font=(font, 15),bg=color)
    name.place(x=200,y=80)
    name_entry=Entry(rframe,width=50,textvariable=Name)
    name_entry.place(x=380,y=87)

    fname = Label(rframe, text="Father Name :", font=(font, 15), bg=color)
    fname.place(x=200, y=113)
    fname_entry = Entry(rframe, width=50, textvariable=fname2)
    fname_entry.place(x=380, y=120)

    mname = Label(rframe, text="Mother Name :", font=(font, 15), bg=color)
    mname.place(x=200, y=147)
    mname_entry = Entry(rframe, width=50, textvariable=mname2)
    mname_entry.place(x=380, y=154)

    deg = Label(rframe, text="Designation :", font=(font, 15), bg=color)
    deg.place(x=200, y=180)
    designation=['Student','Teacher']
    deg_box = Combobox(rframe, width=47, values=designation)
    deg_box.place(x=380, y=187)

    dob = Label(rframe, text="Date of birth :", font=(font, 15), bg=color)
    dob.place(x=200, y=213)
    dob_entry = Entry(rframe, width=35,textvariable=D_O_B)
    dob_entry.place(x=380, y=220)
    dob_button = Button(rframe, text="Select", width=10, font=("Bootiquak An",7), command=calander)
    dob_button.place(x=600, y=220)


    regno = Label(rframe, text="Registration no. :", font=(font, 15), bg=color)
    regno.place(x=200, y=246)
    regno_entry = Entry(rframe, width=50,textvariable=Registration_no)
    regno_entry.place(x=380, y=253)

    gender = Label(rframe, text="Gender :", font=(font, 15), bg=color)
    gender.place(x=200, y=279)
    genderm=Radiobutton(rframe,text="Male", font=(font, 15), bg=color,variable=var,value="Male")
    genderm.place(x=380, y=279)
    genderf = Radiobutton(rframe, text="Female", font=(font, 15), bg=color,variable=var,value="Female")
    genderf.place(x=480, y=279)

    mobno = Label(rframe, text="Mobile no. :", font=(font, 15), bg=color)
    mobno.place(x=200, y=312)
    mobno_entry = Entry(rframe, width=50,textvariable=Mobile_no)
    mobno_entry.place(x=380, y=319)

    emailid= Label(rframe, text="Email Id :", font=(font, 15), bg=color)
    emailid.place(x=200, y=345)
    emailid_entry = Entry(rframe, width=50,textvariable=Email_id)
    emailid_entry.place(x=380, y=352)

    joindate = Label(rframe, text="Join date :", font=(font, 15), bg=color)
    joindate.place(x=200, y=378)
    joindate_entry = Entry(rframe, width=35, textvariable=joindate1)
    joindate_entry.place(x=380, y=385)
    join_button = Button(rframe, text="Select", width=10, font=("Bootiquak An",7), command=calander1)
    join_button.place(x=600, y=380)

    addr = Label(rframe, text="Address :", font=(font, 15,), bg=color)
    addr.place(x=200, y=411)

    
    
    addr_entry = Text(rframe, width=38,height=3,font=("Arial",11))
    addr_entry.place(x=380, y=418)    
    s=Scrollbar(addr_entry,cursor="arrow")
    s.place(x=290,y=0,height=53,width=15)
    addr_entry.config(yscrollcommand=s.set)    
    s.config(command=addr_entry.yview)

    qual = Label(rframe, text="Qualification :", font=(font, 15), bg=color)
    qual.place(x=200, y=477)
    qualification = ['Below 10th', '10th appearing',"11th appearing ","12th appearing","Engineering"]
    qual_box = Combobox(rframe, width=47, values=qualification)
    qual_box.place(x=380, y=484)


    photo = Label(rframe, text="Upload Image", font=(font, 15), bg=color)
    photo.place(x=200, y=510)
    photo_entry = Entry(rframe, width=30,textvariable=imagepath)
    photo_entry.place(x=380, y=517)
    photo_button = Button(rframe, text="Select", width=10, font=("Bootiquak An",7), command=select_image)
    photo_button.place(x=575, y=517)

    submit_button = Button(rframe, text="Submit", width=20, font=("Bootiquak An", 13), command=submit_info)
    submit_button.place(x=380, y=570)


    id_button = Button(rframe, text="Back",width=10, font=("Bootiquak An", 10),command=home)
    id_button.place(x=0, y=0)


def savaid():
    global current2
    current2=os.getcwd()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    current=root.filename
    i=current.rfind("/")
    current1=current[:i+1]   
    os.chdir(current1)
      





def qrgenerate():
    # String which represents the QR code 
    link=qrlink.get()    
        
    # Generate QR code 
    url = pyqrcode.create(link) 

    # # Create and save the svg file naming "myqr.svg" 
    #url.svg("myqr.svg", scale = 1) 

    # Create and save the png file naming "myqr.png" 
    url.png('myqr.png', scale = 2) 






def Create_id():
    global c
    link=qrlink.get()
    if link!='':
        d = datetime.datetime.now()
        cd=d.strftime("%Y-%m-%d")
        c=canvas.Canvas(Registration_no+" "+name1+"id card"+".pdf")
        c.setTitle("documentTitle")
        pdfmetrics.registerFont(TTFont('Vera', 'Sabatons Script DEMO.ttf'))
        c.setFont('Vera', 32)
        c.rect(0.2*inch,6*inch,3.38*inch,2.313*inch, fill=0)
        c.setFillColorRGB(0, 0.252,0.842)
        c.rect(0.2*inch,7.7*inch,3.38*inch,0.6*inch, fill=1)
        c.setFillColorRGB(0,0,0)
        c.setFont('Vera', 32)
        c.drawString(1.5*inch,8.0*inch,"Samarpan")
        c.setFont('Vera', 20)
        c.setFillColor("yellow")
        c.drawString(2.3*inch,7.76*inch,"ek nayi pahal")
        image="img2.png"
        c.drawImage(image,3.1*inch,7.9*inch,width=27,height=27)
        c.setFillColorRGB(0,0,0)
        c.setFont('Helvetica-Oblique', 7)

        c.drawString(0.3*inch,6.6*inch,"Gender:"+Gender)
        c.drawString(0.3*inch,6.45*inch,"D.O.B:"+str(D_O_B))
        #c.drawString(140,595,name)
        c.drawString(0.3*inch,6.3*inch,"Join date:"+str(joindate))
        c.drawString(0.3*inch,6.15*inch,"Issue date:"+str(cd))
        c.drawString(1.6*inch,6.6*inch,"Reg no:"+Registration_no)
        c.drawString(1.6*inch,6.45*inch,"Mob:"+ContactNo)
        c.drawString(1.6*inch,6.3*inch,Email)

        c.setFont('Helvetica-Oblique', 10)
        c.drawString(2.8*inch,6.1*inch,'Department')


        c.setFont('Helvetica-Oblique', 16)
        c.drawString(1.1*inch,7.4*inch,name1)

        c.setFont('Helvetica-Oblique', 12)
        c.drawString(1.3*inch,7.15*inch,Designation)

        #write_file(profilepic)
        image="photo/"+Registration_no+".jpg"
        c.drawInlineImage(image,0.3*inch,6.8*inch,width=50,height=60)
        qrgenerate()
        image='myqr.png'
        c.drawInlineImage(image,2.8*inch,6.8*inch,width=50,height=50)        
        savaid()
        c.save()                
        messagebox.showinfo("Congratulation","Id Card Create Successfully")
        os.chdir(current2)
    else:
        messagebox.showerror("Opps","Please Fill QR Link")


def searchid():
    global Registration_no
    global name1
    global D_O_B
    global ContactNo
    global Email
    global Designation
    global joindate
    global Gender
    global profilepic
    name=Name1.get()
    name=name.title()
    name=name.strip()
    regno=Name1.get()
    regno=regno.strip()
    deg2=deg_box3.get()
    if name!='':
        if deg2=="Student":  
            try:
                mydb=mysql.connector.connect(host=hostname,user=username,passwd=passward,database=databasename,auth_plugin='mysql_native_password')
                if(mysql):
                    print("connection successful")
                else:
                    print("connection unsuccessful")
                mycursor=mydb.cursor()                
                #photo=convertToBinaryData(result)
                mycursor.execute("select * from student") 
                data=mycursor.fetchall()                
                i="no"
                for item in data:
                   # for reg in item:
                        if name==item[1] or regno==item[0]:
                            Registration_no=item[0]
                            name1=item[1]
                            fname=item[2]
                            mname=item[3]
                            Designation=item[4]
                            D_O_B=item[5]
                            Gender=item[6]
                            ContactNo=item[7]
                            Email=item[8]
                            joindate=item[9]
                            address=item[10]
                            qualification=item[11]
                            profilepic=item[12]                           
                            i="yes"                                                                                        
            except mysql.connector.DatabaseError as e:
                if mydb:
                    mydb.rollback()
                    if e=='Duplicate entry' in str(e):
                        messagebox.showerror("Opps","Registration No. already present")
                    else:
                        messagebox.showerror("Opps","Connection Error")
            finally:
                if mycursor:
                    mycursor.close()
                if mydb:
                    mydb.close()         
        elif deg2=="Teacher":
            try:
                mydb=mysql.connector.connect(host=hostname,user=username,passwd=passward,database=databasename,auth_plugin='mysql_native_password')
                if(mysql):
                    print("connection successful")
                else:
                    print("connection unsuccessful")
                mycursor=mydb.cursor()
                #photo=convertToBinaryData(result)
                mycursor.execute("select * from teacher") 
                data=mycursor.fetchall()
                i="no"
                for item in data:
                   # for reg in item:
                        if name==item[1] or regno==item[0]:
                            Registration_no=item[0]
                            name1=item[1]
                            fname=item[2]
                            mname=item[3]
                            Designation=item[4]
                            D_O_B=item[5]
                            Gender=item[6]
                            ContactNo=item[7]
                            Email=item[8]
                            joindate=item[9]
                            address=item[10]
                            qualification=item[11]
                            profilepic=item[12] 
                            i="yes"                                                                                        
            except mysql.connector.DatabaseError as e:
                if mydb:
                    mydb.rollback()
                    if e=='Duplicate entry' in str(e):
                        messagebox.showerror("Opps","Registration No. already present")
                    else:
                        messagebox.showerror("Opps","Connection Error")
            finally:
                if mycursor:
                    mycursor.close()
                if mydb:
                    mydb.close()
        if i=="yes":
            dataframe=Frame(width=width1 / 1.5, height=height1/1.2, bg=color)
            dataframe.place(x=0,y=100)
            name = Label(dataframe, text="Name :", font=(font, 15), bg=color)
            name.place(x=200, y=40)
            name = Label(dataframe, text=name1, font=(font, 15), bg=color)
            name.place(x=400, y=40)

            fathername = Label(dataframe, text="Father Name :", font=(font, 15), bg=color)
            fathername.place(x=200, y=70)
            fathername = Label(dataframe, text=fname, font=(font, 15), bg=color)
            fathername.place(x=400, y=70)

            mothername = Label(dataframe, text="Mother Name :", font=(font, 15), bg=color)
            mothername.place(x=200, y=100)
            mothername = Label(dataframe, text=mname, font=(font, 15), bg=color)
            mothername.place(x=400, y=100)

            deg = Label(dataframe, text="Designation :", font=(font, 15), bg=color)
            deg.place(x=200, y=130)
            deg = Label(dataframe, text=Designation, font=(font, 15), bg=color)
            deg.place(x=400, y=130)

            dob = Label(dataframe, text="Date of birth :", font=(font, 15), bg=color)
            dob.place(x=200, y=160)
            dob = Label(dataframe, text=D_O_B, font=(font, 15), bg=color)
            dob.place(x=400, y=160)

            regno = Label(dataframe, text="Registration no. :", font=(font, 15), bg=color)
            regno.place(x=200, y=190)
            regno = Label(dataframe, text=Registration_no, font=(font, 15), bg=color)
            regno.place(x=400, y=190)

            mobno = Label(dataframe, text="Mobile no. :\t", font=(font, 15), bg=color)
            mobno.place(x=200, y=220)
            mobno = Label(dataframe, text=ContactNo, font=(font, 15), bg=color)
            mobno.place(x=400, y=220)

            gender = Label(dataframe, text="Gender :", font=(font, 15), bg=color)
            gender.place(x=200, y=250)
            gender = Label(dataframe, text=Gender, font=(font, 15), bg=color)
            gender.place(x=400, y=250)

            emailid = Label(dataframe, text="Email Id :", font=(font, 15), bg=color)
            emailid.place(x=200, y=280)
            emailid = Label(dataframe, text=Email, font=(font, 15), bg=color)
            emailid.place(x=400, y=280)

            joindate2 = Label(dataframe, text="Join date :", font=(font, 15), bg=color)
            joindate2.place(x=200, y=310)
            joindate2 = Label(dataframe, text=joindate, font=(font, 15), bg=color)
            joindate2.place(x=400, y=310)

            qual = Label(dataframe, text="Qualificatio :", font=(font, 15), bg=color)
            qual.place(x=200, y=340)
            qual = Label(dataframe, text=qualification, font=(font, 15), bg=color)
            qual.place(x=400, y=340)


            address1 = Label(dataframe, text="Address :", font=(font, 15), bg=color)
            address1.place(x=200, y=370)
            address1 = Label(dataframe, text=address, font=(font, 15), bg=color)
            address1.place(x=400, y=370)

            address1 = Label(dataframe, text="QR Link :", font=(font, 15), bg=color)
            address1.place(x=200, y=400)
            qr_entry = Entry(dataframe, width=40, textvariable=qrlink)
            qr_entry.place(x=400, y=407)

            submit_button = Button(dataframe, text="Create Id", width=20, font=("Bootiquak An", 13), command=Create_id)
            submit_button.place(x=330, y=450)
        else:
            messagebox.showinfo("Opps","File Not Found")
    else:
        messagebox.showinfo("Opps", "Please enter details")

def id_generate():
    global deg_box3
    global iframe
    iframe = Frame(width=width1 / 1.5, height=height1 / 1.2, bg=color)
    iframe.place(x=0, y=0)

    registration_label = Label(iframe, text="Create Id Card", font=("ALGERIAN", 30, "bold"), fg="#1bb7f5", width=35)
    registration_label.place(x=0, y=0)

    deg = Label(iframe, text="Designation :", font=(font, 15), bg=color)
    deg.place(x=10, y=60)
    designation = ['Student', 'Teacher']
    deg_box3 = Combobox(iframe, width=35, values=designation)
    deg_box3.place(x=150, y=67)

    name = Label(iframe, text="Name/Reg no.", font=(font, 15), bg=color)
    name.place(x=500, y=60)
    name_entry = Entry(iframe, width=32, textvariable=Name1)
    name_entry.place(x=630, y=67)
    photo_button = Button(iframe, text="Search", width=10, font=("Bootiquak An", 7), command=searchid)
    photo_button.place(x=835, y=65)

    id_button = Button(iframe, text="Back", width=10, font=("Bootiquak An", 10), command=home)
    id_button.place(x=0, y=0)


#for Home
def home():
    hframe=Frame(root,width=width1/1.5,height=height1/1.2,bg="#c7f57d")
    hframe.place(x=0,y=0)
    label1=Label(hframe,text="ID GENERATOR",font=("ALGERIAN",30,"bold"),fg="#1bb7f5", width=35)
    label1.place(x=0,y=0)
    #c=Canvas(hframe,bg="#c7f57d")
   # line=c.create_line(10,3,400,3)
    #c.place(x=width1/5.3,y=50)

    id_button=Button(hframe,text="Create Id",font=("Book Antiqua",20),width=15,command=id_generate)
    id_button.place(x=width1/4.1,y=height1/3.2)

    r_button=Button(hframe,text="Register",font=("Book Antiqua",20),width=15,command=registration_form)
    r_button.place(x=width1/4.1,y=height1/2.4)    
    Name1.set('')




home()
root.mainloop()