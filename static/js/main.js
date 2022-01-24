
function push_command(command){

    let data = { line: command, output: "" }

    post_request(URL_COMMAND, data);

}

function remove_bot(){

    delete_request(URL_API_BOT, function (argument) {

        window.location.replace("/");

    });

}

function get_output(){

    get_request(URL_COMMAND, function(data){

        if (!jQuery.isEmptyObject(data)){

            let output = data["output"]; 

            if (output.localeCompare("exit") == 0) {

                setTimeout(remove_bot, TIME_BEFORE_DELETE_BOT);

            } else {

                $('#output').html(output);

            }

        }

    });

}


$("#sendcmd-btn").click(function(){

    let command = $("#command").val();

    if (command.localeCompare("exit") == 0){

        $("#sendcmd-btn").prop('disabled', true);

    }

    push_command(command);

});


$(document).ready(function(){

    setInterval(get_output, TIME_REFRESH);

});
