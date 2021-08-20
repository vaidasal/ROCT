import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharingService {

  private messageSource = new BehaviorSubject<boolean>(false);
  loaderSource = this.messageSource.asObservable();

  constructor() { }

  changeLoader(message: boolean) {
    this.messageSource.next(message)
  }

  
}
