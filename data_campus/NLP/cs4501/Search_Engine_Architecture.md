# Search Engine Architecture

## Core IR concepts

- Information Need
- Query
- Document
- Relevant

> **"Rank documents by their relevance to the information need"**

## Key Components

- Web Crawler
  - automatic program
- Document analyzer & indexer
- Query Parser
- Ranking Model

> 이 동네에서는 accuracy 안 쓴다. 다른 성능 평가 지표 있음

- Search query logs
- User modeling

## Discussion : Browsing vs. Querying

- Browsing - yahoo did before
  - 시스템이 정보를 조직하여 표현해주는 방식.
  - 사람은 표현된 형태의 결과를 보고 찾아다닌다.
- Querying - google does
  - 사용자로부터 입력받은 쿼리로부터 어떤 documents 가 relevant 한가

## Pull vs. Push

- pull
  - 내가 입력한 정보로부터 데이터를 가져옴
  - ad hoc 
    - 데이터는 그대로 있고 query를 바꿔 나에게 맞는 데이터를 가져온다.
- push
  - 세팅된 항목들에 의해 데이터를 알아서 보여줌. ex)news

