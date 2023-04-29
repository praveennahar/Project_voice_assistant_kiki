from KikiUi import Ui_KikiUi
from PyQt5 import QtCore,QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
###############################################
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup
import sys
# from login import *

engine = pyttsx3.init('sapi5')        #Speech Application Programming Interface
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[7].id)
# engine.setProperty('rate',170) #it's control a speed of voice 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()



    def wishMe(self):
        self.hour = int(datetime.datetime.now().hour)
        if self.hour>=0 and self.hour<12:
            speak("Good Morning!")

        elif self.hour>=12 and self.hour<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am kiki Sir. Please tell me how may I help you")

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            self.r.adjust_for_ambient_noise(source)
            self.r.pause_threshold = 1
            self.audio = self.r.listen(source)

        try:
            print("Recognizing...")
            self.query = self.r.recognize_google(self.audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return self.query


    def Task_Gui(self):
        self.wishMe()
        while True:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                self.results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(self.results)
                speak(self.results)

            elif 'intro' in self.query:
                speak("My name is kiki,sir and I am your personal voice assistant , I will help you to do a daily work,in behalf of you")

            elif 'about yourself' in self.query:
                speak("My name is kiki,sir and I am your personal voice assistant , I will help you to do a daily work,in behalf of you")

            elif 'how' in self.query:
                speak("I'm fine sir, tell me sir what can i do for you.")

            elif 'do' in self.query:
                speak("I can open the application and website like : google , youtube , stachoverflow , online gdb ,"
                      " whatsapp , notepad , Vs code , & I can search wikipedia for you ,"
                      " I will tell you the current time & temperature ,  play music , "
                      "& I can search and play youtube video , tell me sir what can i do for you .")

            elif 'youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'google' in self.query:
                webbrowser.open("google.com")

            elif 'stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'gdb' in self.query:
                webbrowser.open("https://www.onlinegdb.com/")

            elif 'play music' in self.query:
                webbrowser.open("https://music.youtube.com/watch?v=_FySknC-GfM&list=PL9EsgLc9j5H92ohWkyDo-kN0WFpz2J0IF")

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'date' in self.query:
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                day = datetime.datetime.now().day
                speak(f"Sir,the date is {day,month,year}")


            elif 'open vs code' in self.query:
                codePath = "C:\\Users\\DELL\\OneDrive\\Desktop\\Visual Studio Code.lnk"
                os.startfile(codePath)

            elif "whatsapp" in self.query:
                webbrowser.open("https://web.whatsapp.com/")

            elif "play" in self.query:
                self.b="Opening youtube"
                engine.say(self.b)
                engine.runAndWait()
                pywhatkit.playonyt(self.query)

            # elif 'email' in self.query:
            #     try:
            #         speak("What should I say?")
            #         self.content = self.takeCommand()
            #         to = "praveennahar033@gmail.com"
            #         # sendEmail(to, content)
            #         speak("Email has been sent!")
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry my friend . I am not able to send this email")


            elif 'joke' in self.query:
                self.joke_1 = pyjokes.get_joke(language='en',category='neutral')
                print(self.joke_1)
                speak(self.joke_1)

            elif 'notepad' in self.query:
                self.codePath = "C:\\Windows\\notepad.exe"
                os.startfile(self.codePath)


            elif 'temperature' in self.query:
                self.search = "temperature in bhopal"
                url = f"https://www.google.com/search?q={self.search}"
                w = requests.get(url)
                data = BeautifulSoup(w.text, "html.parser")  # it will provide a runtime environment to run a code
                temp = data.find("div", class_="BNeawe").text
                bpl = f"Current {self.search} is {temp}"
                print(bpl)
                speak(bpl)

            elif 'sleep' in self.query:
                speak("okay,bye sir thank you!")
                exit()

            else :
                speak("sorry sir,I'm not capable to find it,")


startfunction = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kiki_ui = Ui_KikiUi()
        self.kiki_ui.setupUi(self)

        self.kiki_ui.pushButton.clicked.connect(self.startFunc)
        self.kiki_ui.pushButton_2.clicked.connect(self.close)

    
    def startFunc(self):

        self.kiki_ui.movies_2 = QtGui.QMovie("__1.gif")
        self.kiki_ui.label_2.setMovie(self.kiki_ui.movies_2)
        self.kiki_ui.movies_2.start()

        self.kiki_ui.movies_3 = QtGui.QMovie("../GUI material/B.G/Iron_Template_1.gif")
        self.kiki_ui.label_3.setMovie(self.kiki_ui.movies_3)
        self.kiki_ui.movies_3.start()

        self.kiki_ui.movies_4 = QtGui.QMovie("../GUI material/extra/B.G_Template_1.gif")
        self.kiki_ui.label_4.setMovie(self.kiki_ui.movies_4)
        self.kiki_ui.movies_4.start()

        startfunction.start()

###############################################################################################################################################
from tkinter import *
from tkinter import messagebox
import pymysql



def CreateConn():
    return pymysql.connect(host="localhost", database="kiki", user="root", passwd="root@123456789", port=3306)


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login In Your Kiki")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")

        # --------BG Image---------

        # self.bg = ImageTk.PhotoImage(file="images/Black_Template.jpg")
        # self.bg_image = Label(self.root,image=self.bg).place(x=0,relwidth=1,relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="orange", bg="white").place(x=90,
                                                                                                                  y=30)
        desc = Label(Frame_login, text="Kiki Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(Frame_login, text="Forget Password?", bg="white", fg="#d25d17", bd=0,
                            font=("times new roman", 12)).place(x=90, y=280)
        login_btn = Button(self.root, text="Login", command=self.login_function, bg="#d77337", fg="white",
                           font=("times new roman", 20)).place(x=300, y=470, width=180, height=40)

    def login_function(self):

        self.u = self.txt_user.get()
        self.p = self.txt_pass.get()

        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        # elif self.txt_user.get()!="kiki" or self.txt_pass.get()!="kiki123":
        #     messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            try:
                self.conn = CreateConn()  # Creating Connection
                self.cursor = self.conn.cursor()
                self.args = (self.u, self.p)
                self.query = "insert into kiki_user_info(username,password)values(%s,%s)"
                self.cursor.execute(self.query, self.args)
                self.conn.commit()  # Saving the data using commit function
                messagebox.showinfo("welcome", f"Welcome {self.txt_user.get()}\nLogin Successfully", parent=self.root)
                self.conn.close()
#######################Calling Main garvis##########################################
                Gui_App = QApplication(sys.argv)
                Gui_kiki = Gui_Start()
                Gui_kiki.show()
                exit(Gui_App.exec_())
#############################################################################
            except Exception as e:
                print("Insert Exception Error : ", e)


root = Tk()
obj = Login(root)
root.mainloop()




# def Main():
#     Gui_App = QApplication(sys.argv)
#     Gui_kiki = Gui_Start()
#     Gui_kiki.show()
#     exit(Gui_App.exec_())