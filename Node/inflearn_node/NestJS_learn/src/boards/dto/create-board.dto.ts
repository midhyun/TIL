import { IsNotEmpty } from "class-validator";

export class createBoardDTO {
    @IsNotEmpty()
    title: string;

    @IsNotEmpty()
    description: string;
}