import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component, ElementRef, OnInit, ViewChild, ViewChildren} from '@angular/core';
import * as Plotly from 'src/assets/plotly-latest.min.js';
import { Subscription } from 'rxjs';
import { DataService } from '../../../services/data.service';
import { SidenavService } from '../../../services/sidenav.service';
import { SharingService } from '../../../services/sharing.service';
import { QueryList } from '@angular/core';



@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css']
})



export class AnalysisComponent implements OnInit {

  basket: string[] = [
  ];

  basketL: string[] = [
  ];

  basketR: string[] = [
  ];

  crossPlots: any[] = ["c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"];
  parallelPlots: any[] = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"];
  pointPlots: any[] = ["o0", "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10"];

  loader!: boolean;
  loadersubscription!: Subscription;
  selRow: any[] = [];
  rowsubscription!: Subscription;
  colsubscription!: Subscription;

  subscription?: Subscription;

  constructor(private sideNavService: SidenavService, private dataService: DataService, private share: SharingService) { }

  ngOnInit(): void {
    console.log(this.selRow)
    this.loadersubscription = this.share.loaderSource.subscribe(loader => this.loader = loader)
    this.rowsubscription = this.share.selRowSource.subscribe(selRow => this.selRow = selRow)
    this.colsubscription = this.share.selColSource.subscribe(selCol => this.basket = selCol)
  }

  ngOnDestroy() {
    this.colsubscription?.unsubscribe();
    this.rowsubscription?.unsubscribe();
    this.loadersubscription?.unsubscribe();
  }

  toggleSidenav() {
    this.sideNavService.toggle();
  }

  newLoader(load: boolean) {
    this.share.changeLoader(load);
  }

  drop(event: CdkDragDrop<string[]>) {
    if (event.previousContainer === event.container) {
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      transferArrayItem(event.previousContainer.data,
        event.container.data,
        event.previousIndex,
        event.currentIndex);
    }
  }

  
  getDashboard() {
    console.log("Dashboard Data Received");
    this.newLoader(true);

    this.dataService.getDashboard(this.selRow).subscribe((data) => {

      document.getElementById('cross')!.textContent = data["crosstext"];
      data["cross"].forEach((value, index) => {
        if (value.data.length !== 0) { Plotly.newPlot("c" + String(index), value) }
      });

      document.getElementById('parallel')!.textContent = data["paralleltext"];
      data["parallel"].forEach((value, index) => {
        if (value.data.length !== 0) { Plotly.newPlot("p" + String(index), value) }
      });

      document.getElementById('point')!.textContent = data["pointtext"];
      data["point"].forEach((value, index) => {
        if (value.data.length !== 0) { Plotly.newPlot(String("o" + index), value) }
      });


      this.newLoader(false);
    })
  }



}
