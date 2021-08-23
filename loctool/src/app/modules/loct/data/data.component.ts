import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/services/data.service';
import { SidenavService } from 'src/app/services/sidenav.service';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit {

  constructor(private dataService: DataService, private sideNavService: SidenavService) { }

  ngOnInit(): void {
  }

  refresh(): void {
    this.dataService.getRefreshCSV().subscribe((data: any) => {console.log(data)});;
  }

  toggleSidenav() { 
    this.sideNavService.toggle();
  }

}
