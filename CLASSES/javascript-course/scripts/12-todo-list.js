const todoList = [{
    name:'make dinner',
    dueDate: '2022-12-22'},{
    name: 'wash dishes',
    dueDate: '2022-12-22'}];


renderTodoList();

function renderTodoList(){
  let todoListHTML='';

  // .forEach Method is BEST PRACTICE; "easier to read"
  todoList.forEach((todoObject, index) =>{
    const{ name, dueDate} =todoObject;
    const html = `<div>${name}</div>
                  <div>${dueDate}</div>
                  <button class=
                  "delete-todo-button js-delete-todo-button">Delete</button>
                    `;
    todoListHTML += html;
  });
  document.querySelector('.js-todo-list').innerHTML=todoListHTML;

  // KEY CONCEPT: for each delete button on the page 
  // we add a click event listener ; 
  // objects with same class act as ARRAY
  document.querySelectorAll('.js-delete-todo-button')
  .forEach((deleteButton, index) => {
    deleteButton.addEventListener('click',()=>{
      todoList.splice(index,1);
      renderTodoList();
    })
  });

  
} //renderTodoList

document.querySelector('.js-add-todo-button')
  .addEventListener('click', () => {  
    addTodo()}
);

function addTodo(){
  const inputElement=document.querySelector('.js-name-input');
  const name=inputElement.value;
  
  const dateInputElement=document.querySelector('.js-due-date-input');
  const dueDate=dateInputElement.value;

  todoList.push({
    //name: name,
    //dueDate: dueDate
    // lines ^ replace by below [OBJECT SHORTHAND]
    name,
    dueDate
  });

  console.log(todoList);

  inputElement.value=" ";
  renderTodoList();
}