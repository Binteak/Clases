import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UnoComponent } from './uno/uno.component'; // Asegúrate de importar el componente UnoComponent

@NgModule({
  declarations: [
    AppComponent,
    UnoComponent // Asegúrate de agregar el componente UnoComponent aquí
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }