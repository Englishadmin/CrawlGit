import request
import re
from teleplayinfo import TeleInfoModel


class MovieInfoManager(request.RequestDelegate):
    def __init__(self):
        self.__request = request.Request(self)

    def download(self, url):
        self.__request.request(url)

    def receive_data(self, data):
        self.analyze_data(data)

    def analyze_data(self, data):
        if data == None:
            return
        info = TeleInfoModel()
        pattern = '"name":(.*)"director": '
        ret = re.search(pattern, data, re.S)

        pattern = '"(.*)",.*"url"'
        ret = re.search(pattern, ret.group(1), re.S)
        # 存储电视名字
        info.set_name(ret.group(1))

        # 获取电视导演
        pattern = '"director":(.*)"author":'
        ret = re.search(pattern, data, re.S)
        # 分割字符串
        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            pattern = '"name": "(.*)"'
            ret = re.search(pattern, i, re.S)
            ls = ret.group(1).split(" ")
            # 添加一名导演
            info.add_director(ls[0])

        # 查找演员
        pattern = '"actor":(.*)"datePublished"'
        ret = re.search(pattern, data, re.S)
        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            pattern = '"name": "(.*)"'
            ret = re.search(pattern, i, re.S)
            ls = ret.group(1).split(" ")
            info.add_actor(ls[0])

        # 设置评分
        pattern = '"ratingValue": "(.*)"'
        ret = re.search(pattern, data)
        info.set_score(float(ret.group(1)))

        # 添加简介
        pattern = '"description":(.*)"@type": '
        ret = re.search(pattern, data, re.S)

        ls = ret.group(1).split('"@type"')
        info.add_brief_introduce(ls[0][:-1])

        print(info)
ls = [25754848, 27195020, 26849758, 30230682,30337138, 26660368, 26794191, 26738112,33422361, 30170894]
for i in ls:
    print(i)

path = "https://movie.douban.com/subject/25754848/"
mim = MovieInfoManager()
mim.download(path)
