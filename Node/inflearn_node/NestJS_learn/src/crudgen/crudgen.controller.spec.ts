import { Test, TestingModule } from '@nestjs/testing';
import { CrudgenController } from './crudgen.controller';
import { CrudgenService } from './crudgen.service';

describe('CrudgenController', () => {
  let controller: CrudgenController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [CrudgenController],
      providers: [CrudgenService],
    }).compile();

    controller = module.get<CrudgenController>(CrudgenController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
