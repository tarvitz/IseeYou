function CustomFileBrowser(field_name, url, type, win) {
    
    var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;
    
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

tinyMCE.init({
    height: 300,
    mode: 'textareas',
    imagemanager_contextmenu: false,
    force_p_newlines: false,
    forced_root_block : '',
    theme: 'advanced',
    force_br_newlines : true,
    file_browser_callback: 'CustomFileBrowser',
    relative_urls : false,
    convert_urls : false,
    remove_script_host : false,
    //content_css : "/appmedia/blog/style.css",
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_buttons1 : "fullscreen,separator,preview,separator,bold,italic,underline,strikethrough,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,link,unlink,anchor,separator,image,cleanup,help,separator,code,pasteword",
	theme_advanced_buttons2 : "",
	theme_advanced_buttons3 : "",
	auto_cleanup_word : true,
	plugins : "table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,searchreplace,print,contextmenu,fullscreen,paste,media,template",
	plugin_insertdate_dateFormat : "%m/%d/%Y",
	plugin_insertdate_timeFormat : "%H:%M:%S",
	extended_valid_elements : "a[class|name|href|target=_blank|title|\
	 onclick],img[class|src|border=0|alt|title|hspace|vspace|width|\
	 height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],\
	 font[face|size|color|style],span[class|align|style],script[language|type|src],\
         style[type|src]",
	fullscreen_settings : {
		theme_advanced_path_location : "top",
		theme_advanced_buttons1 : "fullscreen,separator,preview,separator,cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
		theme_advanced_buttons2 : "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor",
		theme_advanced_buttons3 : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print"
	}
});
