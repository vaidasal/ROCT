import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { DataService } from 'src/app/services/data.service';


export interface OctCSV {
  id: number;
  status: string;
  seamid: number;
  linenumber: number;
  type: string;
  time: string;
  userid: number;
}

@Component({
  selector: 'app-octcsv',
  templateUrl: './octcsv.component.html',
  styleUrls: ['./octcsv.component.css']
})
export class OctcsvComponent implements OnInit {

  displayedColumns: string[] = ['id','status','seamid','linenumber','type','time','userid', 'grouporder'];
  dataSource!: MatTableDataSource<OctCSV>;

  @ViewChild('paginator') paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private dataService: DataService, private dialog: MatDialog) {
    this.dataService.getOctCSV().subscribe((octcsv) => {
      this.dataSource = new MatTableDataSource(octcsv);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    })
   }
   
   openDialog(row) {
     console.log(row);
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim(); // Remove whitespace
    filterValue = filterValue.toLowerCase(); // Datasource defaults to lowercase matches
    this.dataSource.filter = filterValue;
  }

  ngOnInit(): void {
  }

}
