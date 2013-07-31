function update_server_block(container){
    // updates information about taken serverguide container
    if (!container.querySelector('.server-cell-ip-address') &&
        container.querySelector('.serverguide-bodycells')){
        info_blk = container.querySelector(".serverguide-cell-name-server-info");
        ip_blk = container.querySelector(".serverguide-bodycells");

        ip = ip_blk.getAttribute('ip');
        ip_el = document.createElement('span');
        ip_el.setAttribute('class', 'server-cell-ip-address');
        ip_el.innerText = "• ip: " + ip;
        info_blk.appendChild(ip_el);
    }
}

BF3Block = (function(){
    function getServers(cb){
        username = BF3Block.settings.username;
        server = BF3Block.settings.server;
        api_key = BF3Block.settings.api_key;
        xhr({
            url: 'api/v1/server',
            username: username,
            server: server,
            api_key: api_key,
            success: function(response){
                BF3Block.settings.servers = response;
                if (cb) cb();
            }
        });
    };
    function check_ip(ip_addr){
        ip_addresses = [];
        for (var i = 0; i < BF3Block.settings.servers.objects.length; i++){
            obj = BF3Block.settings.servers.objects[i];
            ip_addresses.push(obj.ip_address);
        }

        return ( ip_addresses.indexOf(ip_addr) != -1 );
    };

    return {
        settings: {},
        init: function(dt){
            console.log('BF3Block init');
            chrome.extension.sendRequest({method: "getBF3BanSettings"}, function(response){
                for (el in response.data){
                    if (el) BF3Block.settings[el] = response.data[el];
                }
                BF3Block.settings = response.data;
                BF3Block.block();
            });
        },
        block: function(){
            getServers(function(){
                if (BF3Block.settings.servers){
                    server_list = document.querySelector("#serverguide-listcontainer");
                    if (server_list){
                        for (var i = 0; i < server_list.children.length; i++){
                            blk = server_list.children[i];
                            if (blk.tagName == 'SURF:CONTAINER' &&
                                    ! blk.getAttribute('data-processed')){
                                ip = blk.children[1].getAttribute('ip');
                                state = check_ip(ip);
                                if (state){
                                    blk.setAttribute('class', 'block');
                                }
                                //altering server-item dom, adding useful links and elements
                                blk.setAttribute('data-processed', 'true');
                                update_server_block(blk);
                                // set checked state for further ignorance
                            }//if blk.name
                        }//
                        block_count = document.querySelectorAll("#serverguide-listcontainer .block").length;
                        chrome.extension.sendRequest({method: "setBF3BanCount", count: block_count}, function(response){
                            //pass
                        });
                    }// if server_list
                }
            });
        }
    } //return
}());

window.onload = function(){
    BF3Block.init();

    //BF3Block.block();
    server_list = document.querySelector("#serverguide-listcontainer");
    content = document.querySelector("#content");
    document.addEventListener("DOMSubtreeModified", function(e){
        if (e.target == server_list || e.target == content && e.target.tagName != 'SURF:CONTAINER'){
            console.log("server list modified, fire blockage");
            BF3Block.block();
        } else if (e.target.tagName == "SURF:CONTAINER"){
            update_server_block(e.target);
        }
    });
}
//document.addEventListener("DOMContentLoaded", block);

