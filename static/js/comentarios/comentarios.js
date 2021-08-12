
actualizarComentarios()



function getComentarios() {

    $.ajax({
        url: "/" + document.getElementById("title").dataset.url + "/",
        type: 'GET',
        dataType: 'json', // solucion para que no muestre el jsonResponse el navegador
        cache: false

    }).done(function (data) {


        comentarios = data;


    }).error(function (data) {
        console.log("ERROR");
        // console.log("Al obtener datos")
        console.log(data);
    }).complete(function(data){
        console.log("REQUEST COMPLETE.")
    })

    
}
var comentarios;
function checkComentarios() {

    // console.log(comentarios)
    // console.log("DONe")
    
    let csrftoken = getCookie('csrftoken');
    if (comentarios !== undefined) {
        $.ajax({
            url: "/" + document.getElementById("title").dataset.url + "/",
            type: 'POST',
            data: {
                comentarios: comentarios,
                csrfmiddlewaretoken: csrftoken
            },
            dataType: 'json',
            cache: false

        }).done(function (data) {


            // console.log(data);
            // console.log(comentarios)
            if (data[0].id_comentario === comentarios[0].id_comentario) {
                // console.log("Son iguales");
                // console.log(comentarios)
                // console.log(data)

                // console.log("DONe")
            } else {
                console.log("Actualizando comentarios");
                actualizarComentarios()

            } getComentarios()
        }).error(function (data) {
            console.log("ERROR");
            console.log(data);
        }).complete(function(data){
            console.log("REQUEST COMPLETE.")
        })
    } else {
        getComentarios();
    }

}


function actualizarComentarios() {

    $.ajax({
        url: "/" + document.getElementById("title").dataset.url + "/",
        type: 'GET',
        dataType: 'json',
        cache: false

    }).done(function (data) {
        var com_ajax =document.getElementById("comentariosbyajax");
        com_ajax.innerHTML = "";
        document.getElementById("count_comentarios").innerHTML = "";
        //console.log(data.length)
        for (let i = 0; i < data.length - 1; i++) {
            let fecha = new Date(data[i].time)
            let recien = 0;
            let fecha_actual = Date.now()
            

            let new_fecha = new Date(fecha_actual)
            let diferencia = (new_fecha-fecha)/1000/60
            console.log(Math.ceil(diferencia));
            if (Math.ceil(diferencia)<=1){
                fecha = "Just now"
            }
            if (diferencia>1 && diferencia<60){
                fecha = Math.round(diferencia)+" minutes ago";
            }else if(Math.round(Math.ceil(diferencia)/60)==1){
                fecha = "1 hour ago";

            }else if(diferencia>60 && diferencia<(60*24)){
                fecha = Math.round(Math.ceil(diferencia)/60)+" hours ago";

            }
            
            
            //fecha = new Date(data[i].time).toUTCString();
            
            //fecha_actual = new Date(fecha_actual).toUTCString();

            //console.log(fecha)
            // console.log(data[i].id_comentario+"|"+data[i].user+"|"+new Date(data[i].time).toUTCString()+"|");
            // console.log(fecha_actual);
            // console.log(data[i].content)
            if (Math.ceil(diferencia)<=1){
                com_ajax.innerHTML += "<div class='comentarios nuevo'><h5>"+data[i].user.toUpperCase()+"</h5><p>"+data[i].content+"<br></p><p class='fecha'><small>"+fecha+"</small></p></div>"

            }else{
                com_ajax.innerHTML += "<div class='comentarios'><h5>"+data[i].user.toUpperCase()+"</h5><p>"+data[i].content+"<br></p><p class='fecha'><small>"+fecha+"</small></p></div>"

            }

            



        }
        document.getElementById("count_comentarios").innerHTML = '<i class="fas fa-comments ml-5"></i>' + data[data.length-1].count;


    }).error(function (data) {
        console.log("ERROR");
        console.log(data);
    }).complete(function(data){
        console.log("REQUEST COMPLETE.")
    })
}

