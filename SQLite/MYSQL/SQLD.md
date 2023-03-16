7. 부모 엔터티에 데이터가 입력될 때 자식 엔터티에 해당 값이 존재하는지의 여부와 강관없이 입력될 수 있는 구조로 표현되어 있기 때문에, 고객 엔터티에 새로운 고객번호 데이터를 입력하는 것은 주문엔터티에 해당 고객번호가 존재하고 있는ㄴ지의 여부와 상관없이 가능하다.
8.  엔터티를 어디에 배치하는가에 대한문제는 필수사항은 아니지만 데이터 모델링 툴 사용 여부와 상관없이 데이터 모델의 가독성 층면에서 중요한 문제이다. 일반적으로 사람의 눈은 왼쪽에서 오른쪽, 위쪽에서 아래쪽으로 이동하는 경향이 있기 때문에 , 데이터 모델링에서도 가장 중요한 엔터티를 왼쪽 상단에 배치하고, 이것을 중심으로 다른 엔터티를 나열하면서 전개하면 사람의 눈이 따라가기에 편리한데이터 모델을 작성할 수 있다. 해당 업무에서 가장 중요한 엔터티는 왼쪽 상단에서 조금 아래쪽 중앙에 배치하여 전체 엔터티와 어울릴 수 있도록 하면 향후 관련 엔터티오 ㅏ관계선을 연결할 때 선이 꼬이지 않고 효과적으로 배치할 수 있게 된다.
9. 병원은 S병원 1개이므로 엔터티로 성립되지 않으며, 이름, 주소는 엔터티의 속성으로 인식될 수 있다. 엔터티는 2개 이상의 속성과 2개 이상으 ㅣ인스턴스를 가져 소위 면적으로 표현될 수 있어야 비로소 기본적인 엔터티의 자격을 갖췄다 할 수 있으므로 '여러 명'의 복수 인스턴스와 이름, 주소 등의 복수 속성을 가진 '환자'가 엔터티로 가장 적절하다고 할 수 있다.
10. 엔터티의 특징은 다음과 같다. 1) 첫 번째, 반드시 해당 업무에서 필요하고 관리하고자 하는 정보이어야 한다. ex)환자, 토익의 응시 횟수 2)두 번째, 유일한 식별자에 의해 식별이 가능해야 한다. 3) 세 번째, 영속적으로 존재하는 (두 개 이상의) 인스턴스의 집합이어야 한다. 4) 네 번째, 엔터티는 업무 프로스세스에 의해 이용되어야 한다. 5) 다섯 번재, 엔터티는 반드시 속성이 있어야 한다. 6) 여섯 번째, 엔터티는 다른 엔터티와 최소 한 개 이상의 관계가 있어야 한다.
11. 엔터티의 중요한 특징의 하나는 다른 엔터티와 관계를 가져야 한다는 것이다. 그러나 공통코드, 통계성 엔터티의 경우는 관계를 생랼할 수 있다.
12. 기본엔터티(키엔터티)란 그 업무에 원래 존재하는 정보로서 다른 엔터티와의 관계에 의해 생성되지 않고 독립적으로 생성이 간으하고 자신은 타 엔터티의 부모의 역할을 하게 된다. 다른 에터티로부터 주식별자를 사옥받지 않고 자신의 고유한 주 식별자를 가지게 된다. 예를 들어 사원, 부서, 고객, 상품, 자재 등이 기본 엔티티가 될 수 있다.
13. 엔터티를 명명하는 일반적인 기준은 다음과 같다. 용어를 사용하는 모든 표기법이 다 그렇듯이 첫 번째는 가능하면 현업업무에서 사용하는 용어를 사용한다. 두 번째는 가능하면 약어를 사용하지 않는다. 세 번째는 단수명사를 사용한다. 네 번째는 모든 엔터티를 통틀어서 유일하게 이름이 부여되어야 한다. 다섯 번째는 엔터티 생성의미대로 이름을 부여한다.
14. 속성이란 사전적인 의미로는 사물의 성질, 특징 또는 본질적인 성질이다. 그것이 없다면 실체를 생각할 수 없는 것으로 정의할 수 있다. 본질적 속성이란 어떤 사물 또는 개념에 없어서는 안될 징표의 전부이다. 이 징표는 사물이나 개념이 어떤 것인지를 나타내고 그것을 다른 것과 구별하는 성질이라고 할 수 있ㄷ.ㅏ 이런 사전적인 정의 외에 데이터 모델링 관점에서 속성을 정의하자면, '업무에서 필요로 하는 인스턴스에서 관리하고자 하는 의미상 더 이상 분리되지 않는 최소의 데이터 단위' 로 정의할 수 있다. 업무상 관리가 가능한 최소의 의미 단위로 생각할 수 있고, 이것은 엔터티에서 한 분야를 담당하고 있다.
15. 하나의 인스턴스에서 각각의 속성은 한 개 의 속성값을 가져야 한다.
16. 이자는 계산된 값으로 파생속성이 맞지만, 이자율은 원래 가지고 있어야 하는 속성이므로 기본속성에 해당한다.
17. 데이터를 조회할 때 빠른 성능을 할 수 있도록 하기 위해 원래 속성의 값을 계산하여 저장할 수 있도록 만든 속성을 파생속성 이라 한다.
18. 각 엔터티의 속성에 대해서 어떤 유형의 값이 들어가는지를 정의하는 개념은 도메인에 해당함
19. 속성의 명칭은 애매모호하지 않게, 복합 명사를 사용하여 구체적으로 명명함으로써 전체 데이터모델에서 유일성을 확보하는 것이 반 정규화, 통합 등의 작업을 할 때 혼란을 방지할 수 있는 방법이 됨
20. 데이터모델링에서는 조재적 관계와 행위에 의한 관계를 구분하는 표기법이 없으며, UML에서는 연관관계와 의존관계에 대해 다른 표기법을 가지고 표현하게 되어 있다.
21. 관계 표기법은 관계명, 관계차수, 선택성(선택사양)의 3가지 개념으로 표현한다.
22. 관계의 기수성을 나타내는 개념은 관계차수에 해당함
23. 업무기술서, 장표에 관계연결을 가능하게 하는 동사가 있는가? 가 되어야 한다. 동사는 관계를 서술하는 업무기술서의 가장 중요한 사항이다.
24. 4개의 항목 모두 관계를 정의할 때 체크해야 할 항목이다.
25. 주식별자에 의해 엔터티내에 모든 인스턴스들이 유일하게 구분되어야 한다. 주식별자를 구성하는 속성의 수는 유일성을 만족하는 최소의 수가 되어야 한다. 지정된 주식별자의 값은 자주 변하지 않는 것이어야 한다. 주식별자가 지정이 되면 반드시 값이 들어와야 한다.
26. 사번은 업무적으로 의미 있는 식별자로 시스템적으로 부여된 인조식별자가 아니라 일반적으로 사원 인스턴스의 탄생과 함께 업무적으로 부여되는 사원 인스턴스의 본질적인 속성에 해당한다 할 수 있기 때문에 본질식별자로 볼 수 있다.
27. 명칭, 내역등과 같이 이름으로 기술되는 것들은 주식별자로 지정하기에 적절하지 않다. 특히 사람의 이름은 동명이인이 있을 수 있기 때문에 주식별자로서 더더욱 부적절하다.
28. 주식별자를 도출하기 위한 기준은 다음과 같다. 해당 업무에서 자주 이용되는 속성을 주식별자로 지정한다. 명칭, 내역 등과 같이 이름으로 기술되는 것들은 가능하면 주식별자로 지정하지 않는다. 복합으로 주식별자로 구성할 경우 너무 많은 속성이 포함되지 않도록 한다. 자주 수정된는 속성이 주식별자가 되면 자식 엔터티에 대한 연쇄 수정이 필요하여 시스템 상에 부하의 원인이 될 수 있기 때문에 주식별자로서 적합하지 않다.
29. 부모엔터티의 주식별자를 자식 엔터티에서 받아 손자 엔터티까지 계속 흘려 보내기 위해서는 식별자관계를 고려해야 한다. 3의경우는 비식별자 관계를 선택하는 기준으로 고려하기에 가장 마지막으로 고려할만한 비중을 갖는다고 할 수 있다. 즉. 비식별자관계의 선택이 단순히 SQL 문장의 복잡도를 낮추는 목적에서 고려되는 것은 바람직하지 않음을 의미한다.
30. 엔터티별로 데이터의 생명주기(LIFE CYCLE)를 다르게 관리할 경우, 예를 들어 부모엔터티의 인스턴스가 자식의 엔터티와 관계를 가지고 있었지만 자식만 남겨두고 먼저 소멸될 수 잇는 경우 비식별자관계로 연결하는 것이 적절하다. 부모엔터티의 인스턴스가 자식 엔터티와 같이 소멸되는 경우는 비식별자 관계보다 식별자관계로 정의하는 것이 더 적합하다.