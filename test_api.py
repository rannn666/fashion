import urllib.request
import json

try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/api/posts/')
    data = json.loads(response.read().decode())
    print('API测试成功！')
    print(f'博客文章数量: {len(data)}')
    for post in data:
        print(f'- {post["title"]} by {post["author"]["username"]}')
except Exception as e:
    print(f'API测试失败: {e}')