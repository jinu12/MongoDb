from boardMongo import BoardMongo

if __name__ == "__main__":
    obj = BoardMongo()
    obj.getBoardData()
    obj.getBoard(3)
    obj.remove(3)
    obj.write(3, "id3", "title3", 0)
    obj.updateBoard(4, "update")
    obj.search("title1")