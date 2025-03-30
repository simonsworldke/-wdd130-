import yt_dlp

def download_video(video_url, save_path="."):
    try:
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    save_path = r"C:\Users\HP\Downloads\Video"or "."
    download_video(video_url, save_path)