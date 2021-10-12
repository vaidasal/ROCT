import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OctcrossentryComponent } from './octcrossentry.component';

describe('OctcrossentryComponent', () => {
  let component: OctcrossentryComponent;
  let fixture: ComponentFixture<OctcrossentryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OctcrossentryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OctcrossentryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
