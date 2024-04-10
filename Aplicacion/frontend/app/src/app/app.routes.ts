import { Routes } from '@angular/router';
import { ComponenteUnoComponent } from './componenteuno/componenteuno.component';

export const routes: Routes = [
  { path: '', redirectTo: '/componenteuno', pathMatch: 'full' }, // Redirecciona a ComponenteUno por defecto
  { path: 'componenteuno', component: ComponenteUnoComponent },
  // Puedes agregar más rutas aquí si es necesario
  // Por ejemplo:
  // { path: 'otro-componente', component: OtroComponenteComponent },
];