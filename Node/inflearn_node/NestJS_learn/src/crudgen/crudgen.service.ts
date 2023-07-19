import { Injectable } from '@nestjs/common';
import { CreateCrudgenDto } from './dto/create-crudgen.dto';
import { UpdateCrudgenDto } from './dto/update-crudgen.dto';

@Injectable()
export class CrudgenService {
  create(createCrudgenDto: CreateCrudgenDto) {
    return 'This action adds a new crudgen';
  }

  findAll() {
    return `This action returns all crudgen`;
  }

  findOne(id: number) {
    return `This action returns a #${id} crudgen`;
  }

  update(id: number, updateCrudgenDto: UpdateCrudgenDto) {
    return `This action updates a #${id} crudgen`;
  }

  remove(id: number) {
    return `This action removes a #${id} crudgen`;
  }
}
