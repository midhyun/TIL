import { Injectable, NotFoundException } from '@nestjs/common';
import { Board, BoardsStatus } from './board.model';
import { v1 as uuid } from 'uuid';
import { createBoardDTO } from 'src/boards/dto/create-board.dto';

@Injectable()
export class BoardsService {
    private boards: Board[] = [];

    getAllBoards(): Board[] {
        return this.boards;
    }

    createBoard(createBoardDTO: createBoardDTO) {
        const { title, description } = createBoardDTO;

        const board: Board = {
            id: uuid(),
            title,
            description,
            status: BoardsStatus.PUBLIC,
        }
        this.boards.push(board);
        return board
    }

    getBoardById(id: string): Board {
        const found = this.boards.find((board) => board.id === id);

        if (!found) {
            throw new NotFoundException(`Can't find board with id ${id}`);
        }
        return found
    }

    deleteBoard(id: string):void {
        const found = this.getBoardById(id);
        this.boards = this.boards.filter((board) => board.id !== id);
    }

    updateBoardStatus(id: string, status: BoardsStatus): Board {
        const board = this.getBoardById(id);
        board.status = status;
        return board;
    }


}

// DTO ( Data Transfer Object ) 유효성 확인을 위한 객체
// Pipe @Injectabl() 데코레이터로 주석이 달린 클래스
// data transformation 과 data validation을 위해서 사용 됨.
// Data Transforamtion 입력 데이터를 원하는 형식으로 변환
// Data validation 유효성 검사 
// Built-in Pipes ( Validation, ParseInt, ParseBool, ParseBool, ParseArray, ParseUUID, DefaultValue)

// 커스텀 파이프를 이용한 유효성 체크
// Pipe Transform 이란 인터페이스를 새롭게 만들 커스텀 파이프에 구현해야 하다. 이 Pipe Transform 인터페이스는 모든 파이프에서 구현해줘야하는
// 인터페이스이다. 그리고 이것과 함께 모든 파이프는 transform() 메소드를 필요하다. 이 메소드는 NestJS가 인자 (arguments)를 처리하기 위해서 사용됨.

