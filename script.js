
function addHealthyPerson() {
    var input = document.getElementById("healthy-input");
    var person = input.value;
    var healthyList = document.getElementById("healthy-list");
    var listItem = document.createElement("li");
    listItem.textContent = person;
    healthyList.appendChild(listItem);
    input.value = "";
}

function deleteHealthyPerson() {
    var input = document.getElementById("healthy-delete-input");
    var nameToDelete = input.value;

    // Get the list of healthy people
    var healthyList = document.getElementById('healthy-list');
    var listItems = healthyList.getElementsByTagName('li');

    // Loop through the list items to find the name to delete
    for (var i = 0; i < listItems.length; i++) {
        var listItem = listItems[i];
        if (listItem.textContent === nameToDelete) {
            // Remove the found item from the list
            healthyList.removeChild(listItem);
            break; // Stop the loop after the first match is deleted
        }
    }

    // Clear the input field
    input.value = "";
}

function addUnhealthyPerson() {
    var input = document.getElementById("unhealthy-input");
    var person = input.value;
    var healthyList = document.getElementById("unhealthy-list");
    var listItem = document.createElement("li");
    listItem.textContent = person;
    healthyList.appendChild(listItem);
    input.value = "";
}
function deleteUnhealthyPerson() {
    var input = document.getElementById("unhealthy-delete-input");
    var nameToDelete = input.value;

    // Get the list of healthy people
    var unhealthyList = document.getElementById('unhealthy-list');
    var listItems = unhealthyList.getElementsByTagName('li');

    // Loop through the list items to find the name to delete
    for (var i = 0; i < listItems.length; i++) {
        var listItem = listItems[i];
        if (listItem.textContent === nameToDelete) {
            // Remove the found item from the list
            unhealthyList.removeChild(listItem);
            break; // Stop the loop after the first match is deleted
        }
    }

    // Clear the input field
    input.value = "";
}

document.getElementById("addHealthyPerson").addEventListener("click", addHealthyPerson);
document.getElementById("deleteHealthyPerson").addEventListener("click", deleteHealthyPerson);
document.getElementById("deleteHealthyPerson").addEventListener("click", addUnhealthyPerson);
document.getElementById("deleteHealthyPerson").addEventListener("click", deleteUnhealthyPerson);
