function pick(obj, def){
    return (typeof obj == 'undefined') ? def : obj;
}

function xhr(dict){
    var method = pick(dict.method, "GET");
    var data = pick(dict.data, {});
    var reload = pick(dict.reload, false);

    var cache = null;
    chrome.extension.sendRequest({method: "getBF3BanServerCache"}, function(response){
        cache = response.cache;
        try{
            _cache = JSON.parse(cache);
        } catch (SystemError){
            cache = null;
        }

        if (! dict.url && dict.success){
            throw Error("Please provide 'url' and success'");
        }
        console.log('retrieve the list of banned servers');
        var _url = dict.url;
        var _server = dict.server || localStorage['bf3ban_server'] || "b3ban.blacklibrary.ru";
        var _username = dict.username || localStorage['bf3ban_username'] || "default";
        var api_key = dict.api_key || localStorage['bf3ban_apikey'] || 'default';
        _url  = (_url[_url.length-1] != '/') ? _url + '/' : _url;

        var url = "http://" + _server + "/" + _url + "?format=json&username="
            + _username + "&api_key=" + api_key;
        var success = dict.success;

        // do not retrieve the list
        if (!reload && cache){
            console.log('Servers GOT from cache');
            success(_cache);
            return false;
        }

        var request = new XMLHttpRequest();
        request.open(method, url);
        request.onreadystatechange = function(){
            if (request.readyState == 4 && request.status == 200){
                var type = request.getResponseHeader("Content-Type");
                // default it should be JSON
                try{
                    response = JSON.parse(request.responseText)
                    localStorage['bf3ban_servers_cache'] = request.responseText; //response;
                } catch (SyntaxError){
                    response = request.responseText;
                }
                success(response);
            }
        }; //onreadystatechange
        request.send((method == 'POST') ? data: null); //complete GET
    });//sendRequest
}


