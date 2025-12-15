import urllib.request
import json

def test_api():
    print("=== 博客功能API测试 ===")
    
    # 测试博客文章列表API
    print("\n1. 测试博客文章列表API:")
    try:
        response = urllib.request.urlopen('http://127.0.0.1:8000/api/posts/')
        data = json.loads(response.read().decode())
        print(f"   ✓ 成功获取 {len(data)} 篇博客文章")
        for post in data:
            print(f"     - {post['title']} by {post['author']['username']}")
    except Exception as e:
        print(f"   ✗ 失败: {e}")
    
    # 测试评论API
    print("\n2. 测试评论API:")
    try:
        response = urllib.request.urlopen('http://127.0.0.1:8000/api/comments/')
        data = json.loads(response.read().decode())
        print(f"   ✓ 成功获取 {len(data)} 条评论")
        for comment in data:
            print(f"     - {comment['content'][:30]}... by {comment['author']['username']}")
    except Exception as e:
        print(f"   ✗ 失败: {e}")
    
    # 测试特定文章的评论API
    print("\n3. 测试文章详情和评论API:")
    try:
        # 先获取第一篇文章
        response = urllib.request.urlopen('http://127.0.0.1:8000/api/posts/')
        posts = json.loads(response.read().decode())
        if posts:
            post_id = posts[0]['id']
            response = urllib.request.urlopen(f'http://127.0.0.1:8000/api/posts/{post_id}/')
            post_detail = json.loads(response.read().decode())
            print(f"   ✓ 成功获取文章详情: {post_detail['title']}")
            print(f"     评论数量: {len(post_detail.get('comments', []))}")
        else:
            print("   - 没有博客文章可测试")
    except Exception as e:
        print(f"   ✗ 失败: {e}")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    test_api()