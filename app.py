import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best',
        'cookies': 'cookies.txt'  # Ensure cookies.txt file is in the correct directory
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # False means it will only fetch info, not download
        return info['url']

url = "https://youtu.be/uKGTGnfrTS0"
download_link = download_video(url)
print("Download Link:", download_link)
