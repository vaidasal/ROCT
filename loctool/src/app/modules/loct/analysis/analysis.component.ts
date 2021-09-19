import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import * as Plotly from 'src/assets/plotly-latest.min.js';
import { Subscription } from 'rxjs';
import { DataService } from '../../../services/data.service';
import { SidenavService } from '../../../services/sidenav.service';



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

  subscription?: Subscription;

  constructor(private sideNavService: SidenavService, private dataService: DataService) { }

  ngOnInit(): void {
    this.subscription = this.dataService.currentParameter.subscribe(parameter => this.basket = parameter)
  }

  ngOnDestroy() {
    this.subscription?.unsubscribe();
  }

  toggleSidenav() {
    this.sideNavService.toggle();
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
    this.dataService.getDashboard().subscribe((data) => {
      Plotly.newPlot('StepLine', data[1]);
      Plotly.newPlot('HeatSub', data[0]);
      
    })
  }

}
