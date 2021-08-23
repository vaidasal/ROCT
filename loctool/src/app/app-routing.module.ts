import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './modules/user/register/register.component';
import { LoginComponent } from './components/login/login.component';
import { SecureComponent } from './components/secure/secure.component';
import { AuthGuard } from './auth.guard';
import { NotFoundComponent } from './components/not-found/not-found.component';

const routes: Routes = [
  { path: '', redirectTo: 'home/loct/data', pathMatch: 'full' },
  { path: 'secure', canActivate: [ AuthGuard ], component: SecureComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: '404', component: NotFoundComponent },
  { path: 'home', loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule) },
  { path: 'modules/settings', loadChildren: () => import('./modules/settings/settings.module').then(m => m.SettingsModule) },
  { path: 'modules/loct', loadChildren: () => import('./modules/loct/loct.module').then(m => m.LoctModule) },
  { path: 'modules/dataentry', loadChildren: () => import('./modules/loct/dataentry/dataentry.module').then(m => m.DataentryModule) },
  { path: '**', redirectTo: '404' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
