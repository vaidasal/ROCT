import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoctComponent } from './loct.component';

const routes: Routes = [{ path: '', component: LoctComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoctRoutingModule { }
