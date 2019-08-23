# Functional Programming in Python

- `data`로 할수 있는 모든 것은 함수 자체로도 실행될 수 있다
- 재귀는 주 제어 구조이다.
- `list processing`이 가능하다
- 파이썬은 `pure functional programming language`가 아니다.

## (Avoiding) Flow Control

> `어떻게` 하느냐보다 `무엇을` 하느냐에 초점을 맞춘다.

### Encapsulation

> 밖에서는 안을 처리할 수 없다
>
> 안에서만 밖을 처리할 수 있다.

데이터 구조를 더 고립된 구조로 만든다

```python
# configure the data start with
collection = get_initial_state()
state_var = None
for datum in data_set:
    if condition(state_var):
        state_var = calculate_from(datum)
        new = modify(datum, state_var)
        collection.add_to(new)
	else:
        new = modify_differently(datum)
        collection.add_to(new)
        
# Now actually work with the data
for thing in collection:
    process(thing)
```

`어떻게`를 함수로 만들 수 있다. 기능을 추상화하고 고립한다.

```python
# tuck away construction of data
def make_collection(data_set):
    collections = get_initial_state()
    state_var = None
    for datum in data_set:
        if condition(state_var):
            state_var = calculate_from(datum, state_var)
            new = modify(datum, state_var)
            collection.add_to(new)
        else:
            new = modify_differently(datum)
            collection.add_to(new)
    return collection

for thing in make_collection(data_set):
    process(thing)
```

로직을 바꾼것도 아니고 코드 라인도 변하지 않았다. 그러나

`어떻게 collection을 만들지?`에서

`make_collection()은 무엇을 만드나요?` 로 옮겼다.

### Comprehensions

list / set / dicttionary 가 있다.

`무엇을`에 초점을 맞추기 위해 자주 쓰이는 방법

``` python
collection = list()
for datum in data_set:
    if condition(datum):
        collection.append(datum)
    else:
        new = modify(datum)
        collection.append(new)
```

> 오컴의 면도날

``` python
collection = [d if condition(d) else modity(d) 
              for d in data_set]
```

콜렉션이 무엇인지만 생각하고

루프에서 collection의 상태를 생각할 필요가 없다

#### Generators

> 1. yield 로 생성
> 2. Comprehension으로 생성

*lazy* 하다

실제로 사용될 때까지 계산을 연기해서 큰 시퀀스에 대해 메모리를 절약한다.

> open() 함수는 generator로 되어있다. 메모리 절약 가능

```python
# comprehension 방법
log_lines = (line for line in read_line(huge_log_file)
            if complex_condition(line))
```

```python
# yield 방법
def get_log_lines(log_file):
    line = read_line(log_file)
    while True:
        try:
            if complex_condition(line):
                yield line
            line = read_line(log_file)
        except StopIteration:
            raise
log_lines = get_log_lines(huge_log_file)
```

##### duck typing

iterator 클래스 상속하지 않아도 protocol만 지키면 iterator 객체처럼 사용 가능 

```python
class GetLogLines(object):
    def __init__(self, log_file):
        self.log_file = log_file
        self.line = None
    def __iter__(self):
        return self
   	def __next__(self):
        if self.line is None:
            self.line = read_line(log_file)
        while not complex_condition(self.line):
            self.line = read_line(self.log_file)
        return self.line
    
log_lines = GetLogLines(huge_log_file)
```

#### Dicts and Sets

> comprehension으로 생성할 수 있다.

### Recursion

> tail recursion elimination을 python에서 지원하지 않기 때문에 비효율적이다
>
> sys.setrecursionlimiit() 함수로 조정할 수 있으나 비효율적
>
> 점화식으로 표현할 수 있으면 recursion으로 전부 표현 가능

``` python
def running_sum(numbers ,strart=0):
    if len(numbers) == 0:
        return
    total = numbers[0] + start
    running_sum(numbers[1:], total)
```

위 함수는 순환 사용하는 것보다 가독성, 속도 면에서 비효율적

그러나, 재귀가 더 좋은 경우도 있다. 직관적이고 이해하기 쉽다.

``` python
## 재귀적
def factorialR(N):
    assert isinstance(N, int) and N >= 1
    retrun 1 if N <= 1 else N * factorialR(N-1)
    
## 순환적
def factorialI(N):
    assert isinstance(N, int) and N >= 1
    product = 1
    while N >= 1:
        product *= N
        N -= 1
	return product
```

순환적 버전의 product와 N은 계산 자체가 아니다. (더 빠르긴 하다)

``` python
from functools import reduce ## 함수형 패러다임
from operator import mul ## 함수형 패러다임
def factorialHOF(n):
    return reduce(mul, ragne(1, n+1), 1)
```

가장 빠르고 좋은 버전

##### quick sort

상태 변수나 루프 없다.

$O(log N)$의 재귀

```python
def quicksort(lst):
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x==pivot]
    small = quicksort([x for x in lst if x<pivot])
    large = quicksort([x for x in lst if x>pivot])
    return small + pivots + large
```

### Eliminating Loops

> 루프의 for 문 없앤다

```python
for e in it: # statement-based loop
    func(e)
    
map(func, it) # map-based loop
## e 가 반복적으로 바인딩되지 않으므로 state가 없다
```

``` python
# f1, f2, f3를 함수라고 가정
do_it = lambda f, *args : f(*args)

map(do_it, [f1,f2,f3])
```



## Callables

### Named Functions and Lambdas

### Closures and Callable Instances

### Method of Classes

### Multiple Dispatch

## Lazy Evaluation

### The Iterator Protocol

### Module : itertools

## Higher-Order Functions

> 함수의 인자를 함수로 쓸 수 있다. ex) map()
>
> 또는 function 이름을 return 할 수 있다.
>
> map, filter, reduce의 심화버전

``` python
## classic "FP-style"
transformed = map(transformation, iterator)
## Comprehension
transformed = (transformation(x) for x in iterator)

## FP style
filtered = filter(predicate, iterator)
## comprehension
filtered = (x for x in iterator if predicate(x))
```

```python
from functools import reduce
total = reduce(operator.add, it, 0) # 함수를 인자로 받는다.
# total = sum(it)
```

```python
>>> add 5 = lambda n : n+5
>>> reduce(lambda l, x : l+[add5(x)], range(10), [])
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> # simpler : map(add5, range(10))
>>> isOdd = lambda n : n%2
>>> reduce(lambda l, x: l+[x] if isOdd(x) else l, range(10), [])
[1, 3, 5, 7, 9]
>>> #simpler : filter(isOdd, range(10))
```

### Utility Higher-Order Functions

`compose()` : 합성함수로 만든다

``` python
def compose(*funcs):
    """Return a new function s.t.
       compose(f,g,...)(x) == f(g(...(x)))"""
    def inner(data, funcs=funcs):
        result = data # mutable 일 때 주의! 원본이 바뀌지 않게 .copy()쓸수있다.
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner
```

`all()` : 하나라도 false이면 false

`any()` : 하나라도 true이면 true

```python
all_pred = lambda item, *tests: all(p(item) for p in tests)
any_pred = lambda item, *tests: any(p(item) for p in tests)
```

```python
>>> is_lt100 = partial(operator.ge, 100) # less than 100?
>>> is_gt10 = partial(operator.le, 10) # greater than 10?
>>> from nums import is_prime # implemented elsewhere
>>> all_pred(71, is_lt100, is_gt10, is_prime)
True
>>> predicates = (is_lt100, is_gt10, is_prime)
>>> all_pred(107, *predicates)
False
```



### The operator Module

### The functools Module

### Decorators