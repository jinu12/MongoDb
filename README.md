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

use 데이터베이스명 → 작업할 데이터베이스를 생성(없는 경우 생성)

                                     작업하고 싶은 데이터베이스

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

## document 삭제
