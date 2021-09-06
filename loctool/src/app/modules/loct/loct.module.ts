import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoctRoutingModule } from './loct-routing.module';
import { LoctComponent } from './loct.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';


@NgModule({
  declarations: [
    LoctComponent,
  ],
  imports: [
    CommonModule,
    LoctRoutingModule,
    MatPaginatorModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
    MatSidenavModule,
    MatButtonModule,
    MatIconModule,
  ]
})
export class LoctModule { }
