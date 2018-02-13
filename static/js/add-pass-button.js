document.addEventListener('DOMContentLoaded', function(){
    setTimeout(function() {
        addPassButton();
    }, 100);
}, false);

function addPassButton() {
    var submit_row = document.getElementsByClassName("submit-row")[0];
    if(submit_row){
        var button = document.createElement("input");
        var text = "Nie zapisuj";
        button.value = text;
        button.type = "submit";
        button.name = "_pass";
        submit_row.appendChild(button);
    }

}
