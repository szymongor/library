document.addEventListener('DOMContentLoaded', function(){
    addPassButton();
}, false);

function addPassButton() {
    var submit_row = document.getElementsByClassName("submit-row")[0];
    if(submit_row){
        let prevUrl = getPevUrl(window.location.pathname);
        let passBtn = document.createElement("p");
        passBtn.classList.add("deletelink-box");
        style = "background-color: orange;margin-left: 10px;"

        let a = document.createElement("a");
        a.href=prevUrl;
        a.classList.add("deletelink");
        a.setAttribute("style", style);
        a.innerHTML = "Anuluj zmiany"
        a.name = "_pass";
        passBtn.appendChild(a);
        submit_row.appendChild(passBtn);
    }

}

function getPevUrl(url){
    let splitedURL = url.split('/');
    let prevUrl = '/'+splitedURL[1]+'/'+splitedURL[2]
    return prevUrl;
}