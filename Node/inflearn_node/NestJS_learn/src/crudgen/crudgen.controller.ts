import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { CrudgenService } from './crudgen.service';
import { CreateCrudgenDto } from './dto/create-crudgen.dto';
import { UpdateCrudgenDto } from './dto/update-crudgen.dto';

@Controller('crudgen')
export class CrudgenController {
  constructor(private readonly crudgenService: CrudgenService) {}

  @Post()
  create(@Body() createCrudgenDto: CreateCrudgenDto) {
    return this.crudgenService.create(createCrudgenDto);
  }

  @Get()
  findAll() {
    return this.crudgenService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.crudgenService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateCrudgenDto: UpdateCrudgenDto) {
    return this.crudgenService.update(+id, updateCrudgenDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.crudgenService.remove(+id);
  }
}
