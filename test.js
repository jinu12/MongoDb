// 1. dept가 인사인 document의 servlet 평균 구하기
db.test.aggregate([{$match:{dept:{$eq:"인사"}}},
                    {$group:{_id:"$dept", avg:{$avg:"$servlet"}}}])
// 2. java가 80점이 넘는 사람들의 부서별로 몇 명인지 구하기
db.score.aggregate([{$match:{java:{$gte:80}}},
                    {$group:{_id:"$dept",num:{$sum:1}}}])
// 3. 2번 결과를 인원수 데이터를 내림차순으로 정렬해 보세요.
db.score.aggregate([{$match:{java:{$gte:80}}},
                    {$group:{_id:"$dept",num:{$sum:1}}},
                    { $sort : { score : -1}}])
// 4. 앞에서 작업한 결과에 null인 document를 제외하세요

// 5. 다음과 같은 조건을 만족하는 document의 부서별 인원수를 구하세요
//    -  서울, 울산에 거주한 경험이 있고 헬로카봇을 본 적이 있다.
//    -  java 점수가 80점 이상이다.
//    - 위 두 개의 조건을 모두 만족해야 한다.
db.test.aggregate([{$match:{$and : [{"favorites.city":{$in : ["부산","울산"]}},
                    {"favorites.movie":"헬로카봇"},
                    {java:{$gte:80}}]}},
                    {$group:{_id:"$dept",num:{$sum:1}}}])
// 6. 다음과 같은 조건을 만족하는 document 들의 부서별로 java의 평균을 구하세요
//    - 인천에 거주한 경험이 있거나 겨울왕국을 본 경험이 있다.
//   -  java 점수가 90점 이상이다.
//   - 위 두 개의 조건은 둘 중에 하나만 만족하면 됩니다.
db.test.aggregate([{$match:{$and : [{$or : [{"favorites.city":"인천"},{"favorites.movie":"겨울왕국"}]},
                    {"favorites.movie":"헬로카봇"},
                    {java:{$gte:80}}]}},
                    {$group:{_id:"$dept",num:{$sum:1}}}])