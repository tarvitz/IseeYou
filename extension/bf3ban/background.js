// non-modified settings
var normalColor = {color: [80, 80, 80, 255]};
var cleanColor = {color: [200, 20, 20, 255]};

/* event listener */
chrome.extension.onRequest.addListener(function(request, sender, sendResponse){
    switch(request.method){
        case "getBF3BanSettings":
            data = {
                username: localStorage['bf3ban_username'],
                api_key: localStorage['bf3ban_apikey'],
                server: localStorage['bf3ban_server'],
            };
            sendResponse({data: data});
            break;
        case "setBF3BanCount":
            if (request.count > 0){
                chrome.browserAction.setBadgeBackgroundColor(normalColor);
                chrome.browserAction.setBadgeText({text: request.count+''});
            } else {
                pluginIcon = 'img/icon.png'
                chrome.browserAction.setIcon({path: pluginIcon});
                chrome.browserAction.setBadgeBackgroundColor(cleanColor);
                chrome.browserAction.setBadgeText({text:''}); //drop text
            }
            break;
        case "dropBF3BanServerCache":
            delete localStorage['bf3ban_servers_cache'];
            break;
        case "getBF3BanServerCache":
            cache = localStorage['bf3ban_servers_cache'];
            sendResponse({cache: localStorage['bf3ban_servers_cache']});
            break;
        default:
            sendResponse({});
    }
});
