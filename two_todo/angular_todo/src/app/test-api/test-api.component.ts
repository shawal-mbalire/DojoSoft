import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-test-api',
  templateUrl: './test-api.component.html',
  styleUrls: ['./test-api.component.css']
})
export class TestAPIComponent {

  constructor(private http: HttpClient) { }

  obj:any;
  token:any;
  todos:any

  ngOnInit(): void {
    const url = 'http://127.0.0.1:8000/api/auth/';
    const body= {
      username: 'shawal',
      password: 'Namaganda.7',
    };
    this.obj = this.http.post(url,body).subscribe(data => {
      this.obj = data;
    });

    const url2 = 'http://127.0.0.1:8000/api/todos/';
    this.token = this.obj.token;
    const headers={'Authorization': 'Token ' + this.token}
    this.todos = this.http.get(url,{headers}).subscribe(data => {
      this.todos = data;
    });
  }

  


}
