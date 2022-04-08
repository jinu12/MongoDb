## mongo 시작

1. 데이터를 저장할 파일 생성

```powershell
C:\example\data
```

1. mongodb 서버를 실행

```powershell
mongod -- dbpath C:\example\data
```

1. mongodb 클라이언트를 실행해서 데이터를 저장, 조회, 수정, .....

```powershell
mongo
```
## 정의

- Document oriented 데이터베이스
- 특정한 종류의 애플리케이션을 더 쉽고 더 빠르게 데이터 통합을 가능
- 아페로 GPL과 아파치 라이센스를 를 결합하여 공개된 몽고DB는 오픈 소스 소프트웨어

## RDBS 용어 비교

- Database : collection을 담고 있는 컨테이너
- Collection : RDMS의 테이블과 비슷한 개념이지만, 스키마(정해진 구조)가 없다.
- Document : RDBMS에서의 row(record) 와 비슷한 개념
- Field : RDBS 에서의 column(field)와 비슷한 개념
- _id field : RDMBS의 primary key와 비슷한 개념
- Embedded document: RDBMS에서의 table join 과 비슷한 개념
- [ ] : 배열
- { } : 오브젝트 (name과 value를 포함)

## 기본명령어

db.hel() → 명령어 리스트 출력

show dbs → 데이터베이스의 리스트를 확인

use 데이터베이스명 → 작업할 데이터베이스를 생성(없는 경우 생성)

                                     작업하고 싶은 데이터베이스

db → 현재 작업 중인 데이터베이스를 확인

show collections →  작업 중인 DB 안에 collection 리스트 출력

## Collection 관련 명령어

db.createCollection(”컬렉션명”) → 현재 작업 중인 DB 안에 컬렉션 생성

db.컬렉션명1.renameCollection(”컬렉션명2”) → collection 이름 변경(컬렉션명1→컬렉션명2)

## Document 삽입(데이터insert)

mongodb는 데이터를 json 방식으로 관리

컬렉션이 존재하지 않아도 insert를 하면 자동으로 컬렉션이 생성되고 insert 실행

_id field를 입력하지 않으면 자동으로 생성 : 고유값을 지정하고 12byte

1. insert 메소드
- db.컬렉션명.insert({필드명1:펄드값1,필드명2:필드값2...})
- 필드 값이 문자일 경우 “ “로 감싸야 한다.
1. 배열
- json의 배열과 동일하게 표현

    {필드명1:[”값1”,”값2”,”값3”,”값4”]}

## Document 조회

- 컬렉션에 저장된 document를 조회
1. 모든 document 조회
    - db.컬렉션명.find() ⇒ SQL 의 SELECT * FROM 테이블명과 동일
2. 조건에 맞는 document 조회
    - db.컬렉션명.find(조건)⇒ SQL의 SELECT * FROM 테이블명 WHERE 조건과 동일
    - 조건을 주는 방식은 SQL처럼 다양하다.

```json
db.emp.find({id:1101})
```

[구문]

db.collection명.find(조건, 조회할 피드에 대한 정보를 정의)

1. query(조건)
    - 조회할 필드에 대한 정보를 json 형식으로 표기
    
     [query 연산자 - 비교연산자]
    
     $eq : 주어진 조건의 값과 일치(==)
    
     $gt : 조건값보다 큰 값(greater than >)
    
     $gte : 조건값보다 크거나 같은 값(greater than or equal : ≥)
    
     $lt : 조건값보다 작은 값(less than : <)
    
     $lte : 조건값보다 작거나 같은(less than or equal : ≤)
    
     $ne : 조건값과 일치하지 않는(not equal)
    
     $in : selec문의 in 연산자와 동일 - 조건 값이 여러 값(배열)과 비교해서 일치하는지
    
     $nin : 배열에 명시한 값들과 비교해서 일치하지 않는 값을 확인
    

```json
db.score.find({java : {$eq : 88}})
db.score.find({java : {$gt : 90}})
db.score.find({java : {$gte : 90}})
db.score.find({java : {$lt : 90}})
db.score.find({java : {$lte : 90}})
db.score.find({java : {$ne : 90}},{id:1,name:1,dept:1,addr:1,java:1)
db.score.find({java : {$in : [88,90]}})
db.score.find({java : {$nin : [97,98]}})
// 90이상 100이하 (조건을 여러개 줄 수 있다)
db.score.find({java : {$gte : 90,$lte : 100}})
```

1. logic(논리)
    - 두 개 이상의 필드에서 조건을 적용
    - 조건은 배열로 정의
    
     $and  : 두 개 이상의 조건이 모두 true → true
    
     $not :  조건을 만족하지 않는 document와 조건을 판단할 필드가 존재하지 않는 document를 모두 조회 단일 조건
    
     $nor :  정의한 모든 조건을 만족하지 않는 document를 조회
    
     $or : 두 개 이상의 조건 중 하나라도 true → true
    
    ```json
    db.score.find({$and:[{dept:"인사"},{addr:"인천"}]})
    db.score.find({java : {$not:{$lte: 90}}})
    db.score.find({$nor:[{dept:"인사"},{addr:"인천"}]})
    db.score.find({$or:[{dept:"인사"},{addr:"인천"}]})
    db.score.find({$and:[{dept:"인사"},{addr:"인천"}]})
    db.score.find({$and:[{dept:"인사"},{addr:"인천"}]})
    db.score.find({$and:[{dept:"인사"},{addr:"인천"}]})
    ```
    

[자바스크립트 명령어를 조건으로 사용하기]

$where : “자바스크립트명령”

```json
var alldata = db.score.find()
var size = db.score.find().count()
while(alldata.hasNext()){
var one = alldata.next() // cursor에서 dcoument 하나 꺼내서 반환
one.num = 10000 // 
db.score.save(one)
}
```

[Cursor 메소드]

count() : cursor안에 포함된 document의 갯수를 반환

sort({필드명:옵션값}): 정렬  오름차순 1 내림차순 -1

limit(숫자) : limit에 정의한 갯수만큼 document를 조회

skip(숫자) : skip에 정의한 갯수만큼 document를 제외하고 출력 

 

```json
var alldata = db.score.find()
var size = db.score.find().count()
while(alldata.hasNext()){
 var one = alldata.next()
 one.num = 10000
 db.score.save(one)
}

db.getCollection("score").distinct("필드명")
// 필드의 중복을 제거한 값을 배열로 리턴
db.getCollection("score").distinct("필드명").length
// 사이즐를 리턴
```

[정규표현식]

문자열에서 패턴(문자, 기호를 이용해서 특정 문자를 찾는다. 문자나 기호는 내부적으로 의미를 갖고 있다. 거의 대부분의 언어에서 동일하게 작업)과 일치하는 문자가 있는지 찾을 수 있도록 지원

^ : 문자열의 시작

$ : 문자열의 종료

. : 임의의 한 글자 의미(한글, 영문 상관없음)

 | : or의 의미

i : 대소문자 구분없이 조회

/값/ : RDMS의 like연산과 동일 ⇒ where addr like %값%과 동일

A-Z : 영문자대문자

a-z : 영문자소문자

가-힇 : 한글

[ ]: 횟수나 범위 체크 - k _

{} : 횟수나 범위 체크 - k {5} : K가 5번 반복, a{3,5} : a

```json
db.score.find({id:/kang/})
db.score.find({id:/k/})
db.score.find({id:/^k/})
db.score.find({id:/k?/})
db.score.find({id:/[a-f]/})
db.score.find({id:/[^a-f]/})
db.score.find({id:/|a-Z|/},{id:1,name:1})
```

db.score.find({id:/[a-Z]/},{id:1,name:1})

[Aggregation]

- Aggregation framework와 map
1. 연산자
    - $match: where절, having 절과 같은 개념
    - $group : group by
    - $sort : order by
    - $sum : 총합
    - $avg : 평균
    - $max : 최대값
2. 형식
    
     db.collection명.aggregate(aggregation연산들을 이용해서 명령어를 정의)
    
     → 여러 개를 사용하는 경우 배열로 표현
    
- 예제

```json
// addr별 인원수
db.score.aggregate([{$group:{myaddr:"$addr", num:{$sum:1}}}]) // X (필드명은_id)
db.score.aggregate([{$group:{_id:"$addr", num:{$sum:1}}}]) // addr필드에 저장된 값을 가져올 것이므로 $와 함께 사용
// RDBMS
// select addr as myaddr, count(id) num
// from score
// gorup by addr
// dept별 인원수
db.score.aggregate([{$group:{_id:"$dept", num:{$sum:1}}}])
// dept별 java 평균
db.score.aggregate([{$group:{_id:"$dept", avg:{$avg:"$java"}}}])
// dept별 servlet 합계
db.score.aggregate([{$group:{_id:"$addr", sum:{$sum:"$servlet"}}}])
// 조건을 적용한 예제
// $match를 써서 조건을 적용
// java가 80점 넘는 사람들이 부서별로 몇 명인지 구하기
// select dept,count(id)
// from score
// where java>= 80
// group by dept
db.score.aggregate([{$match:{java:{$gte:90}}},{$group:{_id:"$dept",num:{$sum:1}}}])
db.test.find({"favorites.city":{$in :["서울","인천"]}})
db.test.find({$or : [{"favorites.movie":"쉬리"},{dept:"인사"}]})
db.test.find({$and : [{"favorites.city":{$in : ["부산","울산"]}},{"favorites.movie":"헬로카봇"}]})
// 1. dept가 인사인 document의 servlet 평균 구하기
db.test.aggregate([{$match:{dept:{$eq:"인사"}}},{$group:{_id:"$dept", avg:{$avg:"$servlet"}}}])
// 2. java가 80점이 넘는 사람들의 부서별로 몇 명인지 구하기
db.score.aggregate([{$match:{java:{$gte:80}}},{$group:{_id:"$dept",num:{$sum:1}}}])
// 3. 2번 결과를 인원수 데이터를 내림차순으로 정렬해 보세요.
db.score.aggregate([{$match:{java:{$gte:80}}},{$group:{_id:"$dept",num:{$sum:1}}},{ $sort : { score : -1}}])
// 4. 앞에서 작업한 결과에 null인 document를 제외하세요

// 5. 다음과 같은 조건을 만족하는 document의 부서별 인원수를 구하세요
    -  서울, 울산에 거주한 경험이 있고 헬로카봇을 본 적이 있다.
    -  java 점수가 80점 이상이다.
    - 위 두 개의 조건을 모두 만족해야 한다.
db.test.aggregate([{$match:{$and : [{"favorites.city":{$in : ["부산","울산"]}},{"favorites.movie":"헬로카봇"},{java:{$gte:80}}]}},{$group:{_id:"$dept",num:{$sum:1}}}])
// 6. 다음과 같은 조건을 만족하는 document 들의 부서별로 java의 평균을 구하세요
    - 인천에 거주한 경험이 있거나 겨울왕국을 본 경험이 있다.
   -  java 점수가 90점 이상이다.
   - 위 두 개의 조건은 둘 중에 하나만 만족하면 됩니다.
db.test.aggregate([{$match:{$and : [{$or : [{"favorites.city":"인천"},{"favorites.movie":"겨울왕국"}]},{"favorites.movie":"헬로카봇"},{java:{$gte:80}}]}},{$group:{_id:"$dept",num:{$sum:1}}}])
```

## Document 수정

- update
- CRUD를 위한 메소드는 json 형식으로 정의해야 한다.
- 구문

```json
// db.collection명.update(<filter>,-조건(sql, update문의 where절)
// <update>,-set절(변경할 필드와 값) 
// <options>)-update위해서 설정해야 하는 내용
<filter>
업데이트를 하기 윈한 조건
{조건필드:값.....}

<update>
업데이트 연산자와 함께 명시
업데이트할 필드의 값
{변경할 필드:값....}
db.emp.update({id:"kim"},{pass:"123456789"})
             ----------- -------------------
              filter          update
[업데이트 연산자]
$set : 해당 필드의 값을 변경
db.emp.update({id:"kim"},{pass:"123456789"})
//	db.컬랙션명.update({조건필드:조건값},{$set:{업데이트할 컬럼의 정보}})
//	db.컬랙션명.update({id:"kim"},{$set:{pass:"123456789"}})
//  업데이트할 필드가 존재하지 않으면 새로 추가한다.
```

- options(업데이트 옵션)
    
    ⇒ 업데이트 할 때 기본으로 설정된 기능을 변경하고 싶을 때 사용
    
- 배열 데이터를 수정
    - 배열데이터 추가하기

```json
db.score.update({id:"jang"},{$set:{favorite:{city:["서울","안산"],movie:["겨울왕국2","변호인"]}}})
```

- 배열데이터를 수정하는 경우에 업데이트연산자를 이용

[배열 업데이트 연산자]

- $push : 배열에 요소를 추가(중복을 허용)

```json
db.score.update({id:"jang"},{$push:{favorite.city: "안산"}})
```

- $addToSet : 배열에 요소를 추가(중복을 허용x)

```json
db.score.updte({id:"jang"},{$addToSet:{favorite.city:"안산"}})
```

- $pop :
    
    배열의 첫 번째 요소나 마지막 요소를 제거
    
    pop에 옵션으로 1을 정의하면 배열의 마지막 요소를 제거하고 -1을 정의하면 배열의 첫 요소를 제거
    

```json
db.score.update({id:"jang"},{$pop:{"favorites.city":1}})
db.score.update({id:"jang"},{$pop:{"favorites.city":-1}})
```

- pull : 배열의 요소들 중 원하는 아이템을 제거

```json
db.score.update({id:"jang"},{$pull:{"favorites.city":"천안"}})
// each : addToEt이나 push에서 사용할 수 있다. 배열에 여러 개의 요소를 추가할 때 사용
db.score.update({id:"jang"},{$push:{"favorites.city":["천안","가평","수원"]})
// 배열에 요소로 여러 개가 추가되는 것이 아니라 별도의 배열이 삽입
// 여러 개의 요소를 추가하되는 경우 &each연산자를 사용해야 한다.
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"]}}})
// $sort: 정렬 (1:오름차순,-1:내림차순)
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"],$sort:1}}})
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"],$sort:-1}}})
```

- pullAll : 배열의 요소를 제거(여러 개를 조건으로 정의해서 제거하기)

```powershell
db.score.update({id:"jang"},{$pullAll:{"favorites.city":["천안","가평"]}})
```

- 예제

```json
// 배열데이터 업데이트
-- 1. song,jang,hong에 다음과 같은 값을 가질 수 있도록 배열로 필드를 추가하세요
//    song :  history (영업1팀, 총무, 기획실)
//    jang:   history(전략팀,총무,전산)
//    hong :  history(영업1팀, 기획실,전산)
db.score.update({id:"song"},{$set:{"history":["영업1팀","총무","기획실"]}})
db.score.update({id:"jang"},{$set:{"history":["전략팀","총무","전산"]}})
db.score.update({id:"hong"},{$set:{"history":["영업1팀","기획실","전산"]}})
// 2. song의  document history에 자금부를 추가하세요
db.score.update({id:"song"},{$addToSet:{"history":"자금부"}})
// 3. jang의 document의 history에 마지막 데이터를 제거하세요
db.score.update({id:"jang"},{$pop:{"favorites.city":1}})
// 4. servlet데이터가 100점인 모든 document에 bonus를 3000을 추가하세요. 기존데이터가 존재하면 증가되도록 구현하세요
 db.score.update({servlet:100},{$inc:{bonus:+3000}},{multi:true})
// 5. song의 lang.ms에 "visual basic","asp",".net"을 한꺼번에 추가하세요
db.score.update({id:"song"},{$push:{"lang.ms":{$each:["visual basic","asp",".net"]}}})
// db.score.update({id:"song"},{$set:{"lang.ms"::["visual basic","asp",".net"]}})

// 1. 
db.createCollection("board")
// 2. 
for(var i=1;i<=5;i++) {
	db.board.insertOne({no:i,id:"id"+i,title:"title"+i,count:0,wrtiedate:new Date()});
}
db.board.find().pretty() -- 데이터 체이닝
// 3.
db.board.update({no:2},{$set : {comment : [{"no" : 0, "content":"one","count1":0,"count2":0,"writedate":new Date()}]}})
db.board.update({no:2},{$set : {comment : [{"no" : 1, "content":"two","count1":0,"count2":0,"writedate":new Date()}]}})
db.board.update({no:2},{$set : {comment : [{"no" : 2, "content":"three","count1":0,"count2":0,"writedate":new Date()}]}})
```

## Document 삭제

- remove

```json
db.collection명.remove({조건})
=>update와 remove는 find에서 적용한 조건을 동일하게 사용할 수 있다.
```

<h2> Python MongoDb 연결</h2>
<br>
<a href = "https://github.com/jinu12/MongoDb/blob/main/python/__ConnectionPython">바로가기</a>

