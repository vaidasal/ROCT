import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LaserentryComponent } from './laserentry.component';

describe('LaserentryComponent', () => {
  let component: LaserentryComponent;
  let fixture: ComponentFixture<LaserentryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LaserentryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LaserentryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
