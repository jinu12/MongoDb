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

## Database

- collection을 담고 있는 컨테이너

## Collection

- RDMS의 테이블과 비슷한 개념(스키마가 없다. - 정해진 구조가 없다.)

## document

- RDBMS에서

## Embedded do

- 테이블 조인과

## 기본명령어

show dbs → 데이터베이스의 리스트를 확인

use 데이터베이스명 → 작업할 데이터베이스를 생성(없는 경우 생성), 작업하고 싶은 데이터베이스

db → 현재 작업 중인 데이터베이스를 확인

show collections → 컬렉션 목록 확인(select

db.createCollection(”컬렉션명”) → 컬렉션 상ㅌ

## document 삽입(데이터insert)

mongodb는 데이터를 json 방식으로 관리

1. insert 메소드
- db.컬렉션명.insert({필드명1:펄드값1,필드명2:필드값2...})
1. 배열
- json의 배열과 동일하게 표현

    {필드명1:[”값1”,”값2”,”값3”,”값4”]}

## document 조회

- 컬렉션에 저장된 document를 조회
- db.컬렉션명.find()
    - select * from 테이블명과 도일
    - 컬렉션의 모든 document를 조회

## document 수정
- update
- CRUD를 위한 메소드는 json 형식으로 정의해야 한다.
- 구문

```sql
db.collection명.update(<filter>,-조건(sql, update문의 where절)
											 <update>,-set절(변경할 필드와 값)
											 <options>)-update위해서 설정해야 하는 내용
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
--	db.컬랙션명.update({조건필드:조건값},{$set:{업데이트할 컬럼의 정보}})
--	db.컬랙션명.update({id:"kim"},{$set:{pass:"123456789"}})
--  업데이트할 필드가 존재하지 않으면 새로 추가한다.
```

- options(업데이트 옵션)
    
    ⇒ 업데이트 할 때 기본으로 설정된 기능을 변경하고 싶을 때 사용
    
- 배열 데이터를 수정
    - 배열데이터 추가하기

```powershell
db.score.update({id:"jang"},{$set:{favorite:{city:["서울","안산"],movie:["겨울왕국2","변호인"]}}})
```

- 배열데이터를 수정하는 경우에 업데이트연산자를 이용

[배열 업데이트 연산자]

- $push : 배열에 요소를 추가(중복을 허용)

```powershell
db.score.update({id:"jang"},{$push:{favorite.city: "안산"}})
```

- $addToSet : 배열에 요소를 추가(중복을 허용x)

```powershell
db.score.updte({id:"jang"},{$addToSet:{favorite.city:"안산"}})
```

- $pop :
    
    배열의 첫 번째 요소나 마지막 요소를 제거
    
    pop에 옵션으로 1을 정의하면 배열의 마지막 요소를 제거하고 -1을 정의하면 배열의 첫 요소를 제거
    

```powershell
db.score.update({id:"jang"},{$pop:{"favorites.city":1}})
db.score.update({id:"jang"},{$pop:{"favorites.city":-1}})
```

- pull : 배열의 요소들 중 원하는 아이템을 제거

```sql
db.score.update({id:"jang"},{$pull:{"favorites.city":"천안"}})
-- each : addToEt이나 push에서 사용할 수 있다. 배열에 여러 개의 요소를 추가할 때 사용
db.score.update({id:"jang"},{$push:{"favorites.city":["천안","가평","수원"]})
-- 배열에 요소로 여러 개가 추가되는 것이 아니라 별도의 배열이 삽입
-- 여러 개의 요소를 추가하되는 경우 &each연산자를 사용해야 한다.
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"]}}})
-- $sort: 정렬 (1:오름차순,-1:내림차순)
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"],$sort:1}}})
db.score.update({id:"jang"},{$push:{"favorites.city":{each:["천안","가평","수원"],$sort:-1}}})
```

- pullAll : 배열의 요소를 제거(여러 개를 조건으로 정의해서 제거하기)

```powershell
db.score.update({id:"jang"},{$pullAll:{"favorites.city":["천안","가평"]}})
```
- 예제

```sql
-- 배열데이터 업데이트
-- 1. song,jang,hong에 다음과 같은 값을 가질 수 있도록 배열로 필드를 추가하세요
--    song :  history (영업1팀, 총무, 기획실)
--    jang:    history(전략팀,총무,전산)
--    hong :  history(영업1팀, 기획실,전산)
db.score.update({id:"song"},{$set:{"history":["영업1팀","총무","기획실"]}})
db.score.update({id:"jang"},{$set:{"history":["전략팀","총무","전산"]}})
db.score.update({id:"hong"},{$set:{"history":["영업1팀","기획실","전산"]}})
-- 2. song의  document history에 자금부를 추가하세요
db.score.update({id:"song"},{$addToSet:{"history":"자금부"}})
-- 3. jang의 document의 history에 마지막 데이터를 제거하세요
db.score.update({id:"jang"},{$pop:{"favorites.city":1}})
-- 4. servlet데이터가 100점인 모든 document에 bonus를 3000을 추가하세요. 기존데이터가 존재하면 증가되도록 구현하세요
 db.score.update({servlet:100},{$inc:{bonus:+3000}},{multi:true})
-- 5. song의 lang.ms에 "visual basic","asp",".net"을 한꺼번에 추가하세요
db.score.update({id:"song"},{$set:{"lang.ms":["visual basic","asp",".net"]}})
```
## document 삭제
