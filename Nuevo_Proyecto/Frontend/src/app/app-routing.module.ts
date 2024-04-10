import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UnoComponent } from './uno/uno.component';

const routes: Routes = [
  { path: '', component: UnoComponent }, // Ruta para la página principal
  // Otras rutas aquí si las tienes
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }