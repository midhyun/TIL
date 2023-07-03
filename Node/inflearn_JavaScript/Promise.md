프로미스는 비동기 작업을 조금 더 편하게 처리 할 수 있도록 ES6 에 도입된 기능입니다. 이전에는 비동기 작업을 처리 할 때에는 콜백 함수로 처리를 해야 했었는데요, 콜백 함수로 처리를 하게 된다면 비동기 작업이 많아질 경우 코드가 쉽게 난잡해지게 되었습니다.

비동기 함수를 호출하면 함수 내부의 비동기로 동작하는 코드가 완료되지 않았다 해도 기다리지 않고 즉시 종료된다. 즉, 비동기 함수 내부의 비동기로 동작하는 코드는 비동기 함수가 종료된 이후에 완료된다. 따라서 비동기 함수 **내부의 비동기로 동작하는 코드에서 처리 결과를 외부로 반환하거나 상위 스코프의 변수에 할당하면 기대한 대로 동작하지 않는다.**

**이처럼 비동기 함수는 비동기 처리 결과를 외부에 반환할 수 없고, 상위 스코프의 변수에 할당할 수도 없다.** 따라서 비동기 함수의 처리 결과(서버의 응답 등) 에 대한 후속 처리는 **비동기 함수 내부에서 수행**해야 한다. 이때 비동기 함수를 범용적으로 사용하기 위해 비동기 함수에 비동기 처리 결과에 대한 후속 처리를 수행하는 콜백 함수를 전달하는 것이 일반적이다. 필요에 따라 비동기 처리가 성공하면 호출될 콜백 함수와 비동기 처리가 실패하면 호출될 콜백함수를 전달할 수 있다.

한번 숫자 n 을 파라미터로 받아와서 다섯번에 걸쳐 1초마다 1씩 더해서 출력하는 작업을 setTimeout 으로 구현해봅시다.

```javascript
function increaseAndPrint(n, callback) {
	  setTimeout(() => {
	    const increased = n + 1;
	    console.log(increased);
	    if (callback) {
	      callback(increased);
	    }
	  }, 1000);
	}
	
increaseAndPrint(0, n => {
	increaseAndPrint(n, n => {
		increaseAndPrint(n, n => {
			increaseAndPrint(n, n => {
				increaseAndPrint(n, n => {
					console.log('끝!')
				});
			});
		});
	});
});
```

코드 읽기가 복잡하죠? 이런 식의 코드를 Callback Hell (콜백지옥) 이라고 부릅니다.

![](https://i.imgur.com/FDzn5s0.png)

비동기적으로 처리해야 하는 일이 많아질수록, 코드의 깊이가 계속 깊어지는 현상이 있는데요, Promise 를 사용하면 이렇게 코드의 깊이가 깊어지는 현상을 방지 할 수 있습니다.

### Promise 만들기

Promise 는 다음과 같이 만듭니다.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // 구현..
})
```

Promise 는 성공 할 수도 있고, 실패 할 수도 있습니다. 성공 할 때에는 resolve 를 호출해주면 되고, 실패할 때에는 reject 를 호출해주면 됩니다. 지금 당장은 실패하는 상황은 고려하지 않고, 1초 뒤에 성공시키는 상황에 대해서만 구현을 해보겠습니다.

```javascript
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(1);
  }, 1000);
});

myPromise.then(n => {
  console.log(n);
});
```

resolve 를 호출 할 때 특정 값을 파라미터로 넣어주면, 이 값을 작업이 끝나고 나서 사용 할 수 있습니다. 작업이 끝나고 나서 또 다른 작업을 해야 할 때에는 Promise 뒤에 `.then(...)` 을 붙여서 사용하면 됩니다.

이번에는, 1초뒤에 실패되게끔 해봅시다.

```javascript
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject(new Error());
  }, 1000);
});

myPromise
  .then(n => {
    console.log(n);
  })
  .catch(error => {
    console.log(error);
  });
```

실패하는 상황에서는 `reject` 를 사용하고, `.catch` 를 통하여 실패했을시 수행 할 작업을 설정 할 수 있습니다.

이제, Promise 를 만드는 함수를 작성해봅시다.

```javascript
function increaseAndPrint(n) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const value = n + 1;
      if (value === 5) {
        const error = new Error();
        error.name = 'ValueIsFiveError';
        reject(error);
        return;
      }
      console.log(value);
      resolve(value);
    }, 1000);
  });
}

increaseAndPrint(0).then((n) => {
  console.log('result: ', n);
})
```

![](https://i.imgur.com/S4bDqHz.png)

여기까지만 보면, 결국 함수를 전달하는건데, 뭐가 다르지 싶을수도 있습니다. 하지만, Promise 의 속성 중에는, 만약 then 내부에 넣은 함수에서 또 Promise 를 리턴하게 된다면, 연달아서 사용 할 수 있습니다. 다음과 같이 말이죠.

```
function increaseAndPrint(n) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const value = n + 1;
      if (value === 5) {
        const error = new Error();
        error.name = 'ValueIsFiveError';
        reject(error);
        return;
      }
      console.log(value);
      resolve(value);
    }, 1000);
  });
}

increaseAndPrint(0)
  .then(n => {
    return increaseAndPrint(n);
  })
  .then(n => {
    return increaseAndPrint(n);
  })
  .then(n => {
    return increaseAndPrint(n);
  })
  .then(n => {
    return increaseAndPrint(n);
  })
  .then(n => {
    return increaseAndPrint(n);
  })
  .catch(e => {
    console.error(e);
  });
```

![](https://i.imgur.com/526Xcue.png)

위 코드는 이렇게 정리를 할 수 있습니다.

```
function increaseAndPrint(n) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const value = n + 1;
      if (value === 5) {
        const error = new Error();
        error.name = 'ValueIsFiveError';
        reject(error);
        return;
      }
      console.log(value);
      resolve(value);
    }, 1000);
  });
}

increaseAndPrint(0)
  .then(increaseAndPrint)
  .then(increaseAndPrint)
  .then(increaseAndPrint)
  .then(increaseAndPrint)
  .then(increaseAndPrint)
  .catch(e => {
    console.error(e);
  });
```

Promise 를 사용하면, 비동기 작업의 개수가 많아져도 코드의 깊이가 깊어지지 않게 됩니다.

하지만, 이것도 불편한점이 있긴 합니다. 에러를 잡을 때 몇번째에서 발생했는지 알아내기도 어렵고 특정 조건에 따라 분기를 나누는 작업도 어렵고, 특정 값을 공유해가면서 작업을 처리하기도 까다롭습니다. 다음 섹션에서 배울 async/await 을 사용하면, 이러한 문제점을 깔끔하게 해결 할 수 있습니다.

