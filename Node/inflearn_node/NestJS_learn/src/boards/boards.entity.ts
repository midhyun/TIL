import { BaseEntity, Column, Entity, PrimaryGeneratedColumn } from "typeorm";
import { BoardsStatus } from "./board.model";

@Entity()
export class Board extends BaseEntity {
    @PrimaryGeneratedColumn()
    id:number;

    @Column()
    title: string;

    @Column()
    description: string;

    @Column()
    status: BoardsStatus;
}