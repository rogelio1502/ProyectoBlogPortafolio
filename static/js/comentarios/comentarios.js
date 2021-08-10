
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
            let fecha = new Date(data[i].time).toUTCString();
            let fecha_actual = Date.now()
            fecha_actual = new Date(fecha_actual).toUTCString();
            // console.log(data[i].id_comentario+"|"+data[i].user+"|"+new Date(data[i].time).toUTCString()+"|");
            // console.log(fecha_actual);
            // console.log(data[i].content)
            com_ajax.innerHTML += "<div class='comentarios'><h5>"+data[i].user.toUpperCase()+"</h5><p>"+data[i].content+"<br></p><p class='fecha'><small>"+fecha+"</small></p></div>"
            



        }
        document.getElementById("count_comentarios").innerHTML = '<i class="fas fa-comments ml-5"></i>' + data[data.length-1].count;


    }).error(function (data) {
        console.log("ERROR");
        console.log(data);
    }).complete(function(data){
        console.log("REQUEST COMPLETE.")
    })
}

