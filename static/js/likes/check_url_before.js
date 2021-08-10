if(localStorage.getItem("url_anterior")){
    console.log("Hay una cosa pendiente")
    let url_anterior = localStorage.getItem("url_anterior");
    url_anterior.replace("/like/","");
    console.log(url_anterior.slice(6,url_anterior.length));
    
    location.href=url_anterior.slice(6,url_anterior.length)+"#like";
    
    localStorage.clear();
}
if(localStorage.getItem("post_for_comment")){
    console.log("Hay una cosa pendiente")
    let url_anterior = localStorage.getItem("post_for_comment");
    location.href=url_anterior+"#comment";
    
    localStorage.clear();
}