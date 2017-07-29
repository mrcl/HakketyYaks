$( document ).ready(function() {

    $('#goaldetail').hide();
    $.get( "/static/data/mindthegap.json", function( data ) {
        $.mindthegap.thegoals = data.Goals;
        $.mindthegap.loadgoals();
    });

});

$.mindthegap = {
    thegoals : [],
    loadgoals : function(){
        var stOut = '';
        for(var i=0;i<$.mindthegap.thegoals.length;i++){
            stOut += '<div class="col-md-4"><div class="goal"><sup>'+$.mindthegap.thegoals[i].Number+'</sup><h3>'+$.mindthegap.thegoals[i].Name+'</h3></div></div>';
        }
        $('#goals').html(stOut);
        $('.goal').click(function(){
            var numb = $(this).children('sup').html();
            $.mindthegap.goaldetail(numb);
        });
    },
    goaldetail : function(id){
        $('#goals').addClass('small');
        $('.col-md-4').removeClass('col-md-4').addClass('nav');
            
        var theGoal = {};
        for(var i=0;i<$.mindthegap.thegoals.length;i++){
            if($.mindthegap.thegoals[i].Number == id){
                theGoal = $.mindthegap.thegoals[i];
                break;
            }
        }
        
        
        var stOut = '<h2>'+theGoal.Name+'</h2>';

        $('#goaldetail').html(stOut);
        $('#goaldetail').fadeIn();
        //});
    }

}