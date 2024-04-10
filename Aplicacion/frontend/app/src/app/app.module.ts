import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ComponenteUnoComponent } from './componenteuno/componenteuno.component';
import { AppRoutingModule } from './app-routing.module'; 

@NgModule({
  declarations: [
    ComponenteUnoComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule 
  ],
  providers: [],
  bootstrap: []
})
export class AppModule { }