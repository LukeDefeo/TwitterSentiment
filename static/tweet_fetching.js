/**
 * Created with PyCharm.
 * User: Luke
 * Date: 26/08/2013
 * Time: 15:29
 * To change this template use File | Settings | File Templates.
 */
var running = false;
var firstRun = true;
var count = 0;
var posCount = 0;
var negCount = 0;
var current_query = "";
var sentCount = 0

function processInput() {
    console.log(current_query)
    console.log(firstRun)
    var search_query = $("#searchField").val();
    if (search_query == "") {
        return
    }
    showSearchResults();
    console.log("enter pressed");


    if (search_query != current_query) {
        if (firstRun) {
            firstRun = false
        } else {
            //clear list
            console.log("clear list");
            $("#posList").empty();
            $("#negList").empty();
            $("#objList").empty();
            $("#unsureList").empty();

            $('#posScore').html('');
            $('#negScore').html('');
            posCount = 0;
            negCount = 0;
            sentCount = 0;
            count = 0;


        }
        current_query = search_query
    }
    fetch_recursive()
}
function getTotalNoItems() {
    return $("#negList").length + $("#posList").length;
}


function writeToList(value, listID) {
    $(listID).append('<li class="list-group">' + value.text + '<li>');
    count++;

}

function recalculateScore() {
    var posScore = Math.round((100 * (posCount / sentCount))).toString();
    var negScore = Math.round((100 * (negCount / sentCount))).toString();
    $('#posScore').html(posScore + '%');
    $('#negScore').html(negScore + '%')


}

function fetch_recursive() {
    var len = count;
    var search_query = $("#searchField").val();
    console.log(len)
    if (len >= 50) {
        console.log("done");
        return
    }
    $.getJSON("/json", {q: search_query, start: len}, function (data) {
        console.log('Recieving JSON');
        $.each(data, function (key, value) {
            if (value.sentiment == "pos") {
                posCount++;
                sentCount++;
                writeToList(value, "#posList")
            } else if (value.sentiment == "neg") {
                negCount++;
                sentCount++;
                writeToList(value, "#negList")
            } else if (value.sentiment == "unsure") {
                writeToList(value, "#unsureList")
            } else if (value.contains_sentiment == false) {
                writeToList(value,'#objList')
            } else {
                console.log("cannot locate meaning.")
            }



        });
        recalculateScore();
        setTimeout(fetch_recursive, 5000);
    });
}

