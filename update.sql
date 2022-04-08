db.board.update(
		{no: 2},
		{$set: {comment: [
			     {no: 1, content: "comment01", count1: 1, count2: 2, writedate: new Date()},
			     {no: 2, content: "comment02", count1: 2, count2: 3, writedate: new Date()},
			     {no: 3, content: "comment03", count1: 3, count2: 4, writedate: new Date()},
			     ]
		        }
		 }
)