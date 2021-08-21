import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoctRoutingModule } from './loct-routing.module';
import { LoctComponent } from './loct.component';
import { OctcsvComponent } from 'src/app/components/octcsv/octcsv.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';


@NgModule({
  declarations: [
    LoctComponent,
    OctcsvComponent,
  ],
  imports: [
    CommonModule,
    LoctRoutingModule,
    MatPaginatorModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
  ]
})
export class LoctModule { }
