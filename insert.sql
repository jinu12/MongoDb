db.createCollection("board")
for(var i=0;i<=4;i++) {
	db.board.insertOne({no:i,id:"id"+i,title:"title"+i,count:0,wrtiedate:new Date()});
}