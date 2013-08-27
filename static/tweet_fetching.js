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
    var posScore = Math.round((100 * (posCount / count))).toString();
    var negScore = Math.round((100 * (negCount / count))).toString();
    $('#posScore').html(posScore + '%');
    $('#negScore').html(negScore + '%')


}

function fetch_recursive() {
    var len = count;
    var search_query = $("#searchField").val();
    console.log(len)
    if (len > 20) {
        console.log("done");
        return
    }
    $.getJSON("/json", {q: search_query, start: len}, function (data) {
        console.log('Recieving JSON');
        $.each(data, function (key, value) {
            if (value.sentiment == "pos") {
                posCount++;
                writeToList(value, "#posList")
            } else if (value.sentiment == "neg") {
                negCount++;
                writeToList(value, "#negList")
            }
        });
        recalculateScore();
        setTimeout(fetch_recursive, 5000);
    });
}

