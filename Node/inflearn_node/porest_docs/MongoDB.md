### Install MongoDB

#### NPM MongoDB 모듈 설치
```
npm i @nestjs/mongoose mongoose
```

#### app.module.ts 파일에 MongooseModule 추가하기
```
imports: [
	MongooseModule.forRoot('mongodb://localhost/nest'), 
	{dbName: "dbname"}
	]
```

#### cats 모듈일 경우.
- **cats.controller** : HTTP 요청을 처리하는 컨트롤러 클래스로, @Controller() 데코레이터로 정의되며, CatsService를 주입받아 create()와 findAll() 메서드를 구현합니다.
    
- **cats.module** : CatsService와 CatsController를 모듈화하여 관리하는 모듈 클래스로, @Module() 데코레이터로 정의되며, mongoose를 사용하여 MongoDB와 연결합니다.
    
- **cats.service** : 데이터베이스 작업을 수행하는 서비스 클래스로, @InjectModel() 데코레이터를 사용하여 Cat 모델을 주입받아 create()와 findAll() 메서드를 구현합니다.
    
- **schema/cat.schema** : Cat 모델의 스키마 정의로, @Schema() 데코레이터로 정의되며, mongoose를 사용하여 MongoDB에 저장될 필드와 데이터 타입을 정의합니다.

#### schema/cat.schema 작성
```typescript
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose'; 
import { Document } from 'mongoose'; 
export type CatDocument = Cat & Document; 

@Schema() 
export class Cat { 
	@Prop() 
	name: string; 
	
	@Prop() 
	age: number; 
	
	@Prop() 
	breed: string; 
} 
	
export const CatSchema = SchemaFactory.createForClass(Cat);
```

#### cats.module.ts 파일에 Mongoose Model 추가하기
```typescript
import { Module } from '@nestjs/common'; 
import { MongooseModule } from '@nestjs/mongoose'; 
import { CatsController } from './cats.controller'; 
import { CatsService } from './cats.service'; 
import { Cat, CatSchema } from './schemas/cat.schema'; 

@Module({ 
	imports: [
		MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }])
		], 
	controllers: [CatsController], 
	providers: [CatsService], }) 
	
export class CatsModule {}
```

#### cats.service.ts 파일에서 Mongoose Model 사용하기
```typescript
import { Injectable } from '@nestjs/common'; 
import { InjectModel } from '@nestjs/mongoose'; 
import { Model } from 'mongoose'; 
import { Cat, CatDocument } from './schemas/cat.schema'; 
@Injectable() 
export class CatsService { 
	constructor(@InjectModel(Cat.name) private catModel: Model<CatDocument>) {} 
	
	async create(cat: Cat): Promise<Cat> {
		const createdCat = new this.catModel(cat); 
		return createdCat.save();
	}

	async findAll(): Promise<Cat[]> { 
		return this.catModel.find().exec();
	}
}
```

#### 로컬에 MongoDB-community 설치하기
```
$ brew tap mongodb/brew
$ brew install mongodb-community
```

#### MongoDB 실행 및 정지
```
brew services start mongodb-community
brew services stop mongodb-community
```

#### FindById() \_id 가 ObjectId 타입에 일치하지 않을 경우
```
ERROR [ExceptionsHandler] Cast to ObjectId failed for value
```
- FindById(id) 메서드는 id 값을 ObjectId로 한번 캐스팅하기 때문에 ObjectId 타입이 아닌 경우 에러를 리턴한다. 
- null 에는 null 값을 리턴한다.
- 따라서 id로 쿼리를 날리기 전에 id가 타입과 일치하는지 확인을 한다.
```
1) if (_id.match(/^[0-9a-fA-F]{24}$/)) {}
2) if (Types.ObjectId.isValid(_id)) {}
```
- 정규표현식, mongoose.Type.ObjectId.isValid() 메서드
- 두가지 방법모두 유효한 ObjectId인지 검증한다.
- https://www.mongodb.com/docs/manual/reference/bson-types/#std-label-objectid 참고
- 12byte 길이의 unique한 값을 가진다. 아래 3 값을 더해서 리턴한다.
	- Unix 에포크 이후 초 단위로 측정된 ObjectId 생성을 나타내는 4byte 값
	- 프로세스당 한 번 생성되는 5byte 랜덤 값
	- 임의의 값으로 초기화되는 3byte 증분 카운터 값
- MongoDB에서 컬렉션에 저장된 각 문서에는 [기본 키](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-primary-key) 역할을 하는 고유한 \_id 필드가 필요합니다 . 삽입된 문서에서 필드를 생략하면 MongoDB 드라이버가 자동으로`_id`분야를 위해 생성한다.

#### Repository Pattern

Repository 패턴은 서비스 레이어와 데이터베이스 사이에 레포지토리 레이어 계층이 존재하여 레포지토리가 서비스와 DB를 중계하는 패턴을 말한다.

이 패턴은 여러 개의 서비스 레이어가 존재할 때 이점을 가질 수 있다. 예를 들어 A라는 서비스가 있고, 이는 A라는 데이터를 가져온다고 해보자. 이때 B라는 서비스에서 A데이터가 필요해서 A서비스에 접근한다. 그런데 A 역시 마찬가지로 B서비스의 모듈을 참조하는 코드가 있다면 순환 참조가 발생한다([순환 참조](https://dapsu-startup.tistory.com/entry/ts-node-NodeBird-%EC%8B%9C%ED%80%84%EB%9D%BC%EC%9D%B4%EC%A6%88)에 대해 정리했던 글). 이 문제는 어렵지 않게 해결할 수 있지만 가독성이 떨어진다. 이때 데이터베이스에 접근하는 코드가 분리되어 있다면 A, B 서비스 모듈들이 서로 참조할 필요 없이 레포지토리에만 접근하면 되기 때문에 순환 참조 문제를 깔끔하게 해결할 수 있다. 즉 각각의 서비스 모듈들은 각자의 비즈니스 로직에 더 집중할 수 있게 되고 모듈 간의 책임 분리도 명확해진다.

