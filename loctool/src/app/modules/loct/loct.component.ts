import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { SidenavService } from '../../services/sidenav.service';

@Component({
  selector: 'app-loct',
  templateUrl: './loct.component.html',
  styleUrls: ['./loct.component.css']
})
export class LoctComponent implements OnInit {

  @ViewChild('drawer', { static: true }) public sidenav!: MatSidenav;

  constructor(private sideNavService: SidenavService) { }

  ngOnInit(): void {
    this.sideNavService.sideNavToggleSubject.subscribe(()=> {
      this.sidenav.toggle();
    });

    this.sidenav.open();
  }

}
