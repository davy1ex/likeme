function make_like(user_id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/like_"+String(user_id), false ); // false for synchronous request
    console.log("succes")
    xmlHttp.send( null );
    
    // return xmlHttp.responseText;
}