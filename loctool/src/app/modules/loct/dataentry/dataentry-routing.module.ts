import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DataentryComponent } from './dataentry.component';

const routes: Routes = [{ path: '', component: DataentryComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DataentryRoutingModule { }
