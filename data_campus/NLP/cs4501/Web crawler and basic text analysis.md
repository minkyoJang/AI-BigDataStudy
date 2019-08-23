# Web crawler and basic text analysis

## How to represent a document?

- Represent by a String
  - 의미적으로 같은 단어를 다르게 인식하는 문제
  - 구조적, 언어적 정보를 담을 수 없다.
- Represent by a list of sentences
- Represent by a list of words <- 임마로 결정했다
  - Tokenize it first
    - 형태소 분석 등
  - Bag-of-Words representation

## Full text indexing

- Bag-of-Words representation
  - 모두 다 orthognal, independant 하다.
  - 순서에 관계없는 모델로, 생각보다 잘 나와요.
  - Statistical Analysis 기법
  - 가정 : 모든 단어들은 서로 독립이다. 
  - 장점 : 간단하다
  - 단점 : 구문 정보와 순서 정보를 잃어버린다.
  -	 **document representation**의 가장 빈번한 방법
- index document with all the occuring word
  - 장점
    -	 텍스트의 모든 정보를 유지(이론적으로는)
    -	 완전 자동화
  - 단점
    -	 vocabulary gap : cars vs. car
    - large storage. 공간 복잡도 증가 $O(V^N)$
      -	 Sparse Matrix
  - 해결책
    -	 construct controlled vocabulary

## Normalization

- word의 다른 형태들을 정규화
  - U.S.A -> USA
  - St.Louis -> Saint Louis
- Solution
  - Rule-based
  - Dictionary Based

## Stemming

## Stopwords

## Automatic text indexing

- in modern search engine

  - **no** stemming or stopword removal

  - more advanced NLP techniques applied
    - named entity recognition
    - Dependancy parsing

- 