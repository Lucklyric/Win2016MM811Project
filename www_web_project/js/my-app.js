// Initialize app and store it to myApp variable for futher access to its methods
var myApp = new Framework7({material:true});
// Set all instances
var myQuery,myVsList,myMapManager,myTableManager,myTableManager_back;
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

// Ready functions
$(document).ready(function(){
    // initilize all the instances
    $.ajaxSetup({ cache: false });
    myMapManager = new MapManager();
    myMapManager.initialize();
    myVsList = new VsListManager(myApp,$("#vsList"),$("#newQueryDiv"),myMapManager);
    myQuery = new QueryManager($("#preload"),myVsList,$$("#view1Tab"));
    myTableManager = new TableManager("container",myVsList,$("#detailButton"),$("#detail_Title"),1);
    myTableManager_back = new TableManager("container_back",myVsList,$("#detailButton"),$("#detail_Title"),2);

    // Init the table manager
    myTableManager.initTable();
    myTableManager_back.initTable();
    $$("#jumpButton").click(function(){
        console.log("click");
        $$("#view2Tab").trigger("click");
        $$("#view2Tab").trigger("click");
    });




    /**
     * query button function
     */
    $("#fakequery").click(function(){

        // Format the query options based on the user query options
        var queryArray=[];
        queryArray.push(parseInt($('input[name="play"]:checked').val()));
        queryArray.push(parseInt($('input[name="pSchool"]:checked').val()));
        queryArray.push(parseInt($('input[name="cSchool"]:checked').val()));

        //structure
        var radios = document.getElementsByName('struct');

        for (var i = 0, length = radios.length; i < length; i++) {

                if (i == 0){
                    if (radios[i].checked) {
                        queryArray.push(0);
                        queryArray.push(0);
                        queryArray.push(0);
                        queryArray.push(0);
                        queryArray.push(0);
                        queryArray.push(0);
                        break;
                    }
                }else{
                    if  (radios[i].checked){
                        queryArray.push(1);
                    }else{
                        queryArray.push(0)
                    }
                }

        }
        radios = document.getElementsByName('age');

        for (var i = 0, length = radios.length; i < length; i++) {

            if (i == 0){
                if (radios[i].checked) {
                    queryArray.push(0);
                    queryArray.push(0);
                    queryArray.push(0);
                    queryArray.push(0);
                    break;
                }
            }else{
                if  (radios[i].checked){
                    queryArray.push(1);
                }else{
                    queryArray.push(0)
                }
            }

        }
        var radios = document.getElementsByName('emp');

        for (var i = 0, length = radios.length; i < length; i++) {
            if (i == 0){
                if (radios[i].checked) {
                    queryArray.push(0);
                    queryArray.push(0);
                    queryArray.push(0);
                    break;
                }
            }else{
                if  (radios[i].checked){
                    queryArray.push(1);
                }else{
                    queryArray.push(0)
                }
            }
        }

        var queryString = "";
        for (var i = 0;i<queryArray.length;i++){
            if (i != (queryArray.length-1)){
                queryString+= queryArray[i].toString()+","
            }else{
                queryString+= queryArray[i].toString()
            }

        }
        console.log(queryString);
        // Send query request
        myQuery.fakeQuery(queryString);
    });

    /**
     * custom raido functions
     */

    $(".custom-radio").change(function(){
        var otherRadios = document.getElementsByName(this.name);

        if ($(this).val()==0){
            for (var i = 1, length = otherRadios.length; i < length; i++) {
                $(otherRadios[i]).prop('checked', false);
            }
        }else{
           $(otherRadios[0]).prop('checked', false);
        }
    });

});
