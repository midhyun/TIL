# Branch

> branch 관련 commands를 이해하고 직접 사용해본다.

### Branch basic commands

```bash
(master) $ git branch {branch name} # 브랜치 생성
(master) $ git checkout {branch name} # 브랜치 이동
(master) $ git checkout -b {branch name} # 브랜치 생성 및 이동
(master) $ git branch 					# 브랜치 목록
(master) $ git branch -d {branch name} # 브랜치 삭제
```



​	***Branch Switching***	

1. `git init`  

   > 저장소 사용 시작 

2. `touch README.md`  > `git add README.md` > `git commit -m 'Add README'` 

   > 작업 후 커밋

3. `git branch` > `git branch example`  > `git checkout example`

   > (1.브랜치 조회) > (2.'example'라는 브랜치 생성) > (3. switching branch) 

4. `touch example.txt` > `git add example.txt` > `git commit -m 'example'` > `git checkout master`

   >exam 브랜치에서 작업 후 master로 브랜치 switch

---------

### Branch Merge

- `git branch merge`
- `git branch -d example`

#### 1. 업무 분배

- 조모임 // 보고서, 발표자료  (조장, 조원)

- ![1](branch.assets/1-16571698854671.jpg)

- **Situation 1.** fast-foward

  - root-commit 발생

    

  - Working & Commit

    ```bash
    $ git branch
    $ git checkout feature/home
    $ git touch home.txt
    $ git add .
    $ git commit -m 'Complete Home!!!!'
    $ git log --oneline
    
    ```

  - master branch

    ```bash
    (feature/home) $ git checout master
    (master) $ git log --oneline
    ```

  - merge master

    ```bash
    $ git merge feature/home
    ```

- **Situation 2.** merge commit

  - feature/about branch 'create & move'

    ```bash
    $ git branch -b feature/about
    ```

  - Working & Commit

    ```bash
    $ touch
    $ git add
    $ git commit
    ```

  - Move master & Work, Commit

    ```bash
    $ git checkout master 
    $ touch
    $ git add
    $ git commit
    ```

  - master merge

    ```bash
    $ git merge feature/about # $ git merge <branch>
    $ git branch -d feature/about # $ del <branch>
    ```

    > new commit create

- **Situation 3** . 

  - Create <branch>

    ```bash
    (master) $ git checkout -b feature/test
    ```

  - Working & Commit

    ```bash
    $ git checkout feature/test 
    # README.md 파일 생성하기 (feature/test)
    $ touch
    $ git add 
    $ git commit
    ```

  - Move `master` > `commit` > `merge`

    ```bash 
    $ git checkout master
    # README.md // 파일 열어서 수정
    (master) $ git add RAEDME.md
    (master) $ git commit -m '<msg>'
    
    $ git merge feature/test
    $ git status # conflicts error
    ```

  - Conflict check

    ```bash
    $ merge commit 
    ```

    - 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.

    - `w` : write

    - `q` : quit

    > 직접 충돌을 해결 후에 add, commit

  - Commit check

    ```bash
    (master) $ git log --oneline --graph
    ```

#### 2.**Github Pull request PR** 

1. *Create a New  **fork***

    ![create_a_new_fork](branch.assets/create_a_new_fork.jpg)

2. *Code clone*

   ![image-20220707180019803](branch.assets/image-20220707180019803.png)

3. *Working Code*

   `git add`  > `git commit`  > `git push` 

   ![image-20220707180235871](branch.assets/image-20220707180235871.png)

4. *Pull Request*

   \* ❗ head repository <branch> ➡ base repository <branch>

   ![image-20220707180408776](branch.assets/image-20220707180408776.png)

5.  *Comfirm base.*

----

### Github Flow 기본 원칙

1. **master branch는 반드시 배포 가능한 상태여야 한다.**
2. **feature branch는 각 기능의 의도를 알 수 있도록 한다.**
3. **commit message 는 매우 중요하며, 명확하게 작성한다.**
4. **pull request를 통해서 협업을 진행한다.**
5. **변경사항을 반영하고 싶다면, master branch에 병합한다.**

---



