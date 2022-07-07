from tkinter import *
from pytube import YouTube

display = Tk()
display.geometry('500x300')
display.title("youtube video downloader")


Label(display,text = 'Youtube Video Downloader', font ='arial 25 bold').pack()





link = StringVar()

Label(display, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 150 , y = 60)
link_enter = Entry(display, width = 80,textvariable = link).place(x = 32, y = 90)






def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  


Button(display,text = 'DOWNLOAD', font = 'arial 20 bold' ,bg = 'cyan', padx = 4, command = Downloader).place(x=180 ,y = 150)



display.mainloop()
