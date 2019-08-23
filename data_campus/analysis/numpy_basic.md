>  [numpy 공식 basic 문서](https://docs.scipy.org/doc/numpy/user/basics.html)를 보며 정리하였습니다.

# Data types

## 

- 넘파이는 파이썬보다 다양한 숫자형 타입을 지원합니다. 이러한 타입들은 C와 크게 연관되어 있습니다.
- 이러한 숫자형 타입들은 `dtype`의 인스턴스입니다. 

- numpy array는 homogeneous하다.

# Array creation

## Introduction

array를 생성하는 5가지 매커니즘

1. 다른 파이썬 구조에서 변환하기
2. numpy array 생성 객체
3. 디스크에서 array 읽기
4. raw bytes로부터 생성
5. 특정 라이브러리 함수로 생성