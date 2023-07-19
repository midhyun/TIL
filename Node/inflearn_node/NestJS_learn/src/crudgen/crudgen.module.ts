import { Module } from '@nestjs/common';
import { CrudgenService } from './crudgen.service';
import { CrudgenController } from './crudgen.controller';

@Module({
  controllers: [CrudgenController],
  providers: [CrudgenService]
})
export class CrudgenModule {}
