class TeleInfoModel:
    def __init__(self):
        self.__brief_introduce = None
        self.__name = None
        self.__director_list = []
        self.__actor_list = []
        self.__score = 0

    def set_name(self, n):
        self.__name = n

    def add_director(self, director):
        self.__director_list.append(director)

    def add_actor(self, actor):
        self.__actor_list.append(actor)

    def set_score(self, s):
        self.__score = s

    def add_brief_introduce(self, bi):
        self.__brief_introduce = bi

    def __repr__(self):
        director_list = '/'.join(self.__director_list)
        actor_list = '/'.join(self.__actor_list)
        s = "片名:{}\n导演:{}\n主演:{}\n评分:{}\n简介:{}\n".format(self.__name,
                                                         director_list, actor_list, self.__score,
                                                         self.__brief_introduce)
        return s
