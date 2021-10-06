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
  material!: []
  cabin = ["Cabin 1", "Cabin 2", "Cabin 3", "Cabin 4", "Cabin 5", "Cabin 6", "Cabin 7"]

  form = this.fb.group({
    main: this.fb.array([
    ])
  });


  constructor(private fb: FormBuilder, private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getSettings().subscribe((settings) => {
      this.settings = settings
      this.material = JSON.parse(settings["material"])
      this.addFormFields();
    })
  }

  get main() {
    return this.form.get('main') as FormArray;
  }

  addFormFields() {
    const formGroup = this.fb.group({
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

    this.main.push(formGroup);
  }





  onSubmit() {
      this.dataService.saveLaserParams(this.form.value).subscribe((res: any) => {
        //this.router.navigate(['home/user']).then(_ => this.dialogRef.close());
      }, (err: any) => {
        console.log(err);
      });;
  
  }

}
