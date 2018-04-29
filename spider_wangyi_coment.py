import requests
import json
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Referer': 'http://music.163.com/song?id=551816010',
    'Origin': 'http://music.163.com',
    'Host': 'music.163.com'
}
# 加密数据直接拿过来使用
user_data = {
    'params': 'Z7f7ojzCsMPxwerVDMtCcisQkP2Xvw+BzSQnG8AuXQ6uuhpO6Q05jhRCVM+DWlVNtoZklTXbXeLfU7Fj2kvT3XRrHSeG4h7HooV+t5H1W6DOqJekZGXFpsgNNTVUYuYUEuZhOmaUz4NHkPxCMAubYpOeF1sYXyhDSk/NNS1j+a41BWMTWR3nNmfE1XGebbGm',
    'encSecKey': '33279bfc4689f4e1d87ddcae06a0a9363c6028ef6f567f89e8d5f1f55ff0c053de6b72f19802bcfd23a9fda1f8b566bc33e7950e1de3c75f79330bdc6f61a83e93033c5b7158ec62e8adfb774b06281c59b68cb1251e6839f08e5b32a802c71aa76716660d31e47536bc5da567d26a78070227cb3cf7cb84bd3c9c7a05c6367e'
}

response = requests.post(url, headers=headers, data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcomment in data['hotComments']:
    item = {
        'nickname': hotcomment['user']['nickname'],
        'content': hotcomment['content'],
        'likedCount': hotcomment['likedCount']
    }
    hotcomments.append(item)

# 获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

bar = Bar("热评中点赞数示例图")
bar.add("点赞数", nickname, liked_count, is_stack=True, mark_line=['min', 'max'], mark_point=['overage'])
bar.render()

content_text = " ".join(content_list)
wordcloud = WordCloud(font_path=r"C:\simhei.ttf", max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()