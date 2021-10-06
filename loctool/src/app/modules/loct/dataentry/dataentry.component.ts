import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup } from '@angular/forms';

import {CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';
import { DataService } from 'src/app/services/data.service';
import { Router } from '@angular/router';




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
  material!: []
  cabin = ["Cabin 1", "Cabin 2", "Cabin 3", "Cabin 4", "Cabin 5", "Cabin 6", "Cabin 7"]
  tcp = "TCP"

  constructor(private router: Router, private fb: FormBuilder, private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getSettings().subscribe((settings) => {
      this.settings = settings
      this.material = JSON.parse(settings["material"])
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
      part_number: [this.settings['part_number']],
      welding_cabin: [this.settings['welding_cabin']],
      optics: [this.settings['optics']],

      static_x: [this.settings['static_x']],
      static_y: [this.settings['static_y']],
      static_z: [this.settings['static_z']],
      dynamic_speed: [this.settings['dynamic_speed']],
      dynamic_number: [this.settings['dynamic_number']],

      laser_power: [this.settings['laser_power']],
      robot_speed: [this.settings['robot_speed']],
      scanner_speed: [this.settings['scanner_speed']],
      seam_length: [this.settings['seam_length']],
      welding_duration: [this.settings['welding_duration']],

      ramp_power_start: [this.settings['ramp_power_start']],
      ramp_power_end: [this.settings['ramp_power_end']],
      ramp_duration: [this.settings['ramp_duration']],

      fiber_diameter: [this.settings['fiber_diameter']],
      laser_number: [this.settings['laser_number']],
      defocusing: [this.settings['defocusing']],
   
      
      sheet_1_height: [this.settings['sheet_1_height']],
      sheet_2_height: [this.settings['sheet_2_height']],
      sheet_3_height: [this.settings['sheet_3_height']],
      gap_1: [this.settings['gap_1']],
      gap_2: [this.settings['gap_2']],
      sheet_1_material: [this.material],
      sheet_2_material: [this.material],
      sheet_3_material: [this.material],

      measuring_frequency: [this.settings['measuring_frequency']],
      sled_power: [this.settings['sled_power']],
      jump_speed: [this.settings['jump_speed']],
      step_size_oct_tester: [this.settings['step_size_oct_tester']],
    })

    this.laser.push(parallelForm);
  }

  addParallel() {
    const parallelForm = this.fb.group({
      
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
    })

    this.parallel.push(parallelForm);
    this.updateChipsPar("par");
  }

  addCross() {
    const crossForm = this.fb.group({
      points_per_line: [this.settings['points_per_line']],
      line_length: [this.settings['line_length']],
      extend_points: [this.settings['extend_points']],
      lag_xy: [this.settings['lag_xy']],
      x_start: [this.settings['x_start']],
      x_end: [this.settings['x_end']],
      y_start: [this.settings['y_start']],
      y_end: [this.settings['y_end']],
    })

    this.cross.push(crossForm);
    this.updateChipsPar("cro");
  }

  addPoint() {
    const pointForm = this.fb.group({
      points_per_interval: [this.settings['points_per_interval']],
      extend_points: [this.settings['extend_points']],
      reference_points: [this.settings['reference_points']],
      extend_reference_points: [this.settings['extend_reference_points']],
      x_start: [this.settings['x_start']],
      y_start: [this.settings['y_start']],
      x_ref_coordinate: [this.settings['x_ref_coordinate']],
      y_ref_coordinate: [this.settings['y_ref_coordinate']],
    })

    this.point.push(pointForm);
    this.updateChipsPar("poi");
  }

  changeWeldType(event) {
    this.tcp=event.value
    console.log(event.value)
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
        this.router.navigate(['home/loct']);
      }, (err: any) => {
        console.log(err);
      });;
  
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
