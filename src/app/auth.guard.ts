import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, Router } from '@angular/router';
import {AuthService} from './services/auth.service';
import {TokenService} from './services/token.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private tokenService: TokenService, private router: Router) {
  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): boolean {
      const url: string = state.url;
      return this.checkLogin(url);
    }

  checkLogin(url: string): boolean {
    if (this.tokenService.getRefreshToken()) {
      return true;
    }

    this.authService.redirectUrl = url;

    this.router.navigate(['/login']);
    return false;
  }
  
}
