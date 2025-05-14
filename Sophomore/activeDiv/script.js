var isActiveList;

if(!localStorage.getItem("activeList")) {
    
    isActiveList = [false, false, false, false, false, false, false, false];
    
} else {
    
    isActiveList = JSON.parse(localStorage.getItem("activeList"));
    
}

$(".highlight").click(active);

function active() {
    
    var index = parseInt(this.innerHTML);
    
    isActiveList[index] = !isActiveList[index];
    
    if(isActiveList[index]) {
        
        $(this).css("backgroundColor", "lightblue");
        
    } else {
        
        $(this).css("backgroundColor", "");
        
    }
    
    localStorage.setItem("activeList", JSON.stringify(isActiveList));
    
}

for(var i = 0; i < isActiveList.length; i++) {
    
    if(isActiveList[i]) {
        
        $(".highlight").eq(i).css("backgroundColor", "lightblue")
        
    }
    
}
