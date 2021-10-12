import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OctpointentryComponent } from './octpointentry.component';

describe('OctpointentryComponent', () => {
  let component: OctpointentryComponent;
  let fixture: ComponentFixture<OctpointentryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OctpointentryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OctpointentryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
