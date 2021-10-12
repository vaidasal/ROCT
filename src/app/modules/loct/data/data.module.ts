import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DataRoutingModule } from './data-routing.module';
import { OctcsvComponent } from 'src/app/components/octcsv/octcsv.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

import {MatExpansionModule} from '@angular/material/expansion';
import {MatCheckboxModule} from '@angular/material/checkbox';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDividerModule } from '@angular/material/divider';
import { DragDropModule } from '@angular/cdk/drag-drop';
import { MatSortModule } from '@angular/material/sort';
import {MatGridListModule} from '@angular/material/grid-list';
import { UpdateComponent } from 'src/app/components/update/update.component';
import { LaserentryComponent } from 'src/app/components/laserentry/laserentry.component';



@NgModule({
  declarations: [
    OctcsvComponent,
    UpdateComponent,
    LaserentryComponent,
  ],
  imports: [
    CommonModule,
    DataRoutingModule,
    MatFormFieldModule,
    MatTableModule,
    MatPaginatorModule,
    MatIconModule,
    MatButtonModule,
    MatInputModule,
    MatExpansionModule,
    MatCheckboxModule,
    ReactiveFormsModule,
    MatDividerModule,
    DragDropModule,
    MatSortModule,
    MatGridListModule,
    FormsModule,
  ]
})
export class DataModule { }
