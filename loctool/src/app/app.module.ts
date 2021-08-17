import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatToolbarModule, MatToolbarRow} from '@angular/material/toolbar'; 

import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {AuthInterceptor} from './services/auth.interceptor';
import { SecureComponent } from './components/secure/secure.component';
import { NotFoundComponent } from './components/not-found/not-found.component';

import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatSortModule} from '@angular/material/sort';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatTableModule} from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './modules/user/register/register.component';
import {MatRadioModule} from '@angular/material/radio';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatMenuModule} from '@angular/material/menu';
import { HomeModule } from './modules/home/home.module';
import {MatProgressBarModule} from '@angular/material/progress-bar';

@NgModule({
  declarations: [
    AppComponent,
    SecureComponent,
    NotFoundComponent,
    LoginComponent,
    RegisterComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatProgressSpinnerModule,
    MatSortModule,
    MatTableModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatRadioModule,
    MatSidenavModule,
    MatMenuModule,
    HomeModule,
    MatSortModule,
    MatPaginatorModule,
    MatProgressBarModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
