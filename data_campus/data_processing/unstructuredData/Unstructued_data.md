# HTTP, DOM

## HTTP

- HTTP는 무적권 **HTML**을 response 한다.
  - 우리는 HTML을 parsing해야 한다
- Simple *request - response* protocol layered on tcp/ip

URL

- protocol : http
- Server : www.example.com
- Port : 80
- File : index.html

Request

- Header
  - Get : /index.html
  - Host : www.example.com
  - Accept : text/html, \*/\*
  - Accept-Language : en-us
  - Accept-Charset : utf-8
  - User-Agent : 클라이언트의 환경
  - Connection : keep-alive
- Body (optional) : post에서 쓴다

HTTP Method

- *safe* method
  - get
  - head
- Message with *Body*
  - put
  - post
  - patch
  - trace
- etc
  - trace
  - options
  - delete

REST

- REST : Representational State Transfer
- CRUD : Create, Read, Update, Delete
- RESTful
  - GET /movies 
    - get list of movies
  - GET /movies/:id
    - find a movie by its ID
  - POST /movies
    - Create a new movie
  - PUT /movies
    - Update movie
  - DELETE /movies
    - delete movie

## Crawling / Scrapping

### Legal Issues

- opt in : 정보수집을 **명시적으로 동의**할 때에만 정보수집 **가능**; *whitelist*
- opt out : 정보수집을 **명시적으로 거부**할 때에만 정보수집 **중단**; *blacklist*
  - 합법이다!
    - 검색엔진 , 가격비교 등 공익 목적이다
  - 위법이다! 
    - 사이트 운영자의 의사에 반하지 않으면 합법이다.
    - 트래픽, 이용방침, 개인정보, 지적재산권 문제가 있다.
- robots.txt
  - bot 접근을 제어하기 위한 규약
- 어떤 사이트를 수집하느냐보다 어떤 데이터를 수집하느냐가 문제
  - 접근 제약 규칙 준수
  - 사이트에 부담 지양
  - 사이트 이용방침(약관) 준수
  - 지적재산권 침해 여부 주의
  - 민감 정보 수집 주의

#### Urllib

[urllib을 이용한 크롤링](./HTTP, DOM)

## DOM

### BeautifulSoup

[노트북](./DOM)

- ```python
  find_all(name, attrs, recursive, string, limit, **kwargs)
  find_all(recursive=false) # 자식만 찾는다.
  ```



# CSS, XPath, 공공데이터

## Selector

- ```css
  selector Declaration
  h1       {color:red; font-size:10;}
          property:value property:Value
  ```

- id는 단 하나만 존재

- 부가적으로 class를 쓸 수 있다. 다중상속이 가능하다. `.`중첩하여 접근 가능
- ID : `#어쩌고`
- CLASS :`.어쩌고`
- 태그 : 태그
- 자손 : 공백
- 자식 : `>`

# Crawling

# Scrapping

# DHTML, AJAX

# Cookie, Session