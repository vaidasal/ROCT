import { Component, Inject, OnInit } from '@angular/core';
import { FormArray, FormBuilder } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { SharingService } from '../../services/sharing.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent implements OnInit {

  updateForm = this.fb.group({
    fields: this.fb.array([
    ])
  });

  fieldLabels: string[] = [];

  loader!: boolean;
  subscription!: Subscription;

  constructor(private fb: FormBuilder, public dialogRef: MatDialogRef<UpdateComponent>, @Inject(MAT_DIALOG_DATA) public row: any, private share: SharingService) { }

  ngOnInit(): void {
    this.subscription = this.share.loaderSource.subscribe(loader => this.loader = loader)
    console.log(this.row.data);
    this.addFields();
    console.log(this.updateForm);
  }

  get fields() {
    return this.updateForm.get('fields') as FormArray;
  }

  addFields() {
    for (var val in this.row.data) {
      console.log(val);
      this.fields.push(this.fb.control(this.row.data[val]));
      this.fieldLabels.push(val);
    }
  }

  newLoader(load: boolean) {
    this.share.changeLoader(load);
  }

  onFormSubmit(): void {
    this.newLoader(true);
    var data = this.updateForm.value.fields
    var dict: { [name: string]: any } = {}
    data.forEach((value, i) => {
      dict[this.fieldLabels[i]] = value
    })
    console.log(dict)
    this.newLoader(false);
    
  }

}
