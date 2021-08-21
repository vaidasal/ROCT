import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoctComponent } from './loct.component';

describe('LoctComponent', () => {
  let component: LoctComponent;
  let fixture: ComponentFixture<LoctComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoctComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoctComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
