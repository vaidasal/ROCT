import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Subscription } from 'rxjs';
import { DataService } from 'src/app/services/data.service';
import { SharingService } from '../../services/sharing.service';
import { UpdateComponent } from '../update/update.component';


@Component({
  selector: 'app-partable',
  templateUrl: './partable.component.html',
  styleUrls: ['./partable.component.css']
})
export class PartableComponent implements OnInit {

  selectedRows: any[] = [];
  rowsubscription!: Subscription;
  colsubscription!: Subscription;

  constructor(private dataService: DataService, private dialog: MatDialog, private share: SharingService) {}

  ngOnInit(): void {
    this.getTable()
    this.rowsubscription = this.share.selRowSource.subscribe(selRow => this.selectedRows = selRow)
    this.colsubscription = this.share.selColSource.subscribe(selCol => this.basket = selCol)
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
    this.share.changeSelCol(this.basket);
    this.selectedRows = []
    this.getTable();
  }

  getTable() {
    console.log(this.basket);
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

  select(row) {
    if (this.selectedRows.includes(row)) {
      this.selectedRows = this.selectedRows.filter(item => item !== row)
    } else {
      this.selectedRows.push(row)
    }
    this.newRow(this.selectedRows)
    console.log(this.selectedRows)
  }

  ngOnDestroy() {
    this.colsubscription?.unsubscribe();
    this.rowsubscription?.unsubscribe();
  }

  newRow(rows) {
    this.share.changeSelRow(rows);
  }

}
