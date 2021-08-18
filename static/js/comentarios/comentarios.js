//const music = new Audio('/holamundo.wav');
setInterval(checkComentarios, 1000)
actualizarComentarios();
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
    }).complete(function (data) {
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
                
                //music.play();
                document.getElementById('audio_send').volume=0.5;

                document.getElementById('audio_send').play();

                
                

            } getComentarios()
        }).error(function (data) {
            console.log("ERROR");
            console.log(data);
        }).complete(function (data) {
            console.log("REQUEST COMPLETE.")
            //music.play();
        })
    } else {
        getComentarios();
    }

}

const getTimeAgo = (postDate) => {
    let fecha = new Date(postDate)
    let fecha_actual = Date.now()


    let new_fecha = new Date(fecha_actual)
    let diferencia = (new_fecha - fecha) / 1000 / 60
    // console.log(Math.ceil(diferencia));
    if (Math.ceil(diferencia) <= 1) {
        fecha = "Just now"
    }
    if (diferencia > 1 && diferencia < 60) {
        fecha = Math.round(diferencia) + " minutes ago";
    } else if (Math.round(Math.ceil(diferencia) / 60) == 1) {
        fecha = "1 hour ago";

    } else if (diferencia > 60 && diferencia < (60 * 24)) {
        fecha = Math.round(Math.ceil(diferencia) / 60) + " hours ago";

    } else if (diferencia > (60 * 24)) {
        fecha = Math.round(Math.ceil(diferencia) / (60 * 24)) + " days ago";

    }
    return fecha;
};


function actualizarComentarios() {

    $.ajax({
        url: "/" + document.getElementById("title").dataset.url + "/",
        type: 'GET',
        dataType: 'json',
        cache: false

    }).done(function (data) {
        
        var com_ajax = document.getElementById("comentariosbyajax");
        com_ajax.innerHTML="";
        com_ajax.innerHTML = "";
        document.getElementById("count_comentarios").innerHTML = "";
        // console.log(data.length)
        for (let i = 0; i < data.length - 1; i++) {

            console.log(data[i].visto)
            com_ajax.innerHTML += "<div  class='comentarios' ><h5>" + data[i].user.toUpperCase() + "</h5><p id='comentario' data-id='" + data[i].id_comentario + "'>" + data[i].content + "<br></p></div>"

            // if (data[i].visto===false){
            //    com_ajax.innerHTML += "<div  class='comentarios nuevo' ><h5>"+data[i].user.toUpperCase()+"</h5><p id='comentario' data-id='"+data[i].id_comentario+"'>"+data[i].content+"<br></p></div>"


            // }
            // else{
            // com_ajax.innerHTML += "<div  class='comentarios'  ><h5>"+data[i].user.toUpperCase()+"</h5><p id='comentario' data-id='"+data[i].id_comentario+"'>"+data[i].content+"<br></p></div>"

            // }
            com_ajax.innerHTML += "<p class='fecha'><small id='comentario" + data[i].id_comentario + "'>"+getTimeAgo(data[i].time)+"</small></p>"
            setInterval(() => {
                document.getElementById("comentario" + data[i].id_comentario).innerHTML = getTimeAgo(data[i].time);
            }, 1000);


        }
        document.getElementById("count_comentarios").innerHTML = '<i class="fas fa-comments ml-5"></i>' + data[data.length - 1].count;


    }).error(function (data) {
        console.log("ERROR");
        console.log(data);
    }).complete(function (data) {
        console.log("REQUEST COMPLETE.")
    })
}


$('#formulario').on('submit', function (e) {
    e.preventDefault();
    console.log($(this).serialize());
    console.log($(this).attr('action'));
    let url = $(this).attr('action');
    $.ajax({url: url, type: "POST", data: $(this).serialize(), dataType: 'json'}).done(function (data) {
        // console.log(data);
        document.getElementById("formulario").reset();
        actualizarComentarios();
        document.getElementById('audio_send').volume=0.5;

        document.getElementById('audio_send').play();

    }).error(function (data) {
        console.log("ERROR");
        console.log(data);
    }).complete(function (data) {
        console.log("REQUEST COMPLETE.")
    })

});
