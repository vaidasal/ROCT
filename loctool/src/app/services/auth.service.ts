import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders, HttpParams} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {catchError, tap} from 'rxjs/operators';
import {TokenService} from './token.service';

const OAUTH_CLIENT = 'express-client';
const OAUTH_SECRET = 'express-secret';
const API_URL = 'http://localhost:8000';
const HTTP_OPTIONS = {
  headers: new HttpHeaders({
    'Content-Type': 'application/x-www-form-urlencoded',
    Authorization: 'Basic ' + btoa(OAUTH_CLIENT + ':' + OAUTH_SECRET)
  })
};


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  redirectUrl = '';

  private static handleError(error: HttpErrorResponse): any {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    return throwError('Something bad happened; please try again later.');
  }

  private static log(message: string): any {
    console.log(message);
  }

  constructor(private http: HttpClient, private tokenService: TokenService) { }

  login(loginData: any): Observable<any> {
    this.tokenService.removeToken();
    this.tokenService.removeRefreshToken();
    const body = new HttpParams()
      .set('username', loginData.username)
      .set('password', loginData.password)

    return this.http.post<any>(API_URL + '/login', body, HTTP_OPTIONS)
      .pipe(
        tap(res => {
          this.tokenService.saveToken(res.access_token);
          this.tokenService.saveRefreshToken(res.refresh_token);
          this.tokenService.saveScope(res.scope);
          this.tokenService.saveName(res.name);
        }),
        catchError(AuthService.handleError)
      );
  }

  refreshToken(refreshData: any): Observable<any> {
    this.tokenService.removeToken();
    this.tokenService.removeRefreshToken();
    const body = new HttpParams()
      .set('refresh_token', refreshData.refresh_token)
      .set('grant_type', 'refresh_token');
      console.log('refresh')
    return this.http.post<any>(API_URL + '/login', body, HTTP_OPTIONS)
      .pipe(
        tap(res => {
          this.tokenService.saveToken(res.access_token);
          this.tokenService.saveRefreshToken(res.refresh_token);
        }),
        catchError(AuthService.handleError)
      );
  }

  logout(): void {
    this.tokenService.removeToken();
    this.tokenService.removeRefreshToken();
  }

  register(data: any): Observable<any> {
    return this.http.post<any>(API_URL + '/users/', data)
      .pipe(
        tap(_ => AuthService.log('register')),
        catchError(AuthService.handleError)
      );
  }

  secured(): Observable<any> {
    console.log("secured");
    return this.http.get<any>(API_URL + '/me')
      .pipe(catchError(AuthService.handleError));
  }

  changePW(data: any): Observable<any> {
    console.log(data);
    return this.http.post<any>(API_URL + '/newpw', data)
      .pipe(
        tap(_ => AuthService.log('newPW')),
        catchError(AuthService.handleError)
      );
  }

  update(data: any): Observable<any> {
    console.log("UPDATE!!");
    console.log(data);
    return this.http.post<any>(API_URL + '/update', data)
      .pipe(
        tap(_ => AuthService.log('updating')),
        catchError(AuthService.handleError)
      );
  }

  delete(id: number): Observable<any> {
    return this.http.delete(API_URL + '/delete/' + String(id))
      .pipe(
        tap(_ => AuthService.log('deleting')),
        catchError(AuthService.handleError)
      );
  }


}
