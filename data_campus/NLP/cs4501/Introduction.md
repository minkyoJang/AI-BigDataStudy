
> http://www.cs.virginia.edu/~hw5x/Course/IR2015/_site/lectures/

# Information Retrival. 정보 검색

- Stored Data로부터 Specific Data를 찾는 과정
- 정보를 효율적으로 탐색하고 우리의 수고를 덜어준다,

## Why information retrieval
- handing unstructured data

    - 실제 중요 정보는 대부분 unstructured data에 있다

## IR is not just about web Search
정보검색 뿐만 아니라
- Recommendation
- Question Answering
    - 대부분의 경우 검색을 기반으로 한다
    - stored data에서 질문과 유사한 정보를 answer한다
- Text Mining

## How to perform Informaion Retrival
- Crawler and indexer
    - indexer : 다양한 데이터들을 전처리, **어떻게 문서와 쿼리를 vectorize할 것인가!?**
- Document Analyzer
    - pagerank
    - document indexer
- Query Parser
- Ranking model
    
## Core concepts in IR
- Query representation
    - Lexical gap : say *vs* said
    - Semantic gap : ranking model *vs* retrieval method
- Document representation : `hadoop`
    - Specific data structure for efficient access
    - Lexical gap and semantic web
- Retrival model
    - find the **most relevant** documents
