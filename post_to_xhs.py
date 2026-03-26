import requests
 
def post_to_xhs(content, image_path=None):
url = "https://www.xiaohongshu.com/api/sns/web/v1/note/draft/create"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"Cookie": "19cfebe756684si7muoudamp2wilid69xnka1eioe50000173736"
}
data = {
"title": "自动发布的标题",
"desc": content,
"category": "life"
}
response = requests.post(url, headers=headers, data=data)
return response.json()
 
if name == "main":
post_content = "今天分享一个自动发布的小技巧~"
post_to_xhs(post_content)
