import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeComponent } from './me/me.component';
import { UserComponent } from './user.component';

const routes: Routes = [{ path: '', component: UserComponent}, { path: 'me', component: MeComponent}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
