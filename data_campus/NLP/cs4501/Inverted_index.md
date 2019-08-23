# Inverted Index

## Sorting-based inverted index construction

![1565318392286](C:\Users\skarn\AppData\Roaming\Typora\typora-user-images\1565318392286.png)

## Search within in inverted index

- 쿼리를 어떻게 처리할까?
  - parse query syntax
    - ex) range OR apple
  - 문서처리와 같은 과정으로 쿼리도 처리해야한다.
    - Tokenization -> normalization -> stemming -> stopwords -> removal
- 과정
  - 딕셔너리에서 쿼리 term을 찾는다
  - posting list를 탐색
  - Boolean operation
    - AND, OR, NOT

### phrase query

- documents 에 term position 정보가 있어야 한다.
  - inverted index에 저장하자
- 