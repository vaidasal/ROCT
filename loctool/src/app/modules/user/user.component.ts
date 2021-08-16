import { Component, OnInit } from '@angular/core';

import {MatDialog} from '@angular/material/dialog';
import { RegisterComponent } from 'src/app/components/register/register.component';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openDialog() {
    this.dialog.open(RegisterComponent, {
      width: '500px',
    });
  }

}
