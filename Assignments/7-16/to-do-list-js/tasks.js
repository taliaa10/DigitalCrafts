var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}


let taskNameTextbox = document.getElementById("task-item-textbox")
let enterTaskButton = document.getElementById("enter-task-button")

let pendingTasksListDiv = document.getElementById("pending-tasks-list-div")
let completedTasksListDiv = document.getElementById("completed-tasks-list-div")

enterTaskButton.addEventListener('click', () => {
    
    // create div for list items
    let listItemDiv = document.createElement("li")
    console.log("item added.")
    let taskName = taskNameTextbox.value

    // COMPLETE TASK
    let checkbox = document.createElement("input")
    checkbox.setAttribute("type", "checkbox")
    checkbox.setAttribute("class", "checkbox")
    checkbox.addEventListener("click", () => {

        completedTasksListDiv.appendChild(listItemDiv)
        if (this.checked == false) {
        pendingTasksListDiv.appendChild(listItemDiv)
        }
    })

    let taskNameSpan = document.createElement("span")
    taskNameSpan.innerHTML = taskName


    // REMOVE TASK ITEM
    let removeButton = document.createElement("button")
    removeButton.setAttribute("id", "remove-task-button")
    removeButton.innerHTML = "Remove"
    removeButton.addEventListener("click", () => {

        listItemDiv.remove()
    })

    listItemDiv.appendChild(checkbox)
    listItemDiv.appendChild(taskNameSpan)
    listItemDiv.appendChild(removeButton)

    pendingTasksListDiv.appendChild(listItemDiv)

})