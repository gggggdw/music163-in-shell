import os

song_id = input("请输入歌曲id:") 
#name = input("请输入歌曲保存后的名字(不要有空格与后缀)")
url = f'https://music.163.com/song/media/outer/url?id={song_id}.mp3'

headers = {
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 下载歌曲
#command = "curl -H "Referer: {headers["Referer"]}" -H -H User-Agent:"{headers["User-Agent"]}"+url+" -o music.mp3"
command = f'curl -s -L -H "Referer: {headers["Referer"]}" -H "User-Agent: {headers["User-Agent"]}" -o {song_id}.mp3 {url}'
os.system(command)
print('下载完成')
