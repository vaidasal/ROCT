import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnalysisComponent } from './analysis.component';
import { MatButtonModule } from '@angular/material/button';
import { DragDropModule } from '@angular/cdk/drag-drop';



@NgModule({
  declarations: [
    AnalysisComponent,
  ],
  imports: [
    CommonModule,
    MatButtonModule,
    DragDropModule,
  ]
})
export class AnalysisModule { }
