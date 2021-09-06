import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<UpdateComponent>, @Inject(MAT_DIALOG_DATA) public row: any) { }

  ngOnInit(): void {
  }

}
