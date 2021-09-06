import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DataentryRoutingModule } from './dataentry-routing.module';
import { DataentryComponent } from './dataentry.component';
import { LaserentryComponent } from 'src/app/components/laserentry/laserentry.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { OctparallelentryComponent } from 'src/app/components/octparallelentry/octparallelentry.component';
import { OctpointentryComponent } from 'src/app/components/octpointentry/octpointentry.component';
import { OctcrossentryComponent } from 'src/app/components/octcrossentry/octcrossentry.component';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatChipsModule } from '@angular/material/chips';
import { DragDropModule } from '@angular/cdk/drag-drop';


@NgModule({
  declarations: [
    DataentryComponent,
    OctparallelentryComponent,
    OctpointentryComponent,
    OctcrossentryComponent,
  ],
  imports: [
    CommonModule,
    DataentryRoutingModule,
    MatFormFieldModule,
    MatInputModule,
    MatCardModule,
    MatDividerModule,
    MatButtonModule,
    FormsModule,
    MatIconModule,
    ReactiveFormsModule,
    MatIconModule,
    MatChipsModule,
    DragDropModule,
  ]
})
export class DataentryModule { }
