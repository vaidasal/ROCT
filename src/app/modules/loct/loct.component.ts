import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { Subscription } from 'rxjs';
import { DataService } from '../../services/data.service';
import { SharingService } from '../../services/sharing.service';
import { SidenavService } from '../../services/sidenav.service';

@Component({
  selector: 'app-loct',
  templateUrl: './loct.component.html',
  styleUrls: ['./loct.component.css']
})
export class LoctComponent implements OnInit {

  isLinear = true;

  selRow: any[] = [];
  rowsubscription!: Subscription;
  colsubscription!: Subscription;
  cols: string[] = [];
  selectedIndex: number = 1

  @ViewChild('drawer', { static: true }) public sidenav!: MatSidenav;

  constructor(private sideNavService: SidenavService, private share: SharingService, private dataService: DataService) { }

  ngOnInit(): void {
    this.rowsubscription = this.share.selRowSource.subscribe(selRow => this.selRow = selRow)
    this.sideNavService.sideNavToggleSubject.subscribe(()=> {
      this.sidenav.toggle();
    });

    this.sidenav.close();
  }

  changeIndex(event) {
    this.selectedIndex = event.selectedIndex
  }


}
