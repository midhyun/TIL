import { PartialType } from '@nestjs/mapped-types';
import { CreateCrudgenDto } from './create-crudgen.dto';

export class UpdateCrudgenDto extends PartialType(CreateCrudgenDto) {}
