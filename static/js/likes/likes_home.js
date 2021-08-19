


function dar_like(slug){
    $.ajax(
        {
            url:slug,
            type:"get",
            cache: false

        }).done(function(response){
             //console.log(response[0]["post"])
                
               
                //console.log(likes.classList)
            // if()
            console.log(response[0]["activo"]);
            if(response[0]["activo"]!=="False"){
                console.log("Hola");
                console.log(response[0]["likes"]);
                let likes = document.getElementById(response[0]["post"]);
                try{
                    document.getElementById("conteo").innerHTML=" "+response[0]["likes"]+" "

                }catch{
                    
                }
                console.log(likes);
                likes.innerHTML=" "+response[0]["likes"]+" ";
                
            }
            else{
                //set url anterior de un like
                localStorage.setItem("url_anterior",slug)

                console.log(slug);
                location.href="http://"+location.host+"/accounts/login/";
                
                
            }
            
            

        }).error(function(error){
            console.log(error)
            //console.log(slug);
        }).complete(function(response){
            console.log("REQUEST COMPLETE")
            
        })
            
            
               
           
    
}





let like = document.getElementsByClassName("like");

for(const l of like ){

    console.log(l.dataset);
    
    l.addEventListener("click",
    function(){
        dar_like(l.dataset.url);
    })
}
