import customtkinter as ct
import tkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(str(ytlink))
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
    except:
        finishLabel.configure(text="Download Error", text_color="red")
    finishLabel.configure(text="Download Complete")


# System settings
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

# Our app frame
app = ct.CTk();
app.geometry("720x480")
app.title("Youtube Downloader")

# Add UI elements
title = ct.CTkLabel(app, text="Insert a youtube like")
title.pack(pady=10, padx=10)

# Link input
url_var = tkinter.StringVar()
link = ct.CTkEntry(app, width=450, height=40, textvariable=url_var)
link.pack()

# Finished text
finishLabel = ct.CTkLabel(app, text="")
finishLabel.pack()

# Download button
download = ct.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run the app
app.mainloop()
