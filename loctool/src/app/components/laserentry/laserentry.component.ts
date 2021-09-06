import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { DataService } from 'src/app/services/data.service';

@Component({
  selector: 'app-laserentry',
  templateUrl: './laserentry.component.html',
  styleUrls: ['./laserentry.component.css']
})
export class LaserentryComponent implements OnInit {

  laserEntry!: FormGroup;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
  }

  onFormSubmit(): void {
    this.dataService.saveLaserParams(this.laserEntry.value)
      .subscribe(() => {
        //this.router.navigate(['/home/loct/data']).then(_ => console.log('You are secure now!'));
      }, (err: any) => {
        console.log(err);
      });
  }


}
