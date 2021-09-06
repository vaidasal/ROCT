import { Component, Inject, OnInit } from '@angular/core';
import { inject } from '@angular/core/testing';
import { FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['../../../app.component.scss']
})
export class UpdateComponent implements OnInit {

  updateForm!: FormGroup;
  email = '';
  new_password = '';
  firstname = '';
  lastname = '';
  scope = '';
  id = '';
  isLoadingResults = false;
  matcher = new MyErrorStateMatcher();
  formValues: any;

  constructor(private authService: AuthService, private router: Router, private formBuilder: FormBuilder,
    public dialogRef: MatDialogRef<UpdateComponent>, @Inject(MAT_DIALOG_DATA) public row: any) { }

  ngOnInit(): void {
    console.log(this.row.data);
    this.updateForm = this.formBuilder.group({
      email : [this.row.data.email, Validators.required],
      new_password : ['old password', Validators.required],
      firstname : [this.row.data.firstname, Validators.required],
      lastname : [this.row.data.lastname, Validators.required],
      scope : [this.row.data.scopes],
      id : [String(this.row.data.id)],
    });
    console.log(this.row.data.scope)
    this.updateForm.patchValue({scope:this.row.data.scope});
  }

  onFormSubmit(): void {
    this.isLoadingResults = true;
    this.authService.update(this.updateForm.value)
      .subscribe((res: any) => {
        this.isLoadingResults = false;
        this.dialogRef.close();
        location.reload();
      }, (err: any) => {
        console.log(err);
        this.isLoadingResults = false;
      });
  }

  onDelete(): void {
    this.isLoadingResults = true;
    this.authService.delete(this.updateForm.value.id)
      .subscribe((res: any) => {
        this.isLoadingResults = false;
        this.dialogRef.close();
        location.reload();
      }, (err: any) => {
        console.log(err);
        this.isLoadingResults = false;
      });
  }

}
