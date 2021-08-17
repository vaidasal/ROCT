import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';
import { MatDialogRef } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-changepw',
  templateUrl: './changepw.component.html',
  styleUrls: ['./changepw.component.css']
})
export class ChangepwComponent implements OnInit {

  changepwForm!: FormGroup;
  password = '';
  newPassword = '';
  isLoadingResults = false;
  matcher = new MyErrorStateMatcher();

  constructor(private authService: AuthService, private router: Router, private formBuilder: FormBuilder, public dialogRef: MatDialogRef<ChangepwComponent>) { }

  ngOnInit(): void {
    this.changepwForm = this.formBuilder.group({
      password : [null, Validators.required],
      newPassword : [null, Validators.required],
    });

  }

  onFormSubmit(): void {
    this.isLoadingResults = true;
    this.authService.changePW(this.changepwForm.value)
      .subscribe((res: any) => {
        this.isLoadingResults = false;
        this.router.navigate(['home/user']).then(_ => this.dialogRef.close());
      }, (err: any) => {
        console.log(err);
        this.isLoadingResults = false;
      });
  }

}
