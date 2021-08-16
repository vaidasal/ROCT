import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NewUserRoutingModule } from './new-user-routing.module';
import { NewUserComponent } from './new-user.component';
import { MatIconModule } from '@angular/material/icon';
import { MatRadioModule } from '@angular/material/radio';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';
import {MatCardModule} from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';


@NgModule({
  declarations: [
    NewUserComponent
  ],
  imports: [
    CommonModule,
    NewUserRoutingModule,
    MatIconModule,
    MatRadioModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatCardModule,
    MatProgressSpinnerModule,
  ]
})
export class NewUserModule { }
