import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { DataService } from 'src/app/services/data.service';
import { UpdateComponent } from '../update/update.component';


@Component({
  selector: 'app-partable',
  templateUrl: './partable.component.html',
  styleUrls: ['./partable.component.css']
})
export class PartableComponent implements OnInit {

  constructor(private dataService: DataService, private dialog: MatDialog) {}

  ngOnInit(): void {
    this.getTable()
  }
  
  dataSource!: MatTableDataSource<any>;
  @ViewChild('paginator_partable') mpaginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  bag1 = [
    'points_per_line',
    'points_per_interval',
    'extend_points',
    'frequency',
  ];

  bag2 = [
    'seam_length',
    'speed',
    'step_size_oct_tester',
    'x_start',
    'x_end',
    'y_start',
    'y_end',
    'x_ref_coordinate',
    'y_ref_coordinate',
    'jump_speed',
    'scantype',
  ];

  bag3 = [
    'seam_length',
    'step_size_oct_tester',
    'reference_points',
    'extend_reference_points',
    'lag_xy',
    'status',
    'linenumber',
    'datetime',
    'userid',
    'grouporder',
    'firstname',
    'lastname',
  ];

  basket: string[] = [
    'seamid', 'type', 'line_length',
  ];

  drop(event: CdkDragDrop<string[]>) {
    if (event.previousContainer === event.container) {
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      transferArrayItem(event.previousContainer.data,
                        event.container.data,
                        event.previousIndex,
                        event.currentIndex);
    }
    this.getTable();
  }

  getTable() {
    this.dataService.postParamTable(this.basket).subscribe((data) => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.mpaginator;
      this.dataSource.sort = this.sort;
  })}

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim(); // Remove whitespace
    filterValue = filterValue.toLowerCase(); // Datasource defaults to lowercase matches
    this.dataSource.filter = filterValue;
  }
  
  openDialog(row) {
    this.dialog.open(UpdateComponent, {
      data: { data: row },
    });
  }

  selectedRows: any[] = [];

  select(row) {
    if (this.selectedRows.includes(row)) {
      this.selectedRows = this.selectedRows.filter(item => item !== row)
    } else {
      this.selectedRows.push(row)
    }
    console.log(this.selectedRows)
  }




}
