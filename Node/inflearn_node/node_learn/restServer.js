const cluster = require('cluster');
const http = require('http');
const fs = require('fs').promises;
const path = require('path');
const numCpus = require('os').cpus().length;

// 쿠키 변환함수
const parseCookies = (cookie = '') =>
  cookie
    .split(';')
    .map(v => v.split('='))
    .reduce((acc, [k, v]) => {
      acc[k.trim()] = decodeURIComponent(v);
      return acc;
    }, {});

const session = {}; // 세션 저장용
const users = {} // 데이터 저장용

if (cluster.isMaster) {
  console.log(`마스터 프로세스 ID: ${process.pid}`);
  // CPU개수 만큼 워커 생산.
  for (let i = 0; i < numCpus; i++) {
    cluster.fork();
  }
  // 워커가 종료되었을 때
  cluster.on('exit', (worker, code, signal) => {
    console.log(`${worker.process.pid}번 워커가 종료되었습니다.`);
    console.log('code', code, 'signal', signal);
    cluster.fork();
  });
} else {
  // 워커들이 포트에서 대기
  
}

http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);
  try {
      if (req.method === 'GET') {
          if (cookies.session && session[cookies.session].expires > new Date()) {
            res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.end(`${session[cookies.session].name}님 안녕하세요`);
          } else if (req.url === '/') {
              const data = await fs.readFile(path.join(__dirname, 'login.html'));
              res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
              return res.end(data);
          } else if (req.url === '/about') {
              const data = await fs.readFile(path.join(__dirname, 'about.html'));
              res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
              return res.end(data);
          } else if (req.url === '/users') {
              res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
              return res.end(JSON.stringify(users));
          } else if (req.url.startsWith('/login')) { // 로그인 하기
            const url = new URL(req.url, 'http://localhost:8082');
            const name = url.searchParams.get('name');
            const expires = new Date();
            expires.setMinutes(expires.getMinutes() + 5);
            const uniqueInt = Date.now();
            session[uniqueInt] = {
              name,
              expires,
            };
            res.writeHead(302, {
              Location: '/',
              'Set-Cookie': `session=${uniqueInt}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
            });
            res.end();
          } else {
            try {
              const data = await fs.readFile(path.join(__dirname, 'login.html'));
              res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
              res.end(data);
            } catch (err) {
              res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8'});
              res.end(err.message);
            }
          }
      } else if (req.method === 'POST') {
          if (req.url === '/user') {
              let body = '';
              // 요청의 body를 stream 형식으로 받음
              req.on('data', (data) => {
                  body += data;
              });
              // 요청의 body를 다 받은 후 실행됨
              return req.on('end', () => {
                console.log('POST 본문(Body):', body);
                const { name } = JSON.parse(body);
                const id = Date.now();
                users[id] = { name };
                res.writeHead(201, { 'Content-type': 'text/plain; charset=utf-8'});
                res.end('등록 성공');
              });
          }
      } else if (req.method === 'PUT') {
          if (req.url.startsWith('/user/start/')) { // 시작 요청
            console.log(req.url)
            const key = req.url.split('/')[3];
            let body = '';
            req.on('data', (data) => {
              body += data;
            });
            return req.on('end', () => {
              const time = Date.now();
              console.log('PUT 시작(Body):', time);
              users[key]['time'] = time;
              res.writeHead(200, { 'Content-type': 'text/plain; charset=utf-8' });
              return res.end(JSON.stringify(users));
            })
          } else if (req.url.startsWith('/user/')) { // 수정 요청
            console.log(req.url)
            const key = req.url.split('/')[2];
            let body = '';
            req.on('data', (data) => {
              body += data;
            });
            return req.on('end', () => {
              console.log('PUT 본문(Body):', body);
              users[key]['name'] = JSON.parse(body).name;
              res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
              return res.end(JSON.stringify(users));
            });
          }
        } else if (req.method === 'DELETE') {
          if (req.url.startsWith('/user/')) {
            const key = req.url.split('/')[2];
            delete users[key];
            res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
            return res.end(JSON.stringify(users));
          }
        } else {
          res.writeHead(404);
          return res.end('NOT FOUND');
        }
      } catch (err) {
        console.error(err);
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end(err.message);
      }
    })
        .listen(8082, () => {
          console.log('8082번 포트에서 서버 대기 중입니다');
    }); 