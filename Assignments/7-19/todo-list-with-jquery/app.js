let taskNameTextbox = $("#task-item-textbox")

$(function() {
    taskNameTextbox.focus()
})


$( function() {
    $( "#pending-tasks-list-div" ).sortable();
    $( "#pending-tasks-list-div" ).disableSelection();
  } );

$( function() {
    $( "#completed-tasks-list-div" ).sortable();
    $( "#completed-tasks-list-div" ).disableSelection();
  } );

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

$(document).ready(() => {



    

    let pendingTasksListDiv = $("#pending-tasks-list-div")
    let completedTasksListDiv = $("#completed-tasks-list-div")

    taskNameTextbox.keypress((e) => {
        let keycode = (event.keyCode ? event.keyCode : event.which)
        if(keycode == '13') {
        // create div for list items
        let listItemDiv = $("<li>")
        console.log("item added.")
        let taskName = taskNameTextbox.val()
        taskNameTextbox.val("")
        


        // COMPLETE TASK
        let checkboxDiv = $("<div>")
        checkboxDiv.attr("class", "checkbox-div")

        // CUSTOM CHECKBOX
        // let checkboxRound = $("<div>")
        // checkboxRound.attr("class", "round")

        // checkboxDiv.append(checkboxRound)

        // let checkbox = $("<input>")
        // checkbox.attr("type", "checkbox")
        // let checkboxLabel = $("<label>")
        // checkboxLabel.attr("for", "checkbox")

        // checkboxRound.append(checkbox)
        // checkboxRound.append(checkboxLabel)

        
        // checkbox.attr("class", "checkbox")


        let checkbox = $("<input>")
        checkbox.attr("type", "checkbox")
        checkbox.attr("class", "checkbox")
        checkbox.click(() => {
            
            if (checkbox.is(':checked')) {
                // console.log("you are checking an item to complete it")
                completedTasksListDiv.append(checkbox.parent())
            } else if (checkbox.is(':not(:checked)')) {
                // console.log("you're unchecking this box")
                pendingTasksListDiv.append(checkbox.parent())
            }

            // completedTasksListDiv.append(listItemDiv)
            // if (this.checked == false) {
            // pendingTasksListDiv.append(listItemDiv)
            // }
        })

        let taskNameSpan = $("<text>")
        taskNameSpan.html(taskName)

        // REMOVE TASK ITEM
        let removeButton = $("<button>")
        removeButton.attr("id", "remove-task-button")
        removeButton.html("Remove")
        removeButton.click(() => {

        listItemDiv.remove()
        })


        listItemDiv.append(checkbox)
        listItemDiv.append(taskNameSpan)
        listItemDiv.append(removeButton)

        pendingTasksListDiv.append(listItemDiv)
        }
    })


//document ready closing tags
})

