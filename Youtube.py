# A simple youtube downloader 
'''This is a Simple Youtube Downloader based of Pytube module that can download
    1. Single Video File
    2. Entire Video playlist
    3. Select Videos from a playlist
    4. Single Audio File
    5. Entire Audio Playlist
    6. Select Audios from a playlist

Disclaimer : Some Files may fail to download due to privacy settings or unavailibility of the video
             in a given region. This downloader uses progressing stream which limits the maximum
             video quality to 720P. (Modify to DASH if you wish to download videos upto 4K resolution)
'''
from progress.bar import ChargingBar
from pytube import YouTube,Playlist

print('-'*70)
print(f'Download:\n1. Playlist\n2. Video \n3. Audio')
print('-'*70)
inp = int(input('Choice:'))

if inp == 1:
    plink = input('playlist link:')
    p = Playlist(plink)
    vids = len([url for url in p.video_urls])

    # Details about playlist
    print('Playlist Title:',p.title)
    print('No of Videos  :',vids)
    print('\nEntire Playlist or Select Videos?:')
    print(f'1. Playlist\n2. Select Videos')
    
    pinput = int(input('Choice:'))

# Downloading Entire Playlist    
    if pinput == 1:
        bar = ChargingBar(max = vids)
        for video in p.videos:
            print(f' Downloading: {video.title}')
            video.streams.get_highest_resolution().download()
            bar.next()
        bar.finish()
    
    elif pinput == 2:
        print('Enter Video indexes[Index starting from 0]:')
        try:
            v_list = []
            while True:
                v_list.append(int(input()))
        except:
            print(v_list)
        
# Downloading Select Videos from Playlist based on video index
        bar = ChargingBar()
        for x, video in enumerate(p.videos):
            if x in v_list:
                video.streams.get_highest_resolution().download()
                bar.next()    
            else:
                print(f'skipped {video.title}')
        bar.finish()

# Downloading Video 
elif inp == 2:
    try:
        vlink = input('Video Link:')
        v = YouTube(vlink)
        print(f'downloading {v.title}')
        v.streams.get_highest_resolution().download() 
    except:
        print('Sorry! This Video is Unavailable')

# Downloading Audio
elif inp == 3:
    print(f'1. Single Audio \n2. Playlist')
    ainput = int(input('Choice:'))
    
    # Downloading Single audio    
    if ainput == 1:
        try:
            alink = input('Video Link:')
            a = YouTube(alink)
            print(f'Downloading audio for {a.title}')
            a.streams.filter()
            a.streams.get_audio_only().download()   
        except:
            print("Sorry! Can't Downlaod This Audio")
    
    # Downloading Audio Playlist
    elif ainput == 2:
        aplaylist = input('Playlist Link:')
        p = Playlist(aplaylist)
        vids = len([url for url in p.video_urls])

        # Details about playlist
        print('Playlist Title:',p.title)
        print('No of Videos  :',vids)

        print('\nDownload Entire Playlist or Select Audio?:')
        print(f'1. Playlist\n2. Select Audio')
        choice = int(input('Choice:'))
        
        if choice == 1:
            bar = ChargingBar(max = vids)
            for video in p.videos:
                print(f' Downloading: {video.title}')
                video.streams.get_audio_only().download()
                bar.next()
            bar.finish()
    # Downloading Select audio from Playlist   
        elif choice == 2:
            print('Enter Audio indexes[index starting from 0]:')
            try:
                v_list = []
                while True:
                    v_list.append(int(input()))
            except:
                print(v_list)            
            bar = ChargingBar()
            for x, video in enumerate(p.videos):
                if x in v_list:
                    print(f' Downloading{video.title}')
                    video.streams.get_audio_only().download()
                    bar.next()    
                else:
                    print(f'skipped {video.title}')
            bar.finish()
else:
    print('Invalid Choice!')