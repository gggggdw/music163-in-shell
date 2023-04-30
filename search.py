import os
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
while True:
# 搜索关键词
    print("")
    keyword = input("搜索:")
    print("")

# 构造搜索结果的 URL
    url = 'https://music.163.com/api/search/get/web?csrf_token=&type=1&s=' + keyword + '&offset=0&total=true&limit=10'

# 发送 GET 请求获取 JSON 内容
    response = requests.get(url, headers=headers)
    data = json.loads(response.content.decode('utf-8'))

# 解析 JSON 内容
    results = data['result']['songs']

# 去重
    name_set = set()
    for result in results:
        name = result['name']
        artist = result['artists'][0]['name']
        album = result['album']['name']
        if name not in name_set:
            name_set.add(name)
            print("歌名:"+name,"歌手:"+artist,"ID:",result['id'])
            print('-' * os.get_terminal_size().columns)
    print("")
    con = int(input("""1继续
2结束
3下载id歌曲

>>>"""))
    if con == 1:
        print("")
        print('-' * os.get_terminal_size().columns)
        print("")
    if con == 2:
        break
    if con == 3:
        print("")
        print('-' * os.get_terminal_size().columns)
        print("")
        os.system("python3 dl_song.py")
        break
 #print("------------------------------------------")
