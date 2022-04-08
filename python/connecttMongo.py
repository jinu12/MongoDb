import pymongo


class MongoConnection:
    def __init__(self):
        # MongoDb 서버에 접속해서 작업 할 수 있도록 MongoClient 객체를 생성
        # localhost = 127.0.0.1 == 현재 작업하고 있는 pc의 ip
        client = pymongo.MongoClient("localhost:27017")
        # database 접속
        self.db = client.get_database("sample")

    def getCollection(self):
        # collection 선택
        myboard = self.db["board"]
        # myboard 반환
        return myboard