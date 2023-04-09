import { Component } from '@angular/core';
import { Todo } from 'src/models/todo.model';
import { NgForm } from '@angular/forms'; 
import { Guid } from 'guid-typescript';

// TODO: npm install --save angualr-webstorage-service

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'angular_todo';
  uncomplete_todos:number=0; 
  complete_todos:number=0; 
  percentage:number=100*this.complete_todos/(this.complete_todos+this.uncomplete_todos)

  todos: Todo[]=[] //empty todo list

  onSubmit(form: NgForm) {
    let todo = new Todo(
      Guid.create(), 
      form.value.title, 
      form.value.todo_desc, 
      false, 
      false
    );
    this.todos.unshift(todo);
    this.uncomplete_todos ++;
    form.resetForm();
  }

  onDelete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    let index = this.todos.indexOf(todo, 0);
    if (todo.isComplete){
      this.complete_todos --;
    }
    if (!todo.isComplete){
      this.uncomplete_todos --;
    }
    if (index > -1) {
      this.todos.splice(index, 1);
    }
  }

  onComplete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    todo.isComplete = true;
    this.uncomplete_todos --;
    this.complete_todos ++;
  }

  unComplete(id: Guid) {
    let todo = this.todos.filter(x => x.id === id)[0];
    todo.isComplete = false;
  }
}

