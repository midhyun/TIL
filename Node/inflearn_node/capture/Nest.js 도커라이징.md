Nest.js로 만든 서버를 AWS EC2에 배포하는 연습을 하고 있다. 이 과정에서 매번 말로만 들어보던 Docker를 사용해보고 싶어졌다. 마침 좋은 실습 자료가 있어 Velog에도 정리해 보았다.

본 포스팅에서 진행하는 작업은 다음과 같다.

> 1. Docker 이미지 생성
> 2. 생성한 이미지를 AWS EC2에 배포
> 3. (예정) Github-Actions를 통한 CI/CD

## Docker를 사용한 이유

Docker가 하도 편하다고 말이 많길래 한번 해보고 싶었다 ㅎㅎ 그런 김에 GDSC Sookmyung에서 옛날에 진행되었던 도커 세션을 참고하여 개념을 간단히 공부해보았다.

![](https://velog.velcdn.com/images/smjan27/post/36d20ae5-cb27-41eb-aba5-55dc0723ae39/image.png)

이미지 출처: [GDSC Sookmyung 티스토리](https://dsc-sookmyung.tistory.com/108)

## Nest.js 프로젝트 생성

```shell
npm i -g @nestjs/cli
nest new 프로젝트명
```

2023년 1월 30일 기준 nestjs의 의존 패키지인 ts-jest가 kt 회선에서 문제를 일으켜 설치 오류가 발생했다. 와이파이를 끄고 스마트폰 데이터를 키고 핫스팟을 켜서 해결했다. (뭐 이런 황당한 에러가..)

## Docker 이미지 생성

### Dockerfile

Docker 이미지를 생성하기 위한 설정 파일

- `node:<version>-alpine`는 Alpine Linux 프로젝트를 기반으로 한다. alpine 리눅스는 대부분의 배포 기반 이미지 보다 작으며(~5MB), 따라서 일반적으로 작은 이미지를 만들 수 있다. ([출처](https://velog.io/@dev_leewoooo/NestJs-Docker-Image-%EB%A7%8C%EB%93%A4%EA%B8%B0))

```javascript
# build stage
// 사용하는 node 버전
FROM node:18-alpine AS build
// RUN,CMD의 명령이 실행될 디렉토리 경로
WORKDIR /usr/src/app
// COPY (복사할 파일 경로) (이미지에서 파일이 위치할 경로)
COPY package*.json ./
// 이미지 실행 시 사용될 명령어
RUN npm install
COPY . .
// FROM에서 설정한 이미지 위에서 스크립트 혹은 명령을 실행
RUN npm run build

# prod stage
FROM node:18-alpine
WORKDIR /usr/src/app
ARG NODE_ENV=production
// 환경변수 설정
ENV NODE_ENV=${NODE_ENV}
COPY --from=build /usr/src/app/dist ./dist
COPY package*.json ./
RUN npm install --only=production
RUN rm package*.json
// 호스트와 연결할 포트 번호
EXPOSE 8080
// 컨테이너가 시작되었을 때 실행하는 명령
CMD ["node", "dist/main.js"]
```

### docker-compose.yaml (DB 설정 추가 예정)

각각 독립된 컨테이너의 실행 정의, Docker 컨테이너에 관한 실행 옵션

네트워크 드라이버 종류 ([출처](https://developer-eun-diary.tistory.com/145))

- `bridge`: 하나의 호스트 컴퓨터에서 여러 개의 컨테이너들이 통신할 수 있게 한다.
- `host`: 호스트 컴퓨터와 동일한 네트워크에서 여러 개의 컨테이너들이 통신할 수 있게 한다.
- `overlay`: 여러 호스트 컴퓨터(다른 네트워크)에서 여러 개의 컨테이너들이 통신할 수 있게 한다.

```yaml
version: '3.9'

services:
  backend:
    build: ./
    container_name: nestjs_api
    ports:
      - '8080:8080'

networks:
  nestjs_network:
    driver: bridge
```

## GitHub 원격 레포지토리에 업로드

일단 GitHub에서 원격 레포지토리를 생성해야 한다.

```bash
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin 레포지토리 주소
git push -u origin main
```

## AWS EC2 인스턴스 생성

- 운영체제: Ubuntu
- 인바운드 규칙에 8080 포트 추가

## EC2에 Docker 설치

키가 있는 경로에 가서 명령 프롬프트를 실행하고 EC2 인스턴스에 접속한다.

```shell
ssh -i 키이름.pem ubuntu@퍼블릭 ip주소
```

[공식 문서(Install Docker Engine on Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)를 참고하여 설치를 진행한다. **저장소를 사용하여 설치**할 것이다. 새 호스트 시스템에 처음으로 Docker 엔진을 설치하기 전에 Docker 리포지토리를 설정해야 한다. 그런 다음 리포지토리에서 Docker를 설치하고 업데이트할 수 있다.

- 저장소 설정
    
    - HTTPS를 통해 리포지토리를 사용할 수 있도록 패키지 인덱스를 업데이트하고 apt 패키지 설치
    
    ```shell
    $ sudo apt-get update
    $ sudo apt-get install \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
    ```
    
    - Docker의 공식 GPG 키 추가
    
    ```shell
    $ sudo mkdir -p /etc/apt/keyrings
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```
    
    - 리포지토리 설정
    
    ```shell
    $ echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
    
- Docker Engine 설치
    
    - apt 패키지 인덱스 업데이트
    
    ```shell
    $ sudo apt-get update
    ```
    
    - Docker Engine, containerd 및 Docker Compose 설치 (최신 버전)
    
    ```shell
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```
    

## Docker 컨테이너 실행

- 깃허브 레포지토리 클론
    
    ```bash
    mkdir apps
    cd apps/
    git clone 레포지토리 주소
    cd 레포지토리 이름
    ```
    
- 컨테이너 생성 및 시작 (`-d`: 백그라운드에서 컨테이너 실행)
    
    ```shell
    $ sudo docker compose up -d
    ```
    
- 컨테이너 확인
    
    ```shell
    $ sudo docker ps
    ```
    
    ![](https://velog.velcdn.com/images/smjan27/post/fe425fe3-8dc8-4f0b-a8e4-476f4deec555/image.png)
    
- 배포된 주소로 접속  
    ![](https://velog.velcdn.com/images/smjan27/post/02e80be8-09fd-4c24-be87-cbc2231564ef/image.png)
    

## (예정) Github-Actions로 CI/CD 구축