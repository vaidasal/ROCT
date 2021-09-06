import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { RegisterComponent } from 'src/app/modules/user/register/register.component';
import { UpdateComponent } from 'src/app/modules/user/update/update.component';
import { DataService } from 'src/app/services/data.service';

export interface User {
  id: number;
  firstname: string;
  lastname: string;
  email: string;
  scope: string;
}

@Component({
  selector: 'app-usertable',
  templateUrl: './usertable.component.html',
  styleUrls: ['./usertable.component.css']
})
export class UsertableComponent implements OnInit {

  displayedColumns: string[] = ['id','name','email','scope'];
  dataSource!: MatTableDataSource<User>;

  @ViewChild('paginator') paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private dataService: DataService, private dialog: MatDialog) {
    this.dataService.getAllUsers().subscribe((users) => {
      this.dataSource = new MatTableDataSource(users);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    })
   }
   
   openDialog(row) {
     console.log(row);
    this.dialog.open(UpdateComponent, {
      width: '500px', data: {data: row}
    });
  }

  openNewUserDialog() {
    this.dialog.open(RegisterComponent, {
      width: '500px',
    });
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim(); // Remove whitespace
    filterValue = filterValue.toLowerCase(); // Datasource defaults to lowercase matches
    this.dataSource.filter = filterValue;
  }

  ngOnInit(): void {
  }

}
