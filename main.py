from tkinter import *
from tkinter import ttk
import pyperclip
from tkinter import messagebox, ttk
from pytube import YouTube


def about():
    messagebox.showinfo("Youtube Downloader",
                        "Developed by Anshuman | All Rights Reserved")


def paste():
    url_entry.config(textvariable=url)
    url.set(str(pyperclip.paste()))


def download_now():
    if url.get() == '':
        messagebox.showwarning('Warning!', \
        "Please Enter a Valid URL")
    else:
        try:
            yt = YouTube(url.get())
            # If the user selects 'Audio Only' option
            # from the combo box(Download the Audio)
            if quality_com.get() == 'Audio Only':
                audio = yt.streams.filter(type="audio").last()
                audio.download()
            # If the user selects any video resolution from
            # the combo box
            else:
                video = yt.streams.filter(mime_type="video/mp4",\
                res=quality_com.get(), progressive=True).first()
                video.download()
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")


video_quality = ['144p', '360p', '720p', 'Audio Only']

root = Tk()
root.geometry('700x500')
root.title("Youtube Video Downloader")
root.resizable(False, False)
root.configure(bg="white")
root.iconbitmap("youTube.ico")

url = StringVar()

# frame 1

frame = Frame(root).place(x=0, y=0, height=100, width=700)

# top side work

logo = PhotoImage(file="yt_logo.png")
logo_label = Label(frame, image=logo)
logo_label.place(x=10, y=22)

about = Button(frame,
               text="About",
               bg="#319deb",
               fg="red",
               font=("Alef Bold", 20),
               command=about).place(x=420, y=20)

exitq = Button(frame,
               text="Exit",
               bg="#319deb",
               fg="black",
               font=("Alef Bold", 20),
               command=root.destroy).place(x=550, y=20)

(url_entry := Entry(root,
                    bd=2,
                    relief=GROOVE,
                    font=("Bahnschrift SemiBold SemiCondensed", 16),
                    textvariable=url)).place(x=30, y=120, width=520, height=38)

paste_button = Button(root,
                      text="PASTE URL",
                      font=(("Alef Bold", 15)),
                      activebackground="white",
                      cursor="hand2",
                      command=paste,
                      bd=2,
                      relief=GROOVE).place(x=555, y=120, height=38)

quality_lbl = Label(root,
                    text="Quality            =",
                    font=("Calibri Bold", 30),
                    bg="white").place(x=30, y=245)

quality_com = ttk.Combobox(root,
                           font=("Roboto Bold", 20),
                           values=video_quality,
                           state='r',
                           width=12)
quality_com.set("Select Quality")
quality_com.place(x=330, y=255)

download_butt = Button(root,
                       text="Download Now",
                       font=("Calibri Bold", 30),
                       bg="lightyellow",
                       command=download_now,
                       activebackground="lightyellow",
                       bd=2,
                       relief=GROOVE,
                       cursor="hand2").place(x=200, y=375)

root.mainloop()
