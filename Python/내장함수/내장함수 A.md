# 내장함수 A

1. **abs(x)**

   - 숫자의 절댓값을 돌려줍니다. 인자는 정수, 실수 또는 \__abs__()를 구현하는 객체이다. 인자가 복소수면 그 크기가 반환된다.

     ```python
     # input = -30.23
     print(abs(float(input())))
     # output = 30.23
     ```

2. **aiter(asyno_iterable)**

   - Return an asynchronous iterator for an asynchronous iterable. Equivalent to cailling `x.\__aiter__()` 
   - Note : Unlike `iter()`, `aiter()` has no 2 - argument variant   *+) v3.10 add* 

3. **all(iterable)**

   - iterable 의 모든 요소가 참이면 (또는 iterable 이 비어있으면) `True`를 돌려줍니다. 다음과 동등합니다.

     ```python
     def all(iterable):
         for elemnet in iterable:
             if not element:
                 return False
         return True
     ```

   - awaitable anext(asyno_iterator[, default])
     - When awaited, return the next item from the given asynchronous iterator, or default if given ans the iterator is exhausted.
     - this is the async variant of the `next()` builtin, and behaves similarly.
     - This calls the `\__anext__()` methos of async_iterator, returning an **awaitable**. Awaiting this returns the next value of the iteraor. If default is given, it is returned if the iterator is exhuasted, otherwizse *StopAsyncleration* is raised.