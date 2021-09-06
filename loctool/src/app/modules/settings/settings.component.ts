import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder } from '@angular/forms';
import { DataService } from 'src/app/services/data.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {

  settings!: {}

  form = this.fb.group({
    parallel: this.fb.array([
    ]),
    cross: this.fb.array([
    ]),
    point: this.fb.array([
    ]),
    laser: this.fb.array([
    ])
  });


  constructor(private fb: FormBuilder, private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getSettings().subscribe((settings) => {
      this.settings = settings
      console.log(this.settings)
      this.addLaser();
      this.addParallel();
      this.addPoint();
      this.addCross();
    })
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

  addLaser() {
    const parallelForm = this.fb.group({
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
  }


  onSubmit() {
      this.dataService.saveLaserParams(this.form.value).subscribe((res: any) => {
        //this.router.navigate(['home/user']).then(_ => this.dialogRef.close());
      }, (err: any) => {
        console.log(err);
      });;
  
  }

}
