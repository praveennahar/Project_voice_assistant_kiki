from tkinter import*
from tkinter import messagebox
import pymysql


def CreateConn():
    return pymysql.connect(host="localhost",database="kiki",user="root",passwd="root@123456789",port=3306)


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login In Your Kiki")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg="lightblue")

        # --------BG Image---------

        # self.bg = ImageTk.PhotoImage(file="images/Black_Template.jpg")
        # self.bg_image = Label(self.root,image=self.bg).place(x=0,relwidth=1,relheight=1)

        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="orange",bg="white").place(x=90,y=30)
        desc = Label(Frame_login,text="Kiki Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",
                     bg="white").place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn = Button(Frame_login,text="Forget Password?",bg="white",fg="#d25d17",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn = Button(self.root,text="Login",command=self.login_function,bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    def login_function(self):

        self.u=self.txt_user.get()
        self.p=self.txt_pass.get()


        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        # elif self.txt_user.get()!="kiki" or self.txt_pass.get()!="kiki123":
        #     messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            try:
                self.conn = CreateConn() # Creating Connection
                self.cursor = self.conn.cursor()
                self.args = (self.u,self.p)
                self.query = "insert into kiki_user_info(username,password)values(%s,%s)"
                self.cursor.execute(self.query,self.args)
                self.conn.commit() # Saving the data using commit function
                messagebox.showinfo("welcome",f"Welcome {self.txt_user.get()}\nLogin Successfully",parent=self.root)
                self.conn.close()
            
            except Exception as e:
                print("Insert Exception Error : ",e)


root = Tk()
obj=Login(root)
root.mainloop()