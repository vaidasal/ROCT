import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup } from '@angular/forms';
import { SidenavService } from '../../../services/sidenav.service';

import {CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';
import { DataService } from 'src/app/services/data.service';




@Component({
  selector: 'app-dataentry',
  templateUrl: './dataentry.component.html',
  styleUrls: ['./dataentry.component.css']
})
export class DataentryComponent implements OnInit {

  form = this.fb.group({
    chipForm: this.fb.array([
    ]),
    parallel: this.fb.array([
    ]),
    cross: this.fb.array([
    ]),
    point: this.fb.array([
    ]),
    laser: this.fb.array([
    ])
  });

  chips: String[] = []
  parChips: String[] = [
  ];
  poiChips: String[] = [
  ];
  croChips: String[] = [
  ];

  settings!: {}



  constructor(private fb: FormBuilder, private sideNavService: SidenavService, private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getSettings().subscribe((settings) => {
      this.settings = settings
      console.log(this.settings)
      this.addLaser();
    })
    this.updateChips();
  }

  get parallel() {
    return this.form.get('parallel') as FormArray;
  }

  get cross() {
    return this.form.get('cross') as FormArray;
  }

  get point() {
    return this.form.get('point') as FormArray;
  }

  get laser() {
    return this.form.get('laser') as FormArray;
  }

  get chipForm() {
    return this.form.get('chipForm') as FormArray;
  }

  addLaser() {
    const parallelForm = this.fb.group({
      seam_id: [""],
      seam_length: [this.settings['seam_length']],
      speed: [this.settings['speed']],
      step_size_oct_tester: [this.settings['step_size_oct_tester']],
    })

    this.laser.push(parallelForm);
  }

  addParallel() {
    const parallelForm = this.fb.group({
      frequency: [this.settings['frequency']],
      points_per_line: [this.settings['points_per_line']],
      line_length: [this.settings['line_length']],
      extend_points: [this.settings['extend_points']],
      reference_points: [this.settings['reference_points']],
      extend_reference_points: [this.settings['extend_reference_points']],
      lag_xy: [this.settings['lag_xy']],
      x_start: [this.settings['x_start']],
      x_end: [this.settings['x_end']],
      y_start: [this.settings['y_start']],
      y_end: [this.settings['y_end']],
      x_ref_coordinate: [this.settings['x_ref_coordinate']],
      y_ref_coordinate: [this.settings['y_ref_coordinate']],
      jump_speed: [this.settings['jump_speed']],
    })

    this.parallel.push(parallelForm);
    this.updateChipsPar("par");
  }

  addCross() {
    const crossForm = this.fb.group({
      frequency: [this.settings['frequency']],
      points_per_line: [this.settings['points_per_line']],
      line_length: [this.settings['line_length']],
      extend_points: [this.settings['extend_points']],
      lag_xy: [this.settings['lag_xy']],
      x_start: [this.settings['x_start']],
      x_end: [this.settings['x_end']],
      y_start: [this.settings['y_start']],
      y_end: [this.settings['y_end']],
      jump_speed: [this.settings['jump_speed']],
    })

    this.cross.push(crossForm);
    this.updateChipsPar("cro");
  }

  addPoint() {
    const pointForm = this.fb.group({
      frequency: [this.settings['frequency']],
      points_per_interval: [this.settings['points_per_interval']],
      extend_points: [this.settings['extend_points']],
      reference_points: [this.settings['reference_points']],
      extend_reference_points: [this.settings['extend_reference_points']],
      x_start: [this.settings['x_start']],
      y_start: [this.settings['y_start']],
      x_ref_coordinate: [this.settings['x_ref_coordinate']],
      y_ref_coordinate: [this.settings['y_ref_coordinate']],
      jump_speed: [this.settings['jump_speed']],
    })

    this.point.push(pointForm);
    this.updateChipsPar("poi");
  }


  deleteParallel(parallelIndex: number) {
    this.parallel.removeAt(parallelIndex);
    this.updateChipsPar("par");
  }

  deleteCross(crossIndex: number) {
    this.cross.removeAt(crossIndex);
    this.updateChipsPar("cro");
  }

  deletePoint(pointIndex: number) {
    this.point.removeAt(pointIndex);
    this.updateChipsPar("poi");
  }

  deleteLaser(laserIndex: number) {
    this.laser.removeAt(laserIndex);
  }

  onSubmit() {
    const chpForm = this.fb.group({
      "chp": JSON.stringify(this.chips), 
      });
      this.chipForm.removeAt(0);
      this.chipForm.push(chpForm);
      this.dataService.saveLaserParams(this.form.value).subscribe((res: any) => {
        location.reload();
        //this.router.navigate(['home/user']).then(_ => this.dialogRef.close());
      }, (err: any) => {
        console.log(err);
      });;
  
  }

  toggleSidenav() { 
    this.sideNavService.toggle();
  }

  drop(event: CdkDragDrop<String[]>) {
    moveItemInArray(this.chips, event.previousIndex, event.currentIndex);
    this.updateChipForm();
    console.log(this.chips)
  }

  updateChipsPar(type: String) {
    const len = this.form.value["point"].length;
    if (type == "poi") {
      this.poiChips = [];
      for (let i = 0; i < len; i++) {
        this.poiChips.push("Point " + String(i));
      }
    } else if (type == "par") {
      const len = this.form.value["parallel"].length;
      this.parChips = [];
      for (let i = 0; i < len; i++) {
       this.parChips.push("Parallel " + String(i));
      }
    } else if (type == "cro") {
      const len = this.form.value["cross"].length;
      this.croChips = [];
      for (let i = 0; i < len; i++) {
        this.croChips.push("Cross " + String(i));
      }
    }
    this.updateChips()
  }

  updateChips() {
    this.chips = ["Start"]
    this.chips = this.chips.concat(this.parChips);
    this.chips = this.chips.concat(this.poiChips);
    this.chips = this.chips.concat(this.croChips);
    this.updateChipForm();
    console.log(this.chips)
    console.log(this.parChips)
  }

  updateChipForm() {
    const chp = {}
    for (var chip of this.chips) {
      chp[String(chip)]  =  chip;
    }
    console.log(chp)

  }

}
