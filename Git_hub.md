git remote add <원격저장소이름> <git url>

ex) git remote add origin https://github.com/midhyun/test.git

git push <원격저장소이름> <브렌치이름>

git remote -v  : 원격저장소이름, url

git pull <원격저장소이름> <브렌치이름>



git clone



Push 실패 

- 로컬과 원격 저장소의 커밋 이력이 다른 경우 발생.
  - 작업 전에 Pull 작업 후에 commit, push



원칙 1. 로컬에서만 편집 (수정, 삭제, 생성)

> 혼자 작업할 때 볼일 없음.



원칙2. 작업 전에 $ git pull origin matser ★



touch .gitignore : git 버전 관리를 무시함.

.gitignore

http://gitignore.io

