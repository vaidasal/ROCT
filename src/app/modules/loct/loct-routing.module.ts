import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoctComponent } from './loct.component';

const routes: Routes = [{ path: '', component: LoctComponent, children: [
  {path: 'entry', loadChildren: () => import('./dataentry/dataentry.module').then(m => m.DataentryModule)},
  {path: 'data', loadChildren: () => import('../../modules/loct/data/data.module').then(m => m.DataModule)}
] }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoctRoutingModule { }
