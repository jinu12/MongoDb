from datetime import datetime

from connecttMongo import MongoConnection


class BoardMongo:
    def __init__(self):
        # mongoConnection 객체 생성
        mongo = MongoConnection()
        self.collection = mongo.getCollection()

    # boardConnection의 모든 value값 출력
    def getBoardData(self):
        boardlist = self.collection.find()
        print("===========all===========")
        for mydoc in boardlist:
            print(mydoc)

    # board 번호에 맞는 boardCollection 출력
    def getBoard(self, num):
        boardlist = self.collection.find({"$eq": {"no": num}})
        print("===========no============")
        for mydoc in boardlist:
            print(mydoc)

    # 매개변수를 입력받아 insert
    def write(self, no, id, title, count):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("===========insert============")
        my_dict = [{"no": no}, {"id": id}, {"title": title}, {"count": count}, {"date": date}]
        self.collection.insert_many(my_dict)

    # 번호를 입력받아 remove
    def remove(self, num):
        self.collection.delete_one({"no": num})
        print("===========remove============")
        boardlist = self.collection.find()
        for mydoc in boardlist:
            print(mydoc)

    # 번호와 타이틀을 입력받아 update
    def updateBoard(self, num, title):
        query = {"no", num}
        value = {"$set", {"title": title}}
        self.collection.update_many(query, value)
        print("===========update============")
        boardlist = self.collection.find()
        for mydoc in boardlist:
            print(mydoc)

    # 입력받은 매개변수가 title 또는 context와 같으면 출력
    def search(self, context):
        print("===========update============")
        result = self.collection.find({"$or": [{"title": context}, {"context": context}]})
        for mydoc in result:
            print(mydoc)


