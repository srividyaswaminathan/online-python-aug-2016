function changBgColor() {
    var trs = document.getElementById("show").getElementsByTagName("tr");
        for(var i = 1; i< trs.length; i++) {
            if(i % 2 == 0) {
                trs[i].style.backgroundColor="#f5fafe";
            }
            else {
                trs[i].style.backgroundColor="white";
            }
        }
}
function deleteConfirm() {
    if (!confirm("Confirm Delete?")) {
        window.event.returnValue = false;
    }
}
