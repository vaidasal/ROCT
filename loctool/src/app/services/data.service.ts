import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
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
    console.log("Refresh!!")
    return this.http.get<any>(API_URL + '/refresh').pipe(tap(res => console.log(res)));
  }

  getSettings(): Observable<any> {
    console.log("get Settings!!")
    return this.http.get<any>(API_URL + '/settings').pipe(tap(res => console.log(res)));
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
        tap(_ => console.log('ParamTableRequest'))
      );
  }

  getDashboard(rows: any): Observable<any> {
    return this.http.post<any>(API_URL + '/dashboard', rows)
      .pipe(
        tap(_ => console.log('DashboardRequest'))
      );
  }

  getCustomPlot(rowsAndAxes: any): Observable<any> {
    return this.http.post<any>(API_URL + '/customplot', rowsAndAxes)
      .pipe(
        tap(_ => console.log('CustomPlotRequest'))
      );
  }





}
