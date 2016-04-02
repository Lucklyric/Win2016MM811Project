// Initialize app and store it to myApp variable for futher access to its methods
var myApp = new Framework7({material:true});
var myQuery,myVsList;
// We need to use custom DOM library, let's save it to $$ variable:
var $$ = Dom7;

// Add view
var mainView = myApp.addView('.view-main', {
    // Because we want to use dynamic navbar, we need to enable it for this view:

});

// Now we need to run the code that will be executed only for About page.


// Option 2. Using one 'pageInit' event handler for all pages:
$$(document).on('pageInit', function (e) {
    // Get page data from event data
    var page = e.detail.page;

    if (page.name === 'index') {
        // Following code will be executed for page with data-page attribute equal to "about"
        myApp.alert('Here comes About page');
}
});

// Option 2. Using live 'pageInit' event handlers for each page
$$(document).on('pageInit', '.page[data-page="about"]', function (e) {
    // Following code will be executed for page with data-page attribute equal to "about"
    myApp.alert('Here comes About page');
});


$(document).ready(function(){
    $.ajaxSetup({ cache: false });
    myVsList = new VsListManager(myApp,$("#vsList"),$("#newQueryDiv"));
    myQuery = new QueryManager($("#preload"),myVsList,$$("#view1Tab"));

    $$("#jumpButton").click(function(){
        console.log("click");
        $$("#view2Tab").trigger("click");
        $$("#view2Tab").trigger("click");
    });

    /**
     * query button function
     */
    $("#fakequery").click(function(){
        var fakedata = {
            admin : 11,
            pwd:"this"
        };
        myQuery.fakeQuery(fakedata);
    });


});
