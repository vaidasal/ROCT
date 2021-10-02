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
import { FilterComponent } from '../../components/filter/filter.component';
import { AnalysisComponent } from './analysis/analysis.component';
import { DataentryComponent } from './dataentry/dataentry.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDividerModule } from '@angular/material/divider';
import { MatCardModule } from '@angular/material/card';
import { MatChipsModule } from '@angular/material/chips';
import { MatTabsModule } from '@angular/material/tabs';
import { MatSelectModule } from '@angular/material/select';


@NgModule({
  declarations: [
    LoctComponent,
    DataComponent,
    PartableComponent,
    FilterComponent,
    AnalysisComponent,
    DataentryComponent,
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
    ReactiveFormsModule,
    MatDividerModule,
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatCardModule,
    FormsModule,
    MatChipsModule,
    MatTabsModule,
    MatSelectModule,
  ]
})
export class LoctModule { }
