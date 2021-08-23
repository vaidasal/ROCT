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
    console.log("USERS")
    return this.http.get<any>(API_URL + '/users').pipe(tap(res => console.log(res)));
  }

  getOctCSV(): Observable<any> {
    console.log("OctCSV")
    return this.http.get<any>(API_URL + '/octcsv').pipe(tap(res => console.log(res)));
  }

  getRefreshCSV(): Observable<any> {
    console.log("get!!")
    return this.http.get<any>(API_URL + '/refresh').pipe(tap(res => console.log(res)));
  }

  saveLaserParams(form_data: any): Observable<any> {
    return this.http.post<any>(API_URL + '/addparameters', form_data)
      .pipe(
        tap(_ => console.log('saved'))
      );
  }

  postParamTable(cols: any): Observable<any> {
    return this.http.post<any>(API_URL + '/postparamtable', cols)
      .pipe(
        tap(_ => console.log('requested'))
      );
  }


}
