import { Component, OnInit } from '@angular/core';

import {AuthService} from '../../services/auth.service';
import {ErrorStateMatcher} from '@angular/material/core';
import {FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import { SharingService } from 'src/app/services/sharing.service';
import { Subscription } from 'rxjs';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['../../app.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm!: FormGroup;
  username = '';
  password = '';
  isLoadingResults = false;
  matcher = new MyErrorStateMatcher();

  loader!: boolean;
  subscription!: Subscription;

  

  constructor(private authService: AuthService, private router: Router, private formBuilder: FormBuilder, private share: SharingService) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      username : [null, Validators.required],
      password : [null, Validators.required]
    });
    this.subscription = this.share.loaderSource.subscribe(loader => this.loader = loader)
  }

  newLoader(load: boolean) {
    this.share.changeLoader(load);
  }

  onFormSubmit(): void {
    this.newLoader(true);
    this.authService.login(this.loginForm.value)
      .subscribe(() => {
        this.newLoader(false);
        this.router.navigate(['/home/loct/data']).then(_ => console.log('You are secure now!'));
      }, (err: any) => {
        console.log(err);
        this.newLoader(false);
      });
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}


