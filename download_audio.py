from qutescript import userscript
import youtube_dl

import urllib.request
import json
import urllib

base_dir = 'music_directory' #/home/user/Music/
music_dir = base_dir + "/" + "%(title)s.%(ext)s"

opts = {
    'format': 'bestaudio/best',
    'outtmpl': music_dir,

    'postprocessors' : [
                        {
            
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }
    ],
}

def get_video_title(link):
    print("THE LINK is",link)
    VideoID = link.split("=")[1]
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
            
    return data['title']

@userscript
def audio_download(request):
    url = request.url
    video_title = get_video_title(link=url)
    
    request.send_text(f"Downloading {video_title}")
    with youtube_dl.YoutubeDL(opts) as ydl_audio:
        ydl_audio.download([url]) 
    
    output_dir = opts['outtmpl'].split("%")[0]
    request.send_text(f"Download Completed {video_title} saved at {output_dir}")
    

if __name__ == '__main__':
    audio_download()
