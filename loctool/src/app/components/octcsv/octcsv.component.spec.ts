import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OctcsvComponent } from './octcsv.component';

describe('OctcsvComponent', () => {
  let component: OctcsvComponent;
  let fixture: ComponentFixture<OctcsvComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OctcsvComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OctcsvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
