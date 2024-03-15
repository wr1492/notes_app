let display = document.getElementById('display');

function appendToDisplay(input){
    display.value += input;
}

function calculate() {
  try {
    display.value = eval(display.value);
  } catch (error) {
    display.value = 'Error';
  }
}

function clearDisplay() {
  display.value = '';
}

function showSidebar(){
    const sidebar = document.querySelector('.sidebar');
        sidebar.style.display = 'flex';
    }

function hideSidebar(){
    const sidebar = document.querySelector('.sidebar');
       sidebar.style.display = 'none';
    }

let response = document.getElementById('response')
function clearResponse() {
  response.innerHTML = '';
}

const textarea = document.getElementById("auto-resize");
textarea.addEventListener("keyup", function () {
  textAreaAdjust(this);
});

function show_calculator(){
    const calculator = document.querySelector('#calculator')
        calculator.style.display = "grid";
}

function hide_calculator(){
    const calculator = document.querySelector('#calculator')
        calculator.style.display = "none";
}

function show_todo(){
    const todo = document.querySelector('.todo')
        todo.style.display = "grid";
}

function hide_todo(){
    const todo = document.querySelector('.todo')
        todo.style.display = "none";
}

function add_item() {
        const itemDescription = document.getElementById('item_description').value;
        if (itemDescription.trim() === '') {
            alert('Please enter a task description.');
            return;
        }

        // Create a new list item
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <input type="checkbox" class="item_completed">
            ${itemDescription}
            <button class="calc_button" onclick="delete_item(this)">X</button>
        `;

        // Append the item to the list
        const todoList = document.getElementById('todo_list');
        todoList.appendChild(listItem);

        // Clear the input field
        document.getElementById('item_description').value = '';
    }

function delete_item(button) {
    const listItem = button.parentNode;
    listItem.remove();
}

function edit_note(data){
    let note = document.getElementById('note')
        note.innerHTML = data;
}
