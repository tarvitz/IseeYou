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
    var settings = {};

    function check_ip(ip_addr){
        ip_addresses = [];
        for (var i = 0; i < settings.servers.objects.length; i++){
            obj = settings.servers.objects[i];
            ip_addresses.push(obj.ip_address);
        }
        return ( ip_addresses.indexOf(ip_addr) != -1 );
    };
    
    var clone = function(src){
        var dst = new src.constructor();
        for (el in src) dst[el] = src[el];
        return dst;
    }

    return {
        get settings(){
            return settings;
        },
        set settings(dict){
            for (el in dict) settings[el] = dict[el];
            return settings;

        },
        getServers: function(callback){
            username = this.settings.username;
            server = this.settings.server;
            api_key = this.settings.api_key;
            var $this = this;

            xhr({
                url: 'api/v1/server',
                username: username,
                server: server,
                api_key: api_key,
                success: function(response){
                    $this.settings.servers = response;
                    if (callback) callback.call($this, response);
                }
            });
        },
        init: function(){
            var $this = this;
            console.log('BF3Block init');
            chrome.extension.sendRequest({method: "getBF3BanSettings"}, function(response){
                for (el in response.data){
                    if (el) $this.settings[el] = response.data[el];
                }
                $this.settings = response.data;
                $this.block();
            });
            return this;
        },
        block: function(){
            if (this.settings.servers){
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
                }
            } else {
                $this = this;
                this.getServers(this.block);
                //this.getServers(function(){
                //    $this.block();
                //});
            }
        }
    } //return
}());

window.onload = function(){
    bf3block = BF3Block;
    bf3block.init();
    server_list = document.querySelector("#serverguide-listcontainer");
    content = document.querySelector("#content");
    document.addEventListener("DOMSubtreeModified", function(e){
        if (e.target == server_list || e.target == content && e.target.tagName != 'SURF:CONTAINER'){
            console.log("server list modified, fire blockage");
            bf3block.block();
        } else if (e.target.tagName == "SURF:CONTAINER"){
            update_server_block(e.target);
        }
    });
}

