import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { UserComponent } from './user.component';
import { MatIconModule } from '@angular/material/icon';
import { RegisterComponent } from 'src/app/modules/user/register/register.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';
import { UpdateComponent } from './update/update.component';
import { ChangepwComponent } from './changepw/changepw.component';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { UsertableComponent } from 'src/app/components/usertable/usertable.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatRadioModule } from '@angular/material/radio';
import { FlexLayoutModule } from '@angular/flex-layout';
import {MatDividerModule} from '@angular/material/divider';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';


@NgModule({
  declarations: [
    UserComponent,
    UpdateComponent,
    ChangepwComponent,
    UsertableComponent,
  ],
  entryComponents: [
    RegisterComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    MatIconModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatProgressSpinnerModule,
    MatTableModule,
    MatPaginatorModule,
    MatRadioModule,
    FlexLayoutModule,
    MatDividerModule,
    MatToolbarModule,
    MatButtonModule,
  ]
})
export class UserModule { }
