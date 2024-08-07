# API

> IT 내부의 원활한 소통(데이터 전달)을 돕기 위한 규칙/ 메뉴얼



### API

- API는 Application programming Interface의 약자이다.

  이를 해석하면 **애플리케이션을 프로그래밍하는데 쓰이는 인터페이스**다.

- '인터페이스'는 쉽게 말해 우리가 노트북을 하기 위해 만지고 보게 되느 화면, 키보드, 마우스 등 모든 것을 이야기한다. 즉 사용자와 기기를 연결해 주기 위한 중간 역할을 하는 지점을 의미한다.
- 이를 더 쉽게 이야기하면 식당의 '점원' 이라 보면 된다.
- 손님은 음식을 직접 주방장에게 주문하는 것이 아니라 중간 역할을 하는 '점원'에게 요청하게 되고, '점원'은 이를 주방장에게 전달하게 된다. 그리고 음식이 완성되었을 때도 주방장에게 음식을 받아 '점원'이 손님에게 가져다주게 되는 것이다. 이러한 '점원'이 인터페이스인 것이다.

- 단 여기서 이야기하려는 API는 눈에 보이지 않는 소프트웨어 인터페이스를 의미한다.
- API는 위에서 설명한 것과 같이 중간 역할을 하지만, 우리 눈에 보이지 않는 IT 세계 속에서 하는 것이다.
- 우리는 앱을 사용 할 때 회원가입부터 로그인, 동영상 재생 등 어떠한 정보 실행을 계속 요청하게 된다.
- 그때 그 요청사항을 받고 처리해주는 것이 컴퓨터 '서버'이다. 그런데 사용자인 우리가 같은 내용의 요청을 하는데도 각자 다른 스타일의 언어와 말로 요청하게 ㅗ디면 서버는 그 뜻을 해석한 후 데이터를 처리해야 하는 비효율적인 과정을 거칠 수밖에 없게 된다.
- 그것을 방지하고자 API가 중간에 끼어들어 '대화의 규칙'을 정하면서 효율적으로 정보가 오고 갈 수 있도록 만드는 것이다. **결국 API는 데이터(정보)를 원활하게 주고받기 위한 방법이자, 주고받을 수 있는 데이터의 형식을 정하는 규격(메뉴얼)이라고 볼 수 있다.**

### REST API

> API를 작성하는 가장 트렌디한 방법

- 그런데 API를 사용하다 보니 문제가 발생했다. '대화의 규칙'을 만들어 더 효과적으로 데이터를 주고받을 수 는 있었지만, 문제는 그 규칙과 규격이 개발자마다 달랐던 것이다.
- 예를 들어 A라는 개발자가 API를 만들어 놓고 '퇴사'를 하게 되면, 다음 후임자인 개발자 B는 해당 API를 온전히 이해할 수 없게 된다.
- 이에 API에도 체계가 필요하다는 관점에서 나온 방법이 'REST API(Representational State Transfer)'다.
- API를 다양한 사람들이 사용하는 만큼 규칙과 내용을 더 '간단하고, 쉽게'만든 것이다.
- 그래서 REST API는 "Represent"가 "표현하다"는 뜻인 것처럼 요청하는 내용만 보면 무엇을 요청하는 것인지 직관적으로 이해할 수 있다.
- REST API는 기본적으로 HTTP(HyperText transfer Protocl)를 사용해
  1) 정보의 자원(리소스)와
  2) 명렬할 행위(행동)를 표현한다.
- 우리에게 낯설지 않은 인터넷 주소를 URI(URL보다 큰 개념)이라 부른다.
- 보다 정확히는 HTTP URI이며, 이는 해당 서버의 정체성을 나타내는 이름과도 같다.
- REST API는 데이터를 불러올 때 HTTP URI로 '어떤 자원'을 통해 데이터를 얻을 것인지 표시해 주어야 한다.
- 그리고 HTTP Method를 통해 해당 자원에 대해 행위(명령어)를 정해야 한다.
- 대표적인 명령어는 4 ~ 5 가지이다.
- POST - Create(생성하기) - ex. 웹페이지에 사진을 올리는 요청
- GET - Read(읽어오기) - ex. 웹페이지에서 사진을 불러오는 요청
- PUT(전체)/ PATCH(일부) - Update(변경하기) - ex. 웹페이지의 사진을 바꾸는 요청
- DELETE - Delete(삭제하기) - ex. 웹페이지의 사진을 지우는 요청

본래 보통의 소프트웨어에서는 CRUD(Create, Read, Update, Delete)를 사용하지만,

HTTP는 보다 간단하고 깔끔하게 명령하기 위해 동사가 아닌 '명사'로 표기한다.



### OPEN API

OPEN API는 누구나 쓸 수 있또록 공개된 API를 의미한다. 기업이나 정부가 유익한 서비스를 개발할 수 있도록 개발자들에게 검증된 데이터를 API 형태로 무료로 제공하는 것이다.

- 오픈 API를 이용하면 개발에 들어가는 비용과 시간을 줄일 수 있다는 이점이 있다.
- 또한 신뢰할 만한, 검증된 API들이기 때문에 보다 퀄리티 좋은 앱을 개발할 수 있다.

그런데 여기서 의문이 하나 든다.

정부는 공공목적으로 API를 공개하겠지만, 왜 기업은 무료로 자신의 API를 공개하는 것일까?

당연히 API를 무료로 공개하는 것이 기업에게 이득이 되기 때문이다.

자사 서비스 기능을 API를 통해 오픈하면, 다른 서비스들이 자사 기능을 많이 이용하게 됨으로써 서비스의 시장 점유율, 경쟁력이 커질 수 있다.

어떤 앱을 설치하거나 서비스를 이요할 대, 해당 서비스로부터 위와 같은 카카오톡 메시지를 받는 경우가 있다. 이것이 카카오에서 제공하는 오픈 API를 사용한 사례이다.

우리가 새로운 앱을 만든다고 가정해 보자.

개발하는 과정에서 앱을 사용하는 유저들에게 공지 및 아림 메시지를 보내는 기능을 만들고 싶다면, 무에서 유를 창조하는 개발을 해야 한다. 그러나 카카오에서 알림 메시지 API를 사용하게 되면 어려운 개발 과정 없이 카카오 메시지 기능과 데이터를 활용해 쉽게 개발이 가능하다.

흔히 우리가 알고 있는 네이버, 카카오 등에 연동시켜 '로그인'하는 기능도 오픈 API의 사례이다. 네이버나 카카오에 있는 유저 정보 데이터를 활용하는 것이다. 유저 입장에서 귀찮은 가입 절차가 없어졌기 때문에 보다 해당 서비스로 유입되기 좋다는 장점이 있다.

사용자의 유입률과 이탈률을 신경 써야 하는 PM은 개발과 관련해서 이러한 부분을 이해하고 고민해야 하는 것이라 본다.

OPEN API의 종류

오픈 API 종류로는 국내 기업, 국외기업, 정부기관 API가 있다.



