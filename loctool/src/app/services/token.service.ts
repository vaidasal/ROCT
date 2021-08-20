import { Injectable } from '@angular/core';

const ACCESS_TOKEN = 'access_token';
const REFRESH_TOKEN = 'refresh_token';
const SCOPE = 'scope';
const NAME = '';

@Injectable({
  providedIn: 'root'
})
export class TokenService {

  constructor() { }

  getToken(): string {
    return localStorage.getItem(ACCESS_TOKEN) || '';
  }

  getRefreshToken(): string {
    return localStorage.getItem(REFRESH_TOKEN) || '';
  }

  saveToken(token): void {
    localStorage.setItem(ACCESS_TOKEN, token);
  }

  saveRefreshToken(refreshToken): void {
    localStorage.setItem(REFRESH_TOKEN, refreshToken);
  }

  removeToken(): void {
    localStorage.removeItem(ACCESS_TOKEN);
  }

  removeRefreshToken(): void {
    localStorage.removeItem(REFRESH_TOKEN);
  }

  saveScope(scope): void {
    localStorage.setItem(SCOPE, scope);
  }

  getScope(): string {
    return localStorage.getItem(SCOPE) || '';
  }

  saveName(name): void {
    localStorage.setItem(NAME, name);
  }

  getName(): string {
    return localStorage.getItem(NAME) || '';
  }


}
