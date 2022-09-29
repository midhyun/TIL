# Todolist 

> Todo 웹 개발

### django 활용

- python 기반 venv 가상환경 설정
- django 서버 사용

### Templates

- base.html : base {% extends 'base.html' %} 익스텐즈 활용

- Index.html : 인덱스 페이지
- edit.html : 수정 페이지

### Views

> render 와 redirect 의 차이를 생각해 볼 것.

- index (render)
  - Todo 테이블에서 값을 가져옴
  - index.html 에서 반복문으로 값을 출력함
- create (redirect)
  - Todo 테이블에 각 컬럼마다 값을 넣어줌
  - index.html 에서 input 에값을 넣어서 submit 함
- delete (redirect)
  - Todo 테이블에서 pk가 일치하는 row를 가져옴
  - 해당 row를 삭제함 ( Todo.delete())

- edit (render) : 수정 페이지로 이동
  - Todo 테이블에서 pk가 일치하는 row를 가져옴
  - input value = ' todo.content' 객체 값들을 수정할 수 있도록 기존 값을 보여줌
- modify (redirect)
  - edit 페이지에서 수정한 값들을 가져옴
  - pk가 일치하는 row 에 수정 된 값들을 DB에 넣어줌
  - `todo.save`
  - 수정이 완료되면 index로 redirect
- complete (redirect)
  - pk에 해당하는 complete boolean 값을 변경함
  - 값에 따라 index.html 에서 if문으로 출력을 변경함.