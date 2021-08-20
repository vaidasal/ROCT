import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { DataService } from 'src/app/services/data.service';
import { TokenService } from 'src/app/services/token.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router, private tokenService: TokenService, private dataService: DataService) { }

  title = 'LOCTool';
  name = '';
  access = false;

  ngOnInit(): void {
    this.name = this.tokenService.getName()
    if (this.tokenService.getScope() == "admin") {this.access = true}
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']).then(_ => console.log('Logout'));
  }

  refresh(): void {
    this.dataService.getRefreshCSV().subscribe((data: any) => {console.log(data)});;
  }

}
