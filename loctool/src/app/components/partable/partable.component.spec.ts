import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PartableComponent } from './partable.component';

describe('PartableComponent', () => {
  let component: PartableComponent;
  let fixture: ComponentFixture<PartableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PartableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PartableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
