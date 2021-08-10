

setInterval(checkComentarios,5000)



$('#formulario').on('submit',function(e){
    e.preventDefault();
    console.log($(this).serialize());
    console.log($(this).attr('action'));
    let url = $(this).attr('action');
    $.ajax(
        {
            url:url,
            type:"POST",
            data:$(this).serialize(),
            dataType:'json'

        }
    ).done(
        function(data){
            //console.log(data);
            actualizarComentarios();
            document.getElementById("formulario").reset();

        }
    ).error(function (data) {
        console.log("ERROR");
        console.log(data);
    }
    ).complete(function(data){
        console.log("REQUEST COMPLETE.")
    })
    
});