### Download youtube audio directly -- QuteBrowser

Qutebrowser a keyboard centric browser, makes possible to run custom userscript written in any language which makes possible to add features as needed.
It is a lightweight browser built on top of PyQt5 toolkit, works with current Python (3.6.x) and has affinity for doing things the unix way - clean, simple, no bullshit.

As with unix philosophy, it can pipe commands with webpage text, current URL etc to your shell scripts or binaries, and can accept commands through a temporary FIFO/pipe back to the browser.

Check [Qutebrowser]() here, and running [custom script on QuteBrowser]()

**What does this solve ?**

- I am listening a song in youtube, I want to download the audio version of the video. Hit ```Ctrl + Shift + d``` or change the key binding as needed. 

![](https://raw.githubusercontent.com/prajinkhadka/qutebrowser-youtube-audio/main/example.gif)

**How to setup ?** 

1. Install Qutebrowser.

2. Install this awesome [tool](https://github.com/hiway/python-qutescript) that creates an executable bit set for qutebrowser to run them.

3. Install [youtube-dl](https://pypi.org/project/youtube_dl/)

4. Run ```curl https://raw.githubusercontent.com/prajinkhadka/qutebrowser-youtube-audio/main/download_audio.py >> download_audio.py```

5. Run ```mkdir music_directory``` or, replace with your music directory ```sed -i 's/music_directory/your_directory/g' download_audio.py```

5. Run ```python3 download_audio.py --install --bin=download_audio```, this will install a userscript at ```$HOME/user/.local/share/qutebrowser/userscripts/download_audio```

6. Open the youtube video that you want to download. ( important, you need to be on the same page what you want to download ) 

7. In command mode run ```:spawn --userscript download_audio``` , this will download and save the audio in the specified directory.

**Setting up Keybinding**

1. Qutebrowser stores config file in ```$HOME/.config/qutebrowser/config.py``` 

2. Add ```config.bind("<Ctrl+Shift+d>", "spawn --userscript download_audio")```



