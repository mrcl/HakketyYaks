var marginStacked = {top: 20, right: 20, bottom: 30, left: 40},
    width = 800 - marginStacked.left - marginStacked.right,
    height = 650 - marginStacked.top - marginStacked.bottom;


$( document ).ready(function() {

    $('#goaldetail').hide();
    $.get( "/static/data/mindthegap/mindthegap.json", function( data ) {
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
        
        var stOut = '<h2>'+theGoal.Number+': '+theGoal.Name+'</h2><p class="text-uppercase small">Annual Expenditure Figures (000s)</p> <div id="chart"></div>';

        if(theGoal.References){
            stOut += '<div class="ref"><h2>Referenced Datasets</h2><ul>'
            if(theGoal.References.length > 0){
                for(var m = 0;m < theGoal.References.length; m++){
                    stOut += '<li><a href="'+theGoal.References[m].URL+'">'+theGoal.References[m].Title+'</a>';
                    if(theGoal.References[m].Contribution && theGoal.References[m].Contribution.length > 0)stOut += ' (' + theGoal.References[m].Contribution + ')</li>';
                }
            }else{
                stOut += '<li>No found expenditure datasets, if you know of data that exists, <a href="mailto:HakketyYaks@gmail.com">please let us know</a>.</li>';
            }
            stOut += '</ul></div>';
        }
        
        $('#goaldetail').html(stOut);
        $('#goaldetail').fadeIn();
        $('#goaldetail').append($.mindthegap.rendergraph(theGoal));
        $('.goal').mouseleave();

        //});
    },
    rendergraph : function(theGoal){
        var svg = d3.select("#chart").append("svg")
        .attr("preserveAspectRatio", "xMinYMin meet")
        .attr("viewBox", "0 0 " + (width + marginStacked.left + marginStacked.right) + " " + (height + marginStacked.top + marginStacked.bottom) );
            //.attr("width", width + marginStacked.left + marginStacked.right)
            //.attr("height", height + marginStacked.top + marginStacked.bottom);

        
        g = svg.append("g").attr("transform", "translate(" + marginStacked.left + "," + marginStacked.top + ")");

        var x = d3.scaleBand()
            .rangeRound([0, width-140])
            .paddingInner(0.05)
            .align(0.1);

        var y = d3.scaleLinear()
            .rangeRound([height, 0]);

        var z = d3.scaleOrdinal()
            .range([ "#6b486b", "#a05d56", "#d0743c", "#EAEAEA","#EAEAEA", "#8a89a6", "#7b6888"]);

        d3.csv("/static/data/mindthegap/"+theGoal.Number+".csv", function(d, i, columns) {
            for (i = 1, t = 0; i < columns.length; ++i) t += d[columns[i]] = +d[columns[i]];
            d.total = t;
            return d;
        }, function(error, data) {
            if (error) throw error;

            var keys = data.columns.slice(1);

            //data.sort(function(a, b) { return b.total - a.total; });
            x.domain(data.map(function(d) { return d.Gap; }));
            y.domain([0, d3.max(data, function(d) { return d.total; })]).nice();
            z.domain(keys);

            g.append("g")
                .selectAll("g")
                .data(d3.stack().keys(keys)(data))
                .enter().append("g")
                .attr("fill", function(d) { return z(d.key); })
                .selectAll("rect")
                .data(function(d) { return d; })
                .enter().append("rect")
                .attr("x", function(d) { return x(d.data.Gap); })
                .attr("y", function(d) { return y(d[1]); })
                .attr("height", function(d) { return y(d[0]) - y(d[1]); })
                .attr("width", x.bandwidth());

            g.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            g.append("g")
                .attr("class", "axis")
                .call(d3.axisLeft(y).ticks(null, "s"))
                .append("text")
                .attr("x", 2)
                .attr("y", y(y.ticks().pop()) + 0.5)
                .attr("dy", "0.32em")
                .attr("fill", "#000")
                .attr("font-weight", "bold")
                .attr("text-anchor", "start")
                .text("$");

            var legend = g.append("g")
                .attr("font-family", "sans-serif")
                .attr("font-size", 10)
                .attr("text-anchor", "end")
                .selectAll("g")
                .data(keys.slice().reverse())
                .enter().append("g")
                .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

            legend.append("rect")
                .attr("x", width - 19)
                .attr("width", 19)
                .attr("height", 19)
                .attr("fill", z);

            legend.append("text")
                .attr("x", width - 24)
                .attr("y", 9.5)
                .attr("dy", "0.32em")
                .text(function(d) { return d; });
        });
            
        
    }

};

