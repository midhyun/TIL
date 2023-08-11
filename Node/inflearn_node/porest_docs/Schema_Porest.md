### Restaurant
```typescript
@Schema()
export class Restaurant {

@Prop({ required: true, index: true })
name: string;

@Prop()
en_name: string;

@Prop()
phone_number: string

@Prop()
address: string

@Prop({ type: Date, default: Date.now})
created_at: Date

@Prop({ type: Date, default: Date.now})
updated_at: Date

@Prop()
status: number

@Prop()
menus: Menu

}
```

```json
// Create
METHOD: POST
PARAMS: {
	"_id": ObejctId,
	"name": name, // don't duplicate
	"en_name": en_name, 
	"phone_number": phone_number, 
	"address": address, 
	"status": status
	}
URL: /restaurants
RETURN: restaurants or Error
```

### Menu
- 이름
- 영어이름
- 가격
- 사진
- 설명
- 생성일
- 수정일
- 상태
- 첨가물 정보
- 맛
- 조리방법

### MenuOption
- 한국어 이름
- 영어 이름
- 내용
- 가격
- 생성일
- 수정일
- 상태

에러가 났다 왜났지? s를 빼먹었다.