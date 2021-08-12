import { Component, OnInit } from '@angular/core';

import {ErrorStateMatcher} from '@angular/material/core';
import {FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import {AuthService} from '../../services/auth.service';
import {Router} from '@angular/router';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['../../app.component.scss']
})
export class RegisterComponent implements OnInit {

  registerForm!: FormGroup;
  email = '';
  password = '';
  firstname = '';
  lastname = '';
  scopes = '';
  isLoadingResults = false;
  matcher = new MyErrorStateMatcher();

  constructor(private authService: AuthService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      email : [null, Validators.required],
      password : [null, Validators.required],
      firstname : [null, Validators.required],
      lastname : [null, Validators.required],
      scopes : [null]
    });
  }

  onFormSubmit(): void {
    this.isLoadingResults = true;
    console.log(this.registerForm.value)
    console.log(this.registerForm.get('scopes'))
    this.authService.register(this.registerForm.value)
      .subscribe((res: any) => {
        this.isLoadingResults = false;
        this.router.navigate(['/login']).then(_ => console.log('You are registered now!'));
      }, (err: any) => {
        console.log(err);
        this.isLoadingResults = false;
      });
  }

}
