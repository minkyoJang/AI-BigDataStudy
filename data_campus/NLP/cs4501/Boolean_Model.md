# Boolean Model

## Deficiency of Boolean model

- The query is unlikely precise
  - "over-constrained" 쿼리
    - relevant 문서를 찾을 수 없다
  - "under-constrained" 쿼리
    - over delivery
  - hard for users to specify constraints
- 정확하다 하더라도
  - 모든 유저가 같은 쿼리를 쓰지 않는다
  - all relevant documents are **not equally** important
- Relevance 의 정도가 중요하다

## Document Selection vs. Ranking

- ranking은 문서의 연관성을 수치화한다

## Notion of relevance

![1565328341610](C:\Users\skarn\AppData\Roaming\Typora\typora-user-images\1565328341610.png)

**vector space model** : ElasticSearch, google 다 이거 쓴다!

# Vector space Model

## Relevance = similarity

- 가정
  - 쿼리와 문서는 같은 형태이다
    - 쿼리는 문서로 여겨진다
- 키 이슈
  - 쿼리와 문서를 어떻게 표현?
  - 유사도 측정을 어떻게 정의할거냐
- 문서와 쿼리를 *concepts* vector를 통해 표현한다
  - 각 concept 은 하나의 차원으로 정의된다
  - *K concepts*는 고차원 공간에 정의된다
  - 벡터의 요소는 concept weight와 일치한다
- 측정
  - concept space에서 쿼리 벡터와 문서 벡터의 거리

## What the VS model doesn't say

- 'basic concepts'를 어떻게 정의/선택
  - 컨셉은 *orthogonal*하다고 가정된다
- 어떻게 가중치를 지정?

## 뭐가 좋은 concept냐?

- orthogonal
  - 선형 독립적인 기저 벡터
  - 'non-overlapping'
  - no ambiguity
- 가중치는 자동적으로 정확하게 할당된다

## 어떻게 가중치를 할당?

**개중요!**

- query side : 모든 term은 동일하게 중요한 것이 아니다
- doc side : 몇 term은 content에 대해 더 많은 정보를 가지고 있다.

어떻게?

- two basic heuristics
  - TF
  - IDF
- 

