import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component, ElementRef, OnInit, ViewChild, ViewChildren} from '@angular/core';
import * as Plotly from 'src/assets/plotly-latest.min.js';
import { Subscription } from 'rxjs';
import { DataService } from '../../../services/data.service';
import { SidenavService } from '../../../services/sidenav.service';
import { SharingService } from '../../../services/sharing.service';



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

  basketX: string[] = [
  ];

  crossPlots: any[] = ["c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"];
  parallelPlots: any[] = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"];
  pointPlots: any[] = ["o0", "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10"];
  customPlots: any[] = ["u0", "u1", "u2", "u3", "u4", "u5", "u6", "u7", "u8", "u9", "u10"];
  buttonIds: any[] = ["bu0", "bu1", "bu2", "bu3", "bu4", "bu5", "bu6", "bu7", "bu8", "bu9", "bu10"];

  bag1 = [
    ' OCT_OVEREXPOSED_POINTS',
    ' OCT_AVERAGE_SENSOR_BRIGHTNESS',
  ];


  bag2 = [
    ' OCT_FOCUS_POS',
    ' WELDING_DEPTH_SIGNAL_QUALITY_0',
    ' WELDING_DEPTH_USED_SURFACE_0',
  ];

  bag3 = [
    ' WELDING_DEPTH_POINTS_0',
    ' WELDING_DEPTH_0',
    'timestamp',
    'index',
    'x TCP',
  ];

  bags: Array<String> = []

  chartTypes = [
    'line', 'marker', 'line and marker', 'bar', 'histogram'
  ]

  titleOptions = ["OCT Scan", "Scatter XZ"]
  titlexAx = ["Time", "Timestamp", "Index"]
  titleyAx = ["Depth", "Z"]
  titleyyAx = ["Depth", "Z"]

  seloptionl = "line"
  seloptionr = "line"

  customCharts: Array<any> = []
  darkmodeCheck = true;

  loader!: boolean;
  loadersubscription!: Subscription;
  selRow: any[] = [];
  rowsubscription!: Subscription;

  subscription?: Subscription;

  constructor(private sideNavService: SidenavService, private dataService: DataService, private share: SharingService) { }

  ngOnInit(): void {
    console.log(this.selRow)
    this.loadersubscription = this.share.loaderSource.subscribe(loader => this.loader = loader)
    this.rowsubscription = this.share.selRowSource.subscribe(selRow => this.selRow = selRow)
    this.dataService.getCols(this.selRow).subscribe((data) => {
      const lenOfData = data.length
      const third = Math.floor(lenOfData/3)
      this.bag3 = data.slice(0, third)
      this.bag2 = data.slice(third, third * 2)
      this.bag1 = data.slice(third * 2)
      this.basketX = ["index", "timestamp"]
      if (this.selRow[0]["type"] == "Line") {
        this.basketX = ["index", "timestamp", "xTCP"]
      }
    })
  }

  ngOnDestroy() {
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

  generateCustomPlot(title, xAx, yAx, yyAx) {
    console.log("Custom Plot Data Received");
    this.newLoader(true);
    
    var ch = JSON.parse(JSON.stringify({"rows": this.selRow, "basketL": this.basketL,
      "basketR": this.basketR, "basketX": this.basketX,
      "chartType": [this.seloptionl, this.seloptionr], "chartTitle": title,
      "xAxName": xAx, "yAxName": yAx, "yyAxName": yyAx,"darkmodeCheck": this.darkmodeCheck
    }))
    this.customCharts.push(ch)

    this.dataService.getCustomPlot(this.customCharts).subscribe((data) => {
      document.getElementById('custom')!.textContent = data["customtext"];
      data["custom"].forEach((value, index) => {
        if (value.data.length !== 0) {
          Plotly.newPlot("u" + String(index), value);
          document.getElementById("bu" + String(index))!.style.display = "";
          document.getElementById("u" + String(index))!.style.display = "";
        }
      });


      this.newLoader(false);
    })
  }
  
  getDashboard() {
    console.log("Dashboard Data Received");
    this.newLoader(true);

    const rows = { "rows": this.selRow, "mode": this.darkmodeCheck }

    this.dataService.getDashboard(rows).subscribe((data) => {

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

  onSelChangeL(ev: any) {
    this.seloptionl = ev.source.selected.value
  }
  onSelChangeR(ev: any) {
    this.seloptionr = ev.source.selected.value
  }
  removeChart(id: any) {
    var idnum = id.substring(1)
    this.customCharts.splice(idnum, 1);
    document.getElementById("b" + id)!.style.display = 'none';
    document.getElementById(id)!.style.display = 'none';
  }



}
