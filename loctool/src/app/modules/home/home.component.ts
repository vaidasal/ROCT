import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { TokenService } from 'src/app/services/token.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router, private tokenService: TokenService) { }

  title = 'LOCTool';
  name = '';

  ngOnInit(): void {
    this.name = this.tokenService.getName()
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']).then(_ => console.log('Logout'));
  }

}
