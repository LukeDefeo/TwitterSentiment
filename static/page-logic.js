/**
 * Created with PyCharm.
 * User: Luke
 * Date: 26/08/2013
 * Time: 21:43
 * To change this template use File | Settings | File Templates.
 */

var Pages = {
    searchResultsContainer : '#searchResultsContainer',
        contactMessage : '#contactMessage',
        aboutMessage : '#aboutMessage',
        welcomeMessage : '#welcomeMessage'
};
var Navigation = {
    navSearch : '#navSearch',
    navAbout : '#navAbout',
    navContact : '#navContact'
};


var current_page = Pages.welcomeMessage;
var current_nav = Navigation.navSearch;


function showSearchResults() {
    console.log('showing about page');
    showContent(Pages.searchResultsContainer);
    changeNavBar(Navigation.navSearch)
}

function showWelcome() {
    showContent(Pages.welcomeMessage);
    changeNavBar(Navigation.navSearch);
}

function showAbout() {
    showContent(Pages.aboutMessage);
    changeNavBar(Navigation.navAbout);

}

function showContact() {
    showContent(Pages.contactMessage);
    changeNavBar(Navigation.navContact);
}


function showContent(newPage) {
    console.log(current_page)
    $(current_page).addClass('hide');
    $(newPage).removeClass('hide');
    current_page = newPage
}


function changeNavBar(newPage) {
    console.log(current_nav)
    if(current_nav != newPage) {
        $(newPage).addClass('active');
        $(current_nav).removeClass('active');
        current_nav = newPage
    }

}