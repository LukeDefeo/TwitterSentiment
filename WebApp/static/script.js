/**
 * Created with PyCharm.
 * User: Luke
 * Date: 25/07/2013
 * Time: 11:55
 * To change this template use File | Settings | File Templates.
 */

function go() {
    $.getJSON('search', function (returned) {
        $.each(returned, function (k, v) {
            $("ul").append("<li>" + v.first + "<li>")

        })
    })
}

$("#searchField").keyup(function(event){
    var textFieldValue = $.("#seachField").value();
    if(event.keyCode == 13){
        go(textFieldValue)
    }
});

