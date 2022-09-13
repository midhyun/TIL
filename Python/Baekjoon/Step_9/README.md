### BOJ_Step_9. 재귀

### 9_5. 하노이의 탑

![image-20220803002009680](README.assets/image-20220803002009680.png)

- 접근 방법 : 

  1) ~~하나씩 옮기는 방법~~
  2) 규칙을 찾기 --- 찾았으나 표현이 쉽지 않음
  3) ~~스택 구조와 유사하다 생각함, stack.append(.pop()) 으로 블럭들을 옮기는 생각.~~  (출력 값이 블럭을 옮기는것이 아닌 블록의 **이동기록**)
  4) 맨 아래 블럭을 제외한 블럭을 2번칸으로, 맨 아래 블럭을 목표인 3번으로,
     이후 2번칸에 있는 블럭들을 3번으로, 이부분에 서 재귀가 발생

- 재귀찾기

  - n-1번째 까지의 블럭들을 1과 3이 아닌 곳으로 옮긴다.			# 1
  - n 번째 블럭을 3으로 옮긴다														# 2
  - n-1번째 까지의 블럭들을 1과 3이 아닌곳에서 3으로 옮긴다.  # 3

  ```python
  def hanoi(n, start, end):
      if n == 1:
          print(start, end)			# 블럭 1개는 시작지점에서 도착지점으로 옮기면 됨
          
      hanoi(n-1, start, 6-start-end)  #1 n-1 번째 까지의 블럭들을 시작지점과 도착지점이 아닌곳((1+2+3)-start(1)-end(2)) = 2 으로 옮긴다.
      print(start, end)				#2 맨 아래에 있는 n번째 블럭을 end로 옮긴다.
      hanoi(n-1, 6-start-end, end)	#3 n-1 번째 까지의 블럭들을 시작지점과 도착지점이 아닌 곳 에서 도착지점으로 옮긴다.
      
  n = int(input())
  print(2**n -1)						# 하노이 탑의 최단이동 횟수
  hanoi(n, 1, 3)
  
  # n == 3:
  3
  7
  1 3
  1 2
  3 2
  1 3
  2 1
  2 3
  1 3
  ```

- 규칙을 찾아 3구역으로 나눈것 까지는 좋았다. 조금만 더 쉽게 생각해보자, 재귀는 뒤에서 부터 초깃값으로 생각하는 편이 찾기 쉬운 것 같다.

  재귀가 일어나는 지점을 좀더 구체적으로 보자.