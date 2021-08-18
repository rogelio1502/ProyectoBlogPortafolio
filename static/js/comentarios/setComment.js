/*window.document.onmouseout=function () {
    $.ajax({
        url: "/comentarios/" + document.getElementById("comentario").dataset.id + "/",
        type: 'GET',
        dataType: 'json', // solucion para que no muestre el jsonResponse el navegador
        cache: false
    
    }).done(function (data) {
    
    
        actualizarComentarios();
        
    
    
    }).error(function (data) {
        console.log("ERROR");
        // console.log("Al obtener datos")
        console.log(data);
    }).complete(function(data){
        console.log("REQUEST COMPLETE.")
    })
    
}
*/