import { ArgumentMetadata, BadRequestException, PipeTransform } from "@nestjs/common";
import { BoardsStatus } from "../board.model";

export class BoardStatusValidationPipe implements PipeTransform {

    readonly StatusOptions = [
        BoardsStatus.PRIVATE,
        BoardsStatus.PUBLIC
    ]

    transform(value: any) {
        value = value.toUpperCase();
        console.log('value', value);
        if (!this.isStatusValid(value)) {
            throw new BadRequestException(`${value} isn't in the status options`)
        }

        return value;
    }

    private isStatusValid(status: any) {
        const index = this.StatusOptions.indexOf(status);
        return index !== -1;
    }
}