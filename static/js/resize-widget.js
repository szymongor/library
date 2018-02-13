document.addEventListener('DOMContentLoaded', function(){
    setTimeout(function() {
        resize()
    }, 100);
}, false);


function resize(){
    var categories_to = document.getElementById("id_categories_to");
    var height = categories_to.offsetHeight;
    el = categories_to;
    if(categories_to){
        categories_to.style.height = (height+45)+'px';
    }
}
