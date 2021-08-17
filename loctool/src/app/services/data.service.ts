import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import { tap } from 'rxjs/operators';

const API_URL = 'http://localhost:8000';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getMyData(): Observable<any> {
    return this.http.get<any>(API_URL + '/me').pipe(tap(res => console.log(res.email)));
  }

  getAllUsers(): Observable<any> {
    return this.http.get<any>(API_URL + '/users').pipe(tap(res => console.log(res)));
  }

}
