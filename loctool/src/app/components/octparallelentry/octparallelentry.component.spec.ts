import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OctparallelentryComponent } from './octparallelentry.component';

describe('OctparallelentryComponent', () => {
  let component: OctparallelentryComponent;
  let fixture: ComponentFixture<OctparallelentryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OctparallelentryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OctparallelentryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
