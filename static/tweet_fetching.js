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
var current_query = "";

function processInput() {
    console.log("enter pressed")
    var search_query = $("#searchField").val();

    if (search_query == "") {
        return
    }

    if (search_query != current_query) {
        if (firstRun) {
            firstRun = false
        } else {
            //clear list
            console.log("clear list");
            $("#posList").empty();
            $("#negList").empty();
            current_query = search_query
        }
    }
    fetch_recursive()
}
function getTotalNoItems() {
    return $("#negList").length + $("#posList").length;
}


function writeToList(value, listID) {
    $(listID).prepend("<li>" + value.text + "<li>")
}

function fetch_recursive() {
    var len = getTotalNoItems();
    var search_query = $("#searchField").val();

    if (len > 20) {
        console.log("done");
        return
    }
    $.getJSON("/json", {q: search_query, start: len}, function (data) {
        console.log('Recieving JSON');
        $.each(data, function (key, value) {
            if (value.sentiment == "pos") {
                writeToList(value, "#posList")
            } else if (value.sentiment == "neg") {
                writeToList(value, "#negList")
            }
        });
        setTimeout(fetch_recursive, 5000);
    });
}

