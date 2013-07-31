function popup(dt){
    reload = pick(dt.reload, false);
        settings = {
            username: localStorage['bf3ban_username'],
            server: localStorage['bf3ban_server'],
            api_key: localStorage['bf3ban_apikey'],
        }
        xhr({url: 'api/v1/server',
            reload: reload,
            success: function(response){
                if (response){
                    var ban_list = document.getElementById('banlist');
                    ban_list.innerHTML = "";
                    out = '<table class="table striped">' +
                        "<tr><th>IP address</th><th>Server name</th><th>Reason</th>";
                    for (var i = 0; i < response.objects.length; i++){
                        var obj = response.objects[i];
                        out += sprintf("<tr><td>%s</td><td>%s</td><td>%s</td></tr>", obj.ip_address,
                            obj.server_name || '-', obj.reason);
                    }
                    out += "</table>";
                    ban_list.innerHTML = out;
                    //write servers in cache
                    response_plain = JSON.stringify(response);
                    localStorage['bf3ban_servers_cache'] = response_plain;
                } // if response
            }// end success
        }); //xhr
}

function init(dt){
    //links
    var options_link = document.getElementById('options-link');
    options_link.onclick = function(){
        chrome.tabs.create({url: "options.html"});
    }
    document.getElementById('reload-cache-link').onclick = function(){
        popup({reload: true});
    };
    /* assign links */
    links = document.querySelectorAll("div.link");
    for (var i = 0; i<links.length; i++){
        link = links[i];
        href = link.getAttribute('data-href');
        if (href){
            link.onclick = function(e){
                chrome.tabs.create({url: href});
            }
        }
    }
    popup(dt);
    /* knockout */
    function BanListModel(){
        var self = this;
        self.title = "0.0.1";
        self.arr = ['1', '2', '3', '4'];
    };
    ko.applyBindings(new BanListModel());

}

document.addEventListener('DOMContentLoaded', init);
