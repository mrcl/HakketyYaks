$( document ).ready(function() {

    $.get( "/static/data/mindthegap.json", function( data ) {
        console.log( data );
    });

});