<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import VueProgressBar from 'vue-progressbar'
//import * as Vue from 'vue'

const todos = ref([])
const name  = ref('')

const input_content  = ref('')
const input_category = ref(null) //null by default but changes later

const todos_asc = computed(() => todos.value.sort((a,b) =>{//return the ascending list of todos
	return b.createdAt - a.createdAt
}))

watch(name, (newVal) => { //editing new value and saving to local storage
	localStorage.setItem('name', newVal)
})

watch(todos, (newVal) => { // saving todos to localStorage
	localStorage.setItem('todos', JSON.stringify(newVal))
}, {
	deep: true
})

const addTodo = () => {
	if (input_content.value.trim() === '' || input_category.value === null) {
		return
	}

	todos.value.push({
		content: input_content.value,
		category: input_category.value,
		done: false,
		editable: false,
		createdAt: new Date().getTime()
	})
}

const removeTodo = (todo) => {
	todos.value = todos.value.filter((t) => t !== todo)
}

onMounted(() => {//getting name from local storage
	name.value = localStorage.getItem('name') || ''
	todos.value = JSON.parse(localStorage.getItem('todos')) || []
})

//checking how many todos are done
const doneTodos = computed(() => {
  return todos.value.filter((todo) => todo.done).length
})
//adding progress bar to check how many todos are done
const options = {
  color: '#bffaf3',
  failedColor: '#874b4b',
  thickness: '5px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 300
  },
  autoRevert: true,
  location: 'top',
  inverse: false
}
//Vue.use(VueProgressBar, options)
//VueProgressBar.config(options)
//VueProgressBar.start()


const progress = computed(() => {
  return ((doneTodos.value / todos.value.length) * 100) || 0
})
console.log(progress.value)


</script>

<template>
	<main class="app">
    <div class="progress-bar">
         <VueProgressBar :options="options" :progress="progress" />
    </div>
		
		<section class="greeting">
			<h2 class="title">
				What's up, <input type="text" id="name" placeholder="Name here" v-model="name">
			</h2>
		</section>

		<section class="create-todo">
			<h3>CREATE A TODO</h3>

			<form id="new-todo-form" @submit.prevent="addTodo">
				<h4>What's on your todo list?</h4>
				<input 
					type="text" 
					name="content" 
					id="content" 
					placeholder="Enter your todo here "
					v-model="input_content" />
				
				<h4>Pick a category</h4>
				<div class="options">

					<label>
						<input 
							type="radio" 
							name="category" 
							id="category1" 
							value="school"
							v-model="input_category" />
						<span class="bubble business"></span>
						<div>School</div>
					</label>

					<label>
						<input 
							type="radio" 
							name="category" 
							id="category2" 
							value="personal"
							v-model="input_category" />
						<span class="bubble personal"></span>
						<div>Personal</div>
					</label>

				</div>

				<input type="submit" value="Add todo" />
			</form>
		</section>

		<section class="todo-list">
			<h3>TODO LIST</h3>
			<div class="list" id="todo-list">

				<div v-for="todo in todos_asc" :class="`todo-item ${todo.done && 'done'}`">
					<label>
						<input type="checkbox" v-model="todo.done" />
						<span :class="`bubble ${
							todo.category == 'school' 
							  ? 'school' 
								: 'personal'
						}`"></span>
					</label>

					<div class="todo-content">
						<input type="text" v-model="todo.content" />
					</div>

					<div class="actions">
						<button class="delete" @click="removeTodo(todo)">Delete</button>
					</div>
				</div>

			</div>
		</section>

	</main>
</template>
