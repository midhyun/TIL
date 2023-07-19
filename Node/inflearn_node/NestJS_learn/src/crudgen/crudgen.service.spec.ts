import { Test, TestingModule } from '@nestjs/testing';
import { CrudgenService } from './crudgen.service';

describe('CrudgenService', () => {
  let service: CrudgenService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [CrudgenService],
    }).compile();

    service = module.get<CrudgenService>(CrudgenService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
