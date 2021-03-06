window.user_markers = [];
window.current_latlng = null;
window.new_tweet_num = 0;
$(document).ready(function () {
    //Blue - neutral
    gradient1 = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 225, 255, 1)',
    'rgba(0, 200, 255, 1)',
    'rgba(0, 175, 255, 1)',
    'rgba(0, 160, 255, 1)',
    'rgba(0, 145, 223, 1)',
    'rgba(0, 125, 191, 1)',
    'rgba(0, 110, 255, 1)',
    'rgba(0, 100, 255, 1)',
    'rgba(0, 75, 255, 1)',
    'rgba(0, 50, 255, 1)',
    'rgba(0, 25, 255, 1)',
    'rgba(0, 0, 255, 1)'
  ]
    // Red - negative
    gradient2 = [
        'rgba(255, 255, 0, 0)',
        'rgba(255, 255, 0, 1)',
        'rgba(255, 225, 0, 1)',
        'rgba(255, 200, 0, 1)',
        'rgba(255, 175, 0, 1)',
        'rgba(255, 160, 0, 1)',
        'rgba(255, 145, 0, 1)',
        'rgba(255, 125, 0, 1)',
        'rgba(255, 110, 0, 1)',
        'rgba(255, 100, 0, 1)',
        'rgba(255, 75, 0, 1)',
        'rgba(255, 50, 0, 1)',
        'rgba(255, 25, 0, 1)',
        'rgba(255, 0, 0, 1)'
      ]
    
    // Green - positive
    gradient3 = [
        'rgba(150, 200, 100, 0)',
        'rgba(140, 200, 90, 1)',
        'rgba(130, 200, 80, 1)',
        'rgba(120, 200, 70, 1)',
        'rgba(110, 200, 60, 1)',
        'rgba(100, 200, 50, 1)',
        'rgba(90, 200, 40, 1)',
        'rgba(80, 200, 30, 1)',
        'rgba(70, 200, 20, 1)',
        'rgba(60, 200, 10, 1)',
        'rgba(50, 200, 0, 1)'
      ]
    $("#new_tweet_num").text(0);
    <!-- To get New Notifications-->
    $.fn.poll_request = function(){
        var ajaxCall = $.ajax({
            url: "/poll_data/",
            type: "post",
            data: {
                "csrfmiddlewaretoken" : $("[name='csrfmiddlewaretoken']").val()
            },
            success: function(response){
                var new_tweets = response.new_tweets;
                $("#new_tweet_num").text(parseInt($("#new_tweet_num").text())+new_tweets.length);
            },
            error: function(error){
            },
            complete: function(){
                $.fn.poll_request();
            }
        });
    };
    setTimeout($.fn.poll_request, 100);


    $("#search_tweets_button").click(function () {
        $("#loading_modal").modal("show");
        $("#new_tweet_num").text(0);
        $.ajax({
            url: "/search_query/",
            type: "POST",
            data: {
                selected_keyword: $("#keyword_select").val(),
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            },
            success: function (response) {
                //Resetting required fields
                $("#geo_query").prop("disabled",true);
                $("#distance").val("");
                $("#distance").prop("disabled",true);
                window.current_latlng = null;
                $("#selected_lat").text("N/A");
                $("#selected_lon").text("N/A");
                // Using custom PIN when user clicks on MAP
                var user_pinColor = "6600cc";
                var user_pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + user_pinColor,
                        new google.maps.Size(21, 34),
                        new google.maps.Point(0, 0),
                        new google.maps.Point(10, 34));
                var sanFrancisco = new google.maps.LatLng(35, 0);
                var map = new google.maps.Map(document.getElementById('map'), {
                  center: sanFrancisco,
                  zoom: 2,
                  mapTypeId: 'terrain'
                });

                // User Click Event
                google.maps.event.addListener(map, 'click', function (e) {
                    $("#distance").prop("disabled", false);
                    $("#geo_query").prop("disabled", false);
                    window.current_latlng = e;
                    for (var j = 0; j < window.user_markers.length; j++) {
                        window.user_markers[j].setMap(null);
                    }
                    $("#selected_lat").text(e.latLng.lat());
                    $("#selected_lon").text(e.latLng.lng());
                    marker = new google.maps.Marker({
                        position: e.latLng,
                        title: "U",
                        icon: user_pinImage,
                        map: map
                    });
                    window.user_markers.push(marker);
                });

                // Mapping the sentiments
                
                var locations = response.tweet_coordinates;

                $("#num_results").text(response.num_records);
                $("#num_results_div").show();
                $("#results_div").show();
                mapData (map, locations);
                $("#pos_results_div").show();
                $("#neg_results_div").show();
                $("#neut_results_div").show();

            },
            error: function(response) {
                console.log("Error");
            },
            complete: function () {
                $("#loading_modal").modal("hide");
            }
        });
    });

function mapData (map, locations) {
    var heatmapData1 = [];
    var heatmapData2 = [];
    var heatmapData3 = [];
    var i; 
    var posCount = 0;
    var negCount = 0;
    var neutCount = 0;
    for (i = 0; i < locations.length; i++) {
        var iconImage;
        var latLng = new google.maps.LatLng(parseInt(locations[i][1]), parseInt(locations[i][2]));
        if(locations[i][3]=="positive"){
            posCount++;
            heatmapData3.push(latLng);
        }else if(locations[i][3]=="negative"){
            negCount++;
            heatmapData2.push(latLng);
        }else if(locations[i][3]=="neutral"){
            neutCount++;
            heatmapData1.push(latLng);
        }
        
        $("#pos_results").text(posCount);
        $("#neg_results").text(negCount);
        $("#neut_results").text(neutCount);
        
        pointArray1 = new google.maps.MVCArray(heatmapData1);
        pointArray2 = new google.maps.MVCArray(heatmapData2);
        pointArray3 = new google.maps.MVCArray(heatmapData3);
        heatmap1 = new google.maps.visualization.HeatmapLayer({
          data: pointArray1});
        heatmap2 = new google.maps.visualization.HeatmapLayer({
          data: pointArray2});
        heatmap3 = new google.maps.visualization.HeatmapLayer({
          data: pointArray3});
        heatmap1.setMap(map); 
        heatmap2.setMap(map);
        heatmap3.setMap(map); 
        heatmap1.set('gradient', gradient1);  
        heatmap2.set('gradient', gradient2);
        heatmap3.set('gradient', gradient3);
    }
}

    $("#geo_query").click(function () {
        if ($("#distance").val() == "") {
            alert("Please enter a distance!");
        } else {
            $("#loading_modal").modal("show");
            $("#new_tweet_num").text(0);
            $.ajax({
                url: "/geo_query/",
                type: "POST",
                data: {
                    selected_keyword: $("#keyword_select").val(),
                    distance: $("#distance").val(),
                    lat: window.current_latlng.latLng.lat(),
                    lng: window.current_latlng.latLng.lng(),
                    csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
                },
                success: function (response) {
                    //Resetting required fields
                    $("#geo_query").prop("disabled",true);
                    $("#distance").val("");
                    $("#distance").prop("disabled",true);
                    window.current_latlng = null;
                    $("#selected_lat").text("N/A");
                    $("#selected_lon").text("N/A");
                    
                    var user_pinColor = "6600cc";
                    var user_pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + user_pinColor,
                            new google.maps.Size(21, 34),
                            new google.maps.Point(0, 0),
                            new google.maps.Point(10, 34));
                    var sanFrancisco = new google.maps.LatLng(35, 0);
                    var map = new google.maps.Map(document.getElementById('map'), {
                      center: sanFrancisco,
                      zoom: 2,
                      mapTypeId: 'terrain'
                    });

                    // User Click Event
                    google.maps.event.addListener(map, 'click', function (e) {
                        $("#distance").prop("disabled", false);
                        $("#geo_query").prop("disabled", false);
                        window.current_latlng = e;
                        for (var j = 0; j < window.user_markers.length; j++) {
                            window.user_markers[j].setMap(null);
                        }
                        $("#selected_lat").text(e.latLng.lat());
                        $("#selected_lon").text(e.latLng.lng());
                        marker = new google.maps.Marker({
                            position: e.latLng,
                            title: "U",
                            icon: user_pinImage,
                            map: map
                        });
                        window.user_markers.push(marker);
                    });

                    var locations = response.tweet_coordinates;
                    $("#num_results").text(response.num_records);
                    $("#num_results_div").show();
                    $("#results_div").show();
                    mapData (map, locations)

                },
                error: function(response) {
                  console.log("ERROR");
                },
                complete: function () {
                    $("#loading_modal").modal("hide");
                }
            });
        }
    });
});