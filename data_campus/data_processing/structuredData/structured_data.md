##### 2주차

정형 데이터 수집 / 전처리 (SQL, ORM, XML, JSON)

# DBMS

## 데이터베이스 개요

- Unstructured (semi-Structured) 80% <- 관심 가져야 한다.

- Structured 20%

#### Data vs Information

- Data
  - raw facts
  - no context
  - just numbers and text
- Information
  - processed data
  - data with context
  - value-added data

#### what is database?

- a collection of interrelated data
- a set of integrated, stored, shared and operational data

#### 데이터베이스 조건

- **통합** 
  - 동일한 데이터가 중복되지 않도록 구성
  - 최소한의 중복 또는 통제된 중복만 허용
- 저장
  - 컴퓨터로 접근 가능한 물리적 매체 저장
- 공유
  - 공동으로 소유하고 유지하며 이용하는 데이터
- 운영
  - 존재 목적이나 기능 수행에 꼭 필요한 데이터 집합

#### 데이터베이스 특징

- 실시간 접근성
  - 데이터들 간의 밀접한 관계로 연결
  - 중복 데이터를 배제하도록 지양
  - 사용자의 어떤 요구에도 즉각 응답
- 계속적인 변화
  - 현실 세계의 상태를 정확히 반영
  - 동적으로 삽입 / 삭제 / 수정하여 현재의 데이터 유지
- 동시 공유 가능
  - 여러 사용자들이 동시에 이용
  - 같은 시간에 같은 데이터 접근하여 이용
- 내용에 의한 참조 가능
  - 저장된 주소나 위치에 의해서 참조하지 않고
  - 사용자가 요구하는 데이터의 내용 / 값에 따라 참조

#### what is DBMS?

- a collection of programs
- manage the database structure
- controls access to the data stored in the database

#### DBMS의 역할

- create databases
- insert, update and delete data
- sort and query data
- create form and report

#### DBMS 역할과 장점

- improved data sharing
- Improved data security
- Minimized data inconsistency
- Improved data access
- Improved decision making
- Increased end-user productivity
- Reduce application development time

#### DBMS 종류

- 계층형 모델
  - 트리 형태로 표현(1:N)
  - 개체를 노드, 개체 집합들 사이의 관계를 링크로 표현
- 네트워크형 모델
  - 그래프 형태로 표현 (N:M)
  - 각 개체가 여러 관계를 가질 수 있음
- **관계 데이터 모델**
  - 개체를 테이블, 개체 집합들 사이의 관계를 공통 속성으로 연결
- **객체 관계 모델**
  - 속성-관계
  - 개체-관계

> ORM : 관계 데이터 모델을 객체 관계 모델처럼 쓸 수 있게 함

## RDBMS

#### why use RDBMS

- 데이터 안정성
- 동시 접근성
- **장애 허용성**(Falut tolerance)
- 데이터 무결성
- 데이터 확장성
- 데이터 보고서

#### RDBMS Concepts

#### 개체 관계 모델 (E-R Model)

- 개체(Entity)
- 관계(Relationship)
- 속성(Attribute)
- 기본키(Primary key)

#### 예제) 교수-학생 ER 모델

- 이항 관계
- 삼항 관계

## SQL

- Structured Query Language

#### SQL명령

- 데이터 정의 언어 DDL
  - CREATE, DROP, ALTER, TRUNCATE
- 데이터 조작 언어 DML
  - INSERT, UPDATE, DELETE, SELECT
- 데이터 제어 언어 DCL
  - GRANT, REVOKE

#### SQL 구문

- 문 Statement
- 절 clause
- 식 Expression
- 술어 Predicate

#### Data Type

- Boolean
  - True or False
- Character
  - CHAR : 고정 길이
  - VARCHAR : 가변 길이
- Exact numeric
  - NUMERIC
  - DECIMAL
  - INTEGER
  - SMALLINT
  - BIGINT
- Approximate numeric
  - REAL
  - FLOAT
  - DOUBLE
- Datetime(DATE, TIME) / Large Object (CLOB, BLOB)

#### DDL 데이터 정의 언어

- CREATE

```sql
CREATE TABLE [table name] ([column definitions])[table parameters]
```

```sql
CREATE TABLE employee(
	id	INTEGER	PRIMARY KEY,
    first name	VARCHAR(50)	not null,
    dateofbirth	DATE	not null
)
```

#### 

- DROP

```sql
DROP objecttype objectname

DROP TABLE employees;
```

- Truncate

```sql
TRUNCATE TABLE table_name; //autoincrement 등을 싹 다 초기화
```

- ALTER

```sql
ALTER TABLE table_name
ADD column_name datatype;
```



#### DML 데이터 관리 언어

- INSERT

```sql
INSERT INTO table (col1 [,col2, col3...]) VALUES (value1, [value2, value3...])
```

- **SELECT**

```sql
SELECT col1, col2 ...
FROM table_name;
```

```sql
SELECT [ALL|DISTINCT] 컬럼명
FROM 테이블명
[WHERE 조건식]
[GROUP BY 컬럼명 [HAVING 조건식]]
[ORDER BY 컬럼명]
GROUP BY 컬럼명
ORDER BY 컬럼명
```

- UPDATE

```sql
UPDATE table_name
SET col1 = val1, col2 = val2, ...
WHERE condition
```

- DELETE

```sql
DELETE FROM table_name
WHERE condition;
```

- **JOIN** 
  - INNER, LEFT, RIGHT, FULL OUTER JOIN

```sql
SELECT 컬럼명
FROM 테이블명
INNER JOIN 테이블명 ON 조건식
```

## SQLite

[주피터 노트북 참고](./RDBMS.ipynb)

# ORM, RE

## ORM 소개

Object Realtional Mapping

객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것을 말한다.

테이블 간의 관계보다 **데이터베이스에 대한 처리**에 집중

- 객체-관계로 접근

```java
public class Question{
    private long qid;
    private String title;
    [...]
    
    public processTags(String Tag){
    }
}

public class Tag{
    private long tid;
    private String tag;
    [...]
    
    public add(String tag){
    }
}
```

| Web Framework | None           | Flask        | Flask      | Django     |
| ------------- | -------------- | ------------ | ---------- | ---------- |
| ORM           | **SQLAlchemy** | SQLAlchemy   | SQLAlchemy | Django ORM |
| connector     | (builtin)      | Mysql-python | psycopg    | psycopg    |
| RDBS          | SQLite         | MySQL        | PostgreSQL | PostgreSQL |

## SQLAlchemy

- Architecture
- SQLAlchemy CORE
  - Engine
    - Starting point for any SQLAlchemy application
  - Dialect
    - communicate with various types of DBAPI implementations and databases
- [실습 노트북](./ORM, RE.ipynb)

## Regular Expression

- Why use RE?
  - 무지하게 빨라여
  -  NLP 쓰게 되면 필수이다
  - String searching / input validation
- But, There is a **learning curve**

General concepts

Meta Characters

re

- re.compile
  - 패턴을 객체로 바꿔줌
- re.search
  - 문자열 전체를 검색		
- re.match
  - 처음부터 검색. `^` 필요 없다.
- re.split
  - 특정 패턴이 나오면 자른다

# JSON, XML

## JSON

why use JSON?

- 사람이 읽기도 좋고, machine이 읽기도 좋다.

- 무적권 `"` 써야 한다.

Easy processing

Storage size

- character 수가 xml보다 매우 적다.

JSON API

JSON Data Type

- String, number, object, array, true, false, null

계층형 구조

- 파싱 할 수 있다

Parse

```html
<script>
    var str = '{"name":"Kim", "age":30, "car":["Ray", "Spark"]}';
    
    console.log(str);
    console.log(str.name);
    
    obj = JSON.parse(str);
    
    console.log(obj);
    console.log(obj.name);
</script>
```

Reviver

- String으로 변환된 Json 객체의

- 각 타입을 원본 타입에 맞게 바꿔줄 수 있다.

```html
<script>
    var str = '{"name":"Kim", "age":30, "car":["Ray", "Spark"]}';
    
    console.log(str);
    console.log(str.name);
    
    obj = JSON.parse(str, function(k,v){
        if (typeof(v) == "number")
            return v.toString();
        else
            return v;
    })
    console.log(obj);
    console.log(obj.name);
</script>
```

## XML

- **both human and machine readable**

- **standard way of structing data**
- 모든 언어에서 independant
- No predefined tags
  - 명세와 약속이 필요하다
- Validity
  - 프로토콜을 지켜야 유효하다

Well formed Documents

- 특징
  - 반드시 root 노드가 있어야 함
  - 여는 태그와 닫는 태그의 쌍으로 이루어져 있어야 함 ( html의 경우 쌍 아닐 수도 있다.)
  - 대소문자 구별한다
  - 어트리뷰트는 tag의 안에 들어있어야 한다.
  - 어트리뷰트는 quote로 싸여 있어야 한다.

Valid Documents

- well formed 는 vaild xml과 다르다
  - DTD - Document Type Definition

DTD

- define the structure of an XML document

- ```xml-dtd
  <!DOCTYPE note SYSTEM "Note.dtd">
  ....
  ```

Namespace

- **avoid  element name confilts**

XML Schema

- DTD의 대안
- XML로 쓰여짐
- 확장성이 좋다
- data types를 지원한다
- namespace를 지원한다

comparison

- XML : 데이터를 전달하기 위해 설계
- HTML : 데이터를 display 하기 위해 설계

