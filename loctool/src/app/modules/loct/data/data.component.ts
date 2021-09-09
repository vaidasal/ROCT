import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/services/data.service';
import { SidenavService } from 'src/app/services/sidenav.service';
import { Subscription } from 'rxjs';
import { SharingService } from '../../../services/sharing.service';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnInit {

  loader!: boolean;
  subscription!: Subscription;

  

  constructor(private dataService: DataService, private sideNavService: SidenavService, private share: SharingService) { }

  ngOnInit(): void {
    this.subscription = this.share.loaderSource.subscribe(loader => this.loader = loader)
  }

  refresh(): void {
    this.newLoader(true);
    this.dataService.getRefreshCSV().subscribe((data: any) => {
      console.log(data);
      this.newLoader(false);
      location.reload();
    });;
  }

  toggleSidenav() { 
    this.sideNavService.toggle();
  }

  newLoader(load: boolean) {
    this.share.changeLoader(load);
  }

}
