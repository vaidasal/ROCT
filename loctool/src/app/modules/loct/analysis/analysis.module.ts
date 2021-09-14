import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnalysisComponent} from './analysis.component';
import { MatButtonModule } from '@angular/material/button';
import { DragDropModule } from '@angular/cdk/drag-drop';

import * as Plotly from 'src/assets/plotly-latest.min.js';
import { PlotlyModule } from 'angular-plotly.js';
// We have to supply the plotly.js module to the Angular
// library.
PlotlyModule.plotlyjs = Plotly;


@NgModule({
  declarations: [
    AnalysisComponent,
  ],
  imports: [
    CommonModule,
    MatButtonModule,
    DragDropModule,
    PlotlyModule,
  ]
})
export class AnalysisModule { }
