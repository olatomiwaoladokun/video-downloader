# import libaries/packages
import tkinter as tk
from tkinter import ttk
import re
import urllib
import webbrowser
import pytube
from  pytube import YouTube
import os
import sys
from sys import argv
from PIL import  ImageTk, Image
from tkinter import PhotoImage, ttk

#set root
root = tk.Tk()
root.geometry("700x500")
root.title("Tommy- Download")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file = "/home/tom/Documents/video_downloader/play.jpg"))
root.resizable(height=False, width=False)



def download(event):
    global status_error, status_error1
    try:
        status.config(state=tk.NORMAL)
        video = YouTube(str(url.get()))
        # done = f"Congratulations!\nYour video({video.title}) with ({video.views}) has been successfully downloaded to:\n{status.download()}"
        # status.insert("end", done)
        streams = video.streams.filter(progressive= True, file_extension= "mp4").get_by_itag(22)
        stream_mes = streams.download()
        status.insert("end", streams.download())
        status.delete(0, "end")
        done = f"\nCongratulations your video has been successfully downloaded, \nCompleted Downloading {streams.title}\nwith {streams.views} views\nto the present folder"
        status.insert("end", streams.title)
        # status.insert("end", f"downloading... {video.title}, with {video.views} views")
        status.config(state=tk.DISABLED)
    except  urllib.error.URLError:
        status.config(state=tk.NORMAL)
        status_error1= "Dear user your video couldn't be downloaded\nbecause your internet connection is weak\nPlease check your connection and try agein\n\n"
        status.config(fg="gold")
        status.delete(0, "end")
        status.insert("end", status_error1)
        status.config(state=tk.DISABLED)
    except pytube.exceptions.RegexMatchError:
        status.config(state=tk.NORMAL)
        status.delete(0, "end")
        status_error= "Dear user your video couldn't be downloaded\nbecause you inputed an invalid url!\n\n"
        status.config(fg="red")
        # status.delete("1.0", "end")
        status.insert("end", status_error)
        status.config(state=tk.DISABLED)
#    except:
#       status.delete(0, "end")
#        status.insert("end", "There was an error in downloading the video")
        
def open_youtube():
    webbrowser.open(url="https://www.youtube.com")
def open_url():
    webbrowser.open(url=str(url.get()))




url_label = tk.Label(text="Video Url:", fg="blue")
url_label.place(x=10,y=6)



url = tk.Entry(root, width=60)
url.bind("<Return>", download)
url.place(x=80, y=6)

download_btn = tk.Button(root, text="Download", command=lambda: download(download), bg="green")
download_btn.place(x=580,y=0)




status = tk.Text(root, fg="green")
status.config(state=tk.DISABLED)
status.pack(padx= 10, pady=20, expand=True)

scroll_status = ttk.Scrollbar(root, command=status.yview)
scroll_status.place(x=680, y=0, height=500)
status.config(yscrollcommand=scroll_status.set)

youtube_btn = tk.Button(text="Open YouTube", bg="sky blue", command=open_youtube)
youtube_btn.place(x=120, y=460)

url_btn = tk.Button(text="Open Url", bg="Yellow", command=open_url)
url_btn.place(x=420,y=460)


# exit button
def exit_cmd():
    root.destroy()


exit = tk.Button(root,text="Exit", bg="red", command=exit_cmd)

exit.place(x=300, y=460)


root.mainloop()
# sys_url = argv[1]








