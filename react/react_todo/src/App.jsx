import "./App.css"
import React from 'react'

function App(){
  const [newItem, setNewItem] = React.useState({})
  const [todos, setTodos] = React.useState([])

  function handleSubmit(e){
    e.preventDefault()
    setTodos(currentTodos => {
      return [
        ...currentTodos,
        {id:crypto.randomUUID(), title: newItem,completed: false}
      ]
    })
    setNewItem('')
  }

  function toggleToDo(id,completed){
    setTodos(currentTodos => {
      return currentTodos.map(todo => {
        if(todo.id === id){
          return {...todo, completed: completed}
        }
        return todo
      })
    })
  }

  function deleteToDo(id){
    setTodos(currentTodos => {
      return currentTodos.filter(todo => {
        return todo.id !== id
      })
    })
  }


  return (
  <>
  <form className="new-item-form" onSubmit={handleSubmit}>
    <div className="form-row">
      <label htmlFor="New Todo Title">Title</label>
      <input type="text" name="title" placeholder="Title" value={newItem.title} onChange={e => setNewItem(e.target.value)} />
    </div>
    <button className="btn">Add</button>
  </form>

  <h1 className="header">Todo List</h1>


  <ul className="list">
    {todos.length === 0 && <li className="list-item">No Todos</li>/}
    {todos.map(todo => {
      return (
        <li key={todo.id}>
          <label htmlFor="">
            <input type="checkbox" checked={todo.completed} onChange={E=>toggleToDo(todo.id,e.target.checked)}/>
            {todo.title}
          </label>
          <button className="btn btn-danger" onClick={()=>deleteToDo(todo.id)}>Delete</button>
        </li>
      )
    })}
  </ul>


  </>
  )
}

export default App
