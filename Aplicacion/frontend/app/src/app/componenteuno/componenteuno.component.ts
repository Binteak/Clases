import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-componenteuno',
  templateUrl: './componenteuno.component.html',
  styleUrls: ['./componenteuno.component.css']
})
export class ComponenteUnoComponent implements OnInit {
  data: any;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('http://localhost:8000/api/mi_ruta').subscribe(response => {
      this.data = response;
      console.log('JSON recibido desde el backend:', this.data);
    });
  }
}