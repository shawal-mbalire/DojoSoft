import { Component } from '@angular/core';
import { Todo } from 'src/models/todo.model';
import { NgForm } from '@angular/forms';
import { Guid } from 'guid-typescript';

// TODO: npm install --save angualr-webstorage-service

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})

export class AppComponent {
  title = 'angular_todo';
  uncomplete_todos: number = 0;
  complete_todos: number = 0;
  percentage = 100*this.complete_todos / (this.complete_todos+this.uncomplete_todos);


  todos: Todo[] = [] //empty todo list
  // get item from local storage and parse it to JSONe
  // todos_json = JSON.parse(localStorage.getItem('todos'));
  // percentage_json = JSON.parse(localStorage.getItem('percentage'));

  // constructor() {
  //   // if there is no item in local storage, set it to empty array
  //   // else set it to the item in local storage
  //   if (this.todos_json == null) {
  //     localStorage.setItem('todos', JSON.stringify({ data: [] }));
  //   } else {
  //     this.todos = this.todos_json.data;
  //   }

    if (this.percentage_json == null) {
      localStorage.setItem('percentage', JSON.stringify(0));
    } else {
      this.percentage = this.percentage_json;
    }
  }



  onSubmit(form: NgForm) {
    let todo = new Todo(
      Guid.create(),
      form.value.title,
      form.value.todo_desc,
      false,
      false
    );
    this.todos.unshift(todo);
    this.uncomplete_todos++;
    this.percentage = 100*this.complete_todos / (this.complete_todos+this.uncomplete_todos);
    form.resetForm();

    let data = { data: this.todos }
    localStorage.setItem('percentage', JSON.stringify(this.percentage));
    localStorage.setItem('percentage', JSON.stringify(this.percentage));
    localStorage.setItem('todos', JSON.stringify(data));
    //console.log(this.todos_json)
  }

  onDelete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    let index = this.todos.indexOf(todo, 0);
    if (todo.isComplete) {
      this.complete_todos--;
    }
    if (!todo.isComplete) {
      this.uncomplete_todos--;
    }
    if (index > -1) {
      this.todos.splice(index, 1);
    }

    let data = { data: this.todos }
    localStorage.setItem('todos', JSON.stringify(data));

    this.percentage = 100*this.complete_todos / (this.complete_todos+this.uncomplete_todos);
    localStorage.setItem('percentage', JSON.stringify(this.percentage));
  }

  onComplete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    todo.isComplete = true;
    this.uncomplete_todos--;
    this.complete_todos++;

    this.percentage = 100*this.complete_todos / (this.complete_todos+this.uncomplete_todos);
    localStorage.setItem('percentage', JSON.stringify(this.percentage));
  }

  unComplete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    todo.isComplete = false;
    this.uncomplete_todos++;
    this.complete_todos--;

    this.percentage = 100*this.complete_todos / (this.complete_todos+this.uncomplete_todos);
    localStorage.setItem('percentage', JSON.stringify(this.percentage));
  }

}

