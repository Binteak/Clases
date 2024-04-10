import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ComponenteUnoComponent } from './componenteuno/componenteuno.component';

const routes: Routes = [
  { path: '', component: ComponenteUnoComponent }, // Definimos que ComponenteUnoComponent se muestre en la ruta raíz
  // Puedes agregar más rutas aquí según sea necesario
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }