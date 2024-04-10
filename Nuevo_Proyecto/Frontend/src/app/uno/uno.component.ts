import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-uno', // Selector del componente
  templateUrl: './uno.component.html', // Ruta al archivo HTML del componente
  styleUrls: ['./uno.component.css'] // Ruta al archivo CSS del componente (opcional)
})

export class UnoComponent implements OnInit{

  constructor() { }

  ngOnInit(): void {
    // Código que se ejecuta cuando el componente se inicializa
  }

  // Otros métodos y propiedades del componente pueden ir aquí

}
