import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { UserComponent } from './user.component';
import { MatIconModule } from '@angular/material/icon';
import { RegisterComponent } from 'src/app/components/register/register.component';
import { MatDialogModule } from '@angular/material/dialog';


@NgModule({
  declarations: [
    UserComponent,
  ],
  entryComponents: [
    RegisterComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    MatIconModule,
    MatDialogModule,
  ]
})
export class UserModule { }
