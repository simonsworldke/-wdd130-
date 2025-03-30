import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
import threading

# Function to handle the download and update progress
def download_video(video_url, save_path, progress_var, root):
    def progress_hook(d):
        if d['status'] == 'downloading':
            # Update progress bar based on downloaded bytes and total size
            if d.get('downloaded_bytes') and d.get('total_bytes'):
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                progress_var.set(percent)
                root.update_idletasks()  # Force Tkinter to update the progress bar

    try:
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "progress_hooks": [progress_hook]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

# Function to start the download in a separate thread
def start_download():
    video_url = url_entry.get()
    if not video_url.strip():
        messagebox.showwarning("Warning", "Please enter a YouTube URL.")
        return
    save_path = save_path_var.get()

    # Run the download in a separate thread
    download_thread = threading.Thread(target=download_video, args=(video_url, save_path, progress_var, root))
    download_thread.start()

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_path_var.set(folder_selected)

# GUI setup
root = ttk.Window(themename="superhero")
root.title("YouTube Video Downloader")
root.geometry("500x300")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

url_label = ttk.Label(frame, text="Enter YouTube URL:")
url_label.pack(anchor="w")

url_entry = ttk.Entry(frame, width=50)
url_entry.pack(pady=5)

save_path_var = tk.StringVar(value=r"C:\Users\HP\Downloads\Video")
save_label = ttk.Label(frame, text="Save Location:")
save_label.pack(anchor="w")

save_frame = ttk.Frame(frame)
save_frame.pack(fill="x")

save_entry = ttk.Entry(save_frame, textvariable=save_path_var, width=40)
save_entry.pack(side="left", padx=5, pady=5)

browse_button = ttk.Button(save_frame, text="Browse", command=browse_folder)
browse_button.pack(side="right")

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, fill="x")

download_button = ttk.Button(frame, text="Download", command=start_download, bootstyle="success")
download_button.pack(pady=10)

exit_button = ttk.Button(frame, text="Exit", command=root.quit, bootstyle="danger")
exit_button.pack()

root.mainloop()
