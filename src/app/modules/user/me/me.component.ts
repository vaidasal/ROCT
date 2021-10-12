import { ThrowStmt } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DataService } from 'src/app/services/data.service';
import { ChangepwComponent } from '../changepw/changepw.component';

@Component({
  selector: 'app-me',
  templateUrl: './me.component.html',
  styleUrls: ['./me.component.css']
})
export class MeComponent implements OnInit {

  message = '';
  firstname = '';
  lastname = '';
  email = '';
  scope = '';
  isLoadingResults = false;

  constructor(private dataService: DataService, private dialog: MatDialog) { }

  ngOnInit(): void {
    this.isLoadingResults = true;
    this.dataService.getMyData().subscribe((data: any) => {
      this.message = data;
      this.firstname = data.firstname;
      this.lastname = data.lastname;
      this.email = data.email;
      this.scope = data.scope;
      this.isLoadingResults = false;
    });;
  }

  openPasswordDialog() {
    this.dialog.open(ChangepwComponent, {
      width: '500px',
    });
  }



  
}
