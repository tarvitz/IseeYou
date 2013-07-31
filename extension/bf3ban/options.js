function save_options(){
    var username = document.getElementById("username").value;
    var api_key = document.getElementById("api_key").value;
    var server = document.getElementById("server").value;
    var local_storage = document.getElementById("local-storage");

    localStorage["bf3ban_username"] = username;
    localStorage["bf3ban_apikey"] = api_key;
    localStorage["bf3ban_server"] = server || "b3ban.blacklibrary.ru";
    //localStorage["bf3ban_local_storage"] = local_storage.checked;
    alert('saved');
}

function restore_options(){
    var username = localStorage['bf3ban_username'];
    var api_key = localStorage['bf3ban_apikey'];
    var server = localStorage['bf3ban_server'];

    var username_el = document.getElementById("username");
    var api_key_el = document.getElementById("api_key");
    var server_el = document.getElementById("server");
    var local_storage_el = document.getElementById("local-storage");

    if (username)
        username_el.value = username;
    if (api_key)
        api_key_el.value = api_key;
    if (server)
        server_el.value = server;
    /*
    local_storage_el.checked = localStorage['bf3ban_local_storage'] || false;
    if (local_storage_el.checked){
        options = document.querySelectorAll("form input[type=text]");
        for (var i = 0; i < options.length; i++){
            options[i].disabled = local_storage_el.checked;
        }
    }*/
}

function local_storage(e){
    el = e.target;
    options = document.querySelectorAll("form input[type=text]");
    for (var i = 0; i < options.length; i++){
        options[i].disabled = el.checked;
    }
}
document.addEventListener('DOMContentLoaded', restore_options);
document.querySelector("#save").addEventListener('click', save_options);
//document.querySelector("#local-storage").addEventListener('click', local_storage);

// jquery
$(document).ready(function(){
    $("#tabnav a").click(function(e){
        e.preventDefault();
        $(this).tab('show');
    });
});
