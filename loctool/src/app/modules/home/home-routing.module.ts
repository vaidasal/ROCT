import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home.component';

const routes: Routes = [
  { path: '', component: HomeComponent,
  children: [
    {path: 'user', loadChildren: () => import('../../modules/user/user.module').then(m => m.UserModule)},
    {path: 'user/me', loadChildren: () => import('../../modules/user/user.module').then(m => m.UserModule)},
    {path: 'settings', loadChildren: () => import('../../modules/settings/settings.module').then(m => m.SettingsModule)},
    {path: 'loct', loadChildren: () => import('../../modules/loct/loct.module').then(m => m.LoctModule)},
  ]
}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }
