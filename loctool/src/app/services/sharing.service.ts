import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharingService {

  private messageSource = new BehaviorSubject<boolean>(false);
  loaderSource = this.messageSource.asObservable();

  private selectedRowSource = new BehaviorSubject<any[]>([]);
  selRowSource = this.selectedRowSource.asObservable();

  private selectedColSource = new BehaviorSubject<any[]>(['seamid', 'type', 'line_length']);
  selColSource = this.selectedColSource.asObservable();

  constructor() { }

  changeLoader(message: boolean) {
    this.messageSource.next(message)
  }

  changeSelRow(rows) {
    this.selectedRowSource.next(rows)
  }

  changeSelCol(cols) {
    this.selectedColSource.next(cols)
  }

}
