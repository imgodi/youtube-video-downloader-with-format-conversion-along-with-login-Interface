from __future__ import unicode_literals
# from __future__ import unicode_literals should always be the first line of code
# when planning to use it
# For extracting information from website
from tkinter import *
import yt_dlp as youtube_dl
from tkinter import messagebox
import requests
import socket
import speedtest
import pyttsx3
global engine
from tkinter import ttk
import smtplib
import random
import os

def confirm():
    global p
    p = Tk()
    p.geometry("1920x1080")
    p.title("Aincrad Youtube Downloader")

    C = Canvas(p, bg="blue", height=250, width=300)
    filename = PhotoImage(master=C,file="BGpy.png")
    background_label = Label(p, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    midf = Frame(p, bg="lightpink2")
    midf.pack(side=BOTTOM, expand=YES)

    def i_button_hover(e):
        i["bg"] = "pink"

    def i_hover_leave(e):
        i["bg"] = "SystemButtonFace"  # Default button colour on windows

    def mp3_button_hover(e):
        mp3["bg"] = "pink"

    def mp3_hover_leave(e):
        mp3["bg"] = "SystemButtonFace"  # Default button colour on windows

    def mp4_button_hover(e):
        mp4["bg"] = "pink"

    def mp4_hover_leave(e):
        mp4["bg"] = "SystemButtonFace"  # Default button colour on windows

    i = Button(midf, text="Check Internet status", font=("Arial", "15"), command=internet)
    mp3 = Button(midf, text="MP3 Download", font=("Arial", "15"), command=c3)
    mp4 = Button(midf, text="Video Download", font=("Arial", "15"), command=c4)
    i.grid(row=1, column=600, ipady=10, pady=10)
    mp3.grid(row=2, column=0, padx=10, pady=10)
    mp4.grid(row=2, column=1000, padx=10, pady=10)

    i.bind("<Enter>", i_button_hover)
    i.bind("<Leave>", i_hover_leave)

    mp3.bind("<Enter>", mp3_button_hover)
    mp3.bind("<Leave>", mp3_hover_leave)

    mp4.bind("<Enter>", mp4_button_hover)
    mp4.bind("<Leave>", mp4_hover_leave)

    C.pack()
    p.mainloop()


def internet():
    global IPaddress
    global download
    global upload
    global ping
    global enter
    global engine
    global voices
    global var
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[0].id)

    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        engine.say("No Internet connection detected")
        engine.runAndWait()
        
        #messagebox.showerror("No Internet, your localhost is " + IPaddress,
        #                    "Please make sure you are connected to the internet")

    else:
        engine.say("Connected to Internet")
        engine.runAndWait()
        
        #messagebox.showinfo("Connected to internet", "Connected to internet")
        engine.say("Please Wait  " + " Taking speedtest")
        engine.runAndWait()
        #messagebox.showinfo("Please Wait", " Taking speedtest")
        st = speedtest.Speedtest()
        download = str((st.download() / 1024) / 1024) + "    Mbps"
        upload = str((st.upload() / 1024) / 1024) + "   Mbps"
        ping = str(st.results.ping)
        engine.say("Speedtest Done Taking Results")
        engine.runAndWait()
        #messagebox.showinfo("Speeedtest Done", " Results Taken")

        op = Tk()
        op.title("Speedtest Results")
        fr=Frame(op, bg="pink1")
        fr.grid()
        L6 = Label(fr, text="Download Speed   >>>", font=("Arial", "15"), bg="pink1")
        L6.grid(row=6, column=0)

        L7 = Label(fr, text="Upload Speed    >>>", font=("Arial", "15"), bg="pink1")
        L7.grid(row=7, column=0)

        L8 = Label(fr, text="Ping  >>>", font=("Arial", "15"), bg="pink1")
        L8.grid(row=8, column=0)

        L_6 = Label(fr, text=download, font=("Arial", "15"), bg="pink1")
        L_6.grid(row=6, column=1)

        L_7 = Label(fr, text=upload, font=("Arial", "15"), bg="pink1")
        L_7.grid(row=7, column=1)

        L_8 = Label(fr, text=ping, font=("Arial", "15"), bg="pink1")
        L_8.grid(row=8, column=1)


def c3():
    global enter
    global vr
    global room
    vr = 1
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[0].id)

    room = Tk()
    room.config(bg="pink1")
    room.geometry("1000x200")
    room.title("Mp3 Download")
    url = Label(room, text="Enter Youtube URL or Link", font=("Arial", "15"), bg="pink1")
    url.grid(row=1, column=0)

    enter = Entry(room)
    enter.grid(row=1, column=1, pady=10, ipadx=100)
    engine.say("Enter Youtube URL or Link")
    engine.runAndWait()

    Fra = LabelFrame(room, padx=50, pady=50, bg="pink2")
    Fra.grid(row=2, column=1)
    su = Button(Fra, text="SUBMIT LINK", font=("Arial", "15"), command=s)
    su.grid(row=10, column=3)

    def su_button_hover(e):
        su["bg"] = "lightpink2"

    def su_hover_leave(e):
        su["bg"] = "SystemButtonFace"

    su.bind("<Enter>", su_button_hover)
    su.bind("<Leave>", su_hover_leave)

    room.mainloop()

def c4():
    global enter
    global vr
    global root
    vr = 0
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[0].id)

    root = Tk()
    root.config(bg="pink1")
    root.geometry("1000x200")
    root.title("Video Download")
    url = Label(root, text="Enter Youtube URL or Link", font=("Arial", "15"), bg="pink1")
    url.grid(row=1, column=0)

    enter = Entry(root)
    enter.grid(row=1, column=1, pady=10, ipadx=100)
    engine.say("Enter Youtube URL or Link")
    engine.runAndWait()

    Fra = LabelFrame(root, padx=50, pady=50, bg="pink2")
    Fra.grid(row=2, column=1)
    su = Button(Fra, text="SUBMIT LINK", font=("Arial", "15"), command=s)
    su.grid(row=10, column=3)

    def su_button_hover(e):
        su["bg"] = "lightpink2"

    def su_hover_leave(e):
        su["bg"] = "SystemButtonFace"

    su.bind("<Enter>", su_button_hover)
    su.bind("<Leave>", su_hover_leave)

    root.mainloop()
def s():
    global r
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[0].id)

    global e
    e = enter.get()
    if e == "https://www.youtube.com/" or e == "https://www.youtube.com" or e == "https://youtube.com":# or "watch?" not in  e:
        engine.say("Link Not Valid   " + " You have entered youtube.com,please click on a video then take link")
        engine.runAndWait()
        messagebox.showerror("Link Not Valid  ----",
                             "You have entered youtube.com, please click on a video then take link")

    else:
        if "https://" in e and "watch?" in e and e != "https://www.youtube.com/" and e != "https://www.youtube.com" and e != "https://youtube.com"and e.startswith("https://www.youtube.com/")==True:
            engine.say("https present   validating link")
            engine.runAndWait()
            #messagebox.showinfo("https:// present  ----", "https:// present validating link")
            global d
            r = requests.get(e)
            if "Video unavailable" in r.text or "404 Not Found" in r.text:
                engine.say(
                    "Link Not Valid    Please enter valid link either given link's video is unavailable or error 404 Not Found")
                engine.runAndWait()
                messagebox.showerror("Link Not Valid  ----",
                                     "Please enter valid link either given link's video is unavailable or error 404 Not Found")
            else:
                engine.say("Link Valid getting details")
                engine.runAndWait()
                messagebox.showinfo("Link Valid", "Link Valid getting details")
                r = Tk()
                r.config(bg="pink1")
                ydl_opt = {}
                with youtube_dl.YoutubeDL(ydl_opt) as ydl:
                    meta = ydl.extract_info(e, download=False)
                Fram = LabelFrame(r, padx=50, pady=50, bg="pink1")
                Fram.grid()
                L1 = Label(Fram, text="Upload Date  >>>", font=("Arial", "15"), bg="pink1")
                L1.grid(row=1, column=0)

                L2 = Label(Fram, text="Chanel Name   >>>", font=("Arial", "15"), bg="pink1")
                L2.grid(row=2, column=0)

                L3 = Label(Fram, text="View Count    >>>", font=("Arial", "15"), bg="pink1")
                L3.grid(row=3, column=0)

                L4 = Label(Fram, text="Duration In Seconds  >>>", font=("Arial", "15"), bg="pink1")
                L4.grid(row=4, column=0)

                L5 = Label(Fram, text="Video Title    >>>", font=("Arial", "15"), bg="pink1")
                L5.grid(row=5, column=0)

                L_1 = Label(Fram, text=meta['upload_date'], font=("Arial", "15"), bg="pink1")
                L_1.grid(row=1, column=1)

                L_2 = Label(Fram, text=meta['uploader'], font=("Arial", "15"), bg="pink1")
                L_2.grid(row=2, column=1)

                L_3 = Label(Fram, text=meta['view_count'], font=("Arial", "15"), bg="pink1")
                L_3.grid(row=3, column=1)

                L_4 = Label(Fram, text=meta['duration'], font=("Arial", "15"), bg="pink1")
                L_4.grid(row=4, column=1)

                L_5 = Label(Fram, text=meta['title'], font=("Arial", "15"), bg="pink1")
                L_5.grid(row=5, column=1)

                d = Button(Fram, text="Download", font=("Arial", "15"), command=do)
                d.grid(row=10, column=2)

                def d_button_hover(e):
                    d["bg"] = "lightpink2"

                def d_hover_leave(e):
                    d["bg"] = "SystemButtonFace"

                d.bind("<Enter>", d_button_hover)
                d.bind("<Leave>", d_hover_leave)

                r.mainloop()

        else:
            engine.say("Link Not Valid, https not present or you have not entered youtube link")
            engine.runAndWait()
            messagebox.showerror("Link Not Valid  ----", "https:// not present or you have not entered youtube link")


def do():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 125)
    engine.setProperty('voice', voices[0].id)
    global vr
    engine.say("Please Wait Starting download May Take Some Time")
    engine.runAndWait()
    messagebox.showinfo("Please Wait", "Starting download May Take Some Time")
    if vr == 0:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([e])

        engine.say("Download Successful! Video downloaded")
        engine.runAndWait()

        messagebox.showinfo("Download Successful  ----", "Video downloaded")
        r.after(4000, r.destroy)
        root.after(4000, root.destroy)
        
    elif vr == 1:
        ydl_opts = {

            'format': 'bestaudio/best',  # choice of quality

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([e])

        engine.say("Download Successful! Mp3 downloaded")
        engine.runAndWait()

        messagebox.showinfo("Download Successful  ----", "Mp3   downloaded")
        r.after(4000, r.destroy)
        room.after(4000, room.destroy)

    # freq = 100
    # dur = 2500
    # winsound.Beep(freq, dur)
# for forgot password
def forgotpassword():
    global forgot_screen
    forgot_screen = Toplevel(main_screen)
    forgot_screen.geometry("400x500")
    global email_ID_
    global email_ID
    global email_ID_entry
    global email_ID_info
    email_ID = StringVar()
    email_ID_ = Label(forgot_screen, text="Enter Email_ID")
    email_ID_.pack()
    email_ID_entry = Entry(forgot_screen, textvariable=email_ID)
    email_ID_entry.pack()
    email_ID_info = email_ID.get()
    vErify_Otp = Button(forgot_screen, text="Enter Mail_ID", width=10, height=1, bg="grey", command=forget)

    vErify_Otp.pack()
    def vErify_Otp_hover(e):
        vErify_Otp["bg"] = "white"

    def vErify_Otp_hover_leave(e):
        vErify_Otp["bg"] = "SystemButtonFace"

    vErify_Otp.bind("<Enter>", vErify_Otp_hover)
    vErify_Otp.bind("<Leave>", vErify_Otp_hover_leave)


    forgot_screen.after(60000, forgot_screen.destroy)


def forget():
    list_of_files = os.listdir()
    email_ID_info = email_ID.get()
    # print(email_ID.get())

    if email_ID_info.replace('.com', "") in list_of_files:
        file1 = open(email_ID_info.replace(".com", ""), "r")
        verify = file1.read().splitlines()
        if email_ID_info in verify:
            # print(email_ID_info in verify)
            login_via_otp()
            # print(email_ID_info)
        # else:
        # email_ID_entry.delete(0, END)
        # messagebox.showerror("Email ID Not Found","Enter Valid Email ID")

    else:
        messagebox.showerror("Email ID Not Found", "Enter Valid Email ID")


def error():
    messagebox.showerror("Email ID Not Found", "Enter Valid Email ID")


# for loggining in with otp

def verify_Otp():
    global verify_otP
    global OTP
    OTP = StringVar()

    verify_otP = Toplevel(main_screen)
    verify_otP.geometry("400x500")
    otp_verify = Label(verify_otP, text="Enter OTP Sent to Mail").pack()

    otp_verify_entry = Entry(verify_otP, textvariable=OTP)
    otp_verify_entry.pack()
    Verify_Otp = Button(verify_otP, text="Enter Values", width=10, height=1, bg="grey", command=verify_oTp)

    Verify_Otp.pack()
    def Verify_Otp_hover(e):
        Verify_Otp["bg"] = "white"

    def Verify_Otp_hover_leave(e):
        Verify_Otp["bg"] = "SystemButtonFace"

    Verify_Otp.bind("<Enter>", Verify_Otp_hover)
    Verify_Otp.bind("<Leave>", Verify_Otp_hover_leave)

    
    verify_otP.after(75000, verify_otP.destroy)


def verify_oTp():
    otp_v = OTP.get()
    if otp_v == otp:
        login_sucess()
    else:
        messagebox.showerror("Error", "Entered OTP Doesn't Match With OTP Sent Via Mail")


# for changing password via otp sent
def login_via_otp():
    global via_otp
    global otp
    global verify_Otp
    a = email_ID.get()
    via_otp = Toplevel(main_screen)
    via_otp.geometry("400x500")
    otp = str(random.randint(111111, 999999))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("Aincradofficialdownloader@gmail.com", "zjsyakrknxidcurj")
    server.sendmail("Aincradofficialdownloader@gmail.com",
                    "" + a,
                    "Hi, Your OTP Is  " + str(otp))
    server.quit()
    verify_Otp = Button(via_otp, text="Verify OTP", width=10, height=1, bg="grey", command=verify_Otp)
    verify_Otp.pack()
    def verify_Otp_hover(e):
        verify_Otp["bg"] = "white"

    def verify_Otp_hover_leave(e):
        verify_Otp["bg"] = "SystemButtonFace"

    verify_Otp.bind("<Enter>", verify_Otp_hover)
    verify_Otp.bind("<Leave>", verify_Otp_hover_leave)


    via_otp.after(60000, via_otp.destroy)


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x400")

    global username
    global password
    global confirm_password
    global alternate_emailID
    global username_entry
    global password_entry
    global confirm_password_entry
    global alternate_emailID_entry
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()
    alternate_emailID = StringVar()

    Label(register_screen, text="Please enter details below", bg="grey").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Email_ID ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()

    confirm_password_label = Label(register_screen, text="Confirm Password   ")
    confirm_password_label.pack()
    confirm_password_entry = Entry(register_screen, textvariable=confirm_password)
    confirm_password_entry.pack()

    alternate_emailID_label = Label(register_screen, text="Alternate Email ID ")
    alternate_emailID_label.pack()
    alternate_emailID_entry = Entry(register_screen, textvariable=alternate_emailID)
    alternate_emailID_entry.pack()

    Label(register_screen, text="").pack()
    button = Button(register_screen, text="Register", width=10, height=1, bg="grey", command=register_user)
    button.pack()
    def button_hover(e):
        button["bg"] = "white"

    def button_hover_leave(e):
        button["bg"] = "SystemButtonFace"

    button.bind("<Enter>", button_hover)
    button.bind("<Leave>", button_hover_leave)

    # button['state']=DISABLED

    # if password==confirm_password:


# button['state']=NORMAL


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Email_ID * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    forgot_password = Button(login_screen, text="forgot Password", command=forgotpassword).pack()
    bu=Button(login_screen, text="Login", width=10, height=1, command=login_verify)
    bu.pack()
    def bu_hover(e):
        bu["bg"] = "white"

    def bu_hover_leave(e):
        bu["bg"] = "SystemButtonFace"

    bu.bind("<Enter>", bu_hover)
    bu.bind("<Leave>", bu_hover_leave)


# Implementing event on register button

def register_user():
    global Lab
    global Hab

    username_info = username.get()
    password_info = password.get()
    confirm_password_info = confirm_password.get()
    alternate_emailID_info = alternate_emailID.get()

    list_of_files = os.listdir()
    if username_info.replace('.com', "") in list_of_files:
        username_entry.delete(0, END)
        # messagebox.showerror("Email ID Already Exists","Please enter new Email ID")
        Lab = Label(register_screen, text="Email Id Already Exists", fg="red", font=("calibri", 11))
        Lab.pack()
        messagebox.showerror("Email ID ALready Exists", "Please Enter New Mail ID")
        # freq=3000
        # dur=4000
        # winsound.Beep(freq, dur)
        Lab.after(4000, Lab.destroy)



    else:
        if username_info != "" and password_info != "" and confirm_password_info != "" and alternate_emailID_info != "":
            if password_info == confirm_password_info:
                # print(username_info.rstrip("@"))
                file = open(username_info.replace('.com', ''), "w")
                file.write(username_info + "\n")
                file.write(password_info + "\n")
                file.write(alternate_emailID_info)
                file.close()

                confirm_password_entry.delete(0, END)
                alternate_emailID_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

                Hab = Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11))
                Hab.pack()
                # freq=3000
                # dur=4000
                # winsound.Beep(freq, dur)
                Hab.after(4000, Hab.destroy)

            else:
                messagebox.showerror("Passwords Do Not Match",
                                     "Please make sure you have entered the same password in both entires")
        else:
            messagebox.showerror("One Or More Entires", "Please make sure you have filled all  entires")


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1.replace('.com', "") in list_of_files:
        file1 = open(username1.replace(".com", ""), "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("350x200")
    Label(login_success_screen, text="Login Success").pack()
    ju=Button(login_success_screen, text="OK", command=delete_login_success)
    ju.pack()
    def ju_hover(e):
        ju["bg"] = "white"

    def ju_hover_leave(e):
        ju["bg"] = "SystemButtonFace"

    ju.bind("<Enter>", ju_hover)
    ju.bind("<Leave>", ju_hover_leave)

    


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("50x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    au=Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised)
    au.pack()
    def au_hover(e):
        au["bg"] = "white"

    def au_hover_leave(e):
        au["bg"] = "SystemButtonFace"

    au.bind("<Enter>", au_hover)
    au.bind("<Leave>", au_hover_leave)


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("350x200")
    Label(user_not_found_screen, text="User Not Found").pack()
    mu=Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen)
    mu.pack()
    def mu_hover(e):
        mu["bg"] = "white"

    def mu_hover_leave(e):
        mu["bg"] = "SystemButtonFace"

    mu.bind("<Enter>", mu_hover)
    mu.bind("<Leave>", mu_hover_leave)
    


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

    after_login()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x350")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    ku=Button(main_screen,text="Login", height="2", width="30", command=login)
    ku.pack()
    Label(text="").pack()
    lu=Button(main_screen,text="Register", height="2", width="30", command=register)
    lu.pack()
    def ku_hover(e):
        ku["bg"] = "white"

    def ku_hover_leave(e):
        ku["bg"] = "SystemButtonFace"

    ku.bind("<Enter>", ku_hover)
    ku.bind("<Leave>", ku_hover_leave)
    
    def lu_hover(e):
        lu["bg"] = "white"

    def lu_hover_leave(e):
        lu["bg"] = "SystemButtonFace"

    lu.bind("<Enter>",lu_hover)
    lu.bind("<Leave>", lu_hover_leave)

    main_screen.mainloop()

def after_login():
    login_screen.after(1000, login_screen.destroy)
    main_screen.after(1000,main_screen.destroy)
    confirm()

main_account_screen()


