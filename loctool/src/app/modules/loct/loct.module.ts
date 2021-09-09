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
import { MatStepperModule } from '@angular/material/stepper';
import { DataComponent } from './data/data.component';
import { PartableComponent } from '../../components/partable/partable.component';
import { DragDropModule } from '@angular/cdk/drag-drop';
import { MatExpansionModule } from '@angular/material/expansion';


@NgModule({
  declarations: [
    LoctComponent,
    DataComponent,
    PartableComponent,
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
    MatStepperModule,
    DragDropModule,
    MatExpansionModule,
  ]
})
export class LoctModule { }
