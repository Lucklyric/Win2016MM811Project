/**
 * Created by Alvin on 2016-04-01.
 */
function QueryManager(preloadIndiDiv,listManager,view1Tab){
    var queryManagerInstance = this;
    this.preloadIndi= preloadIndiDiv;
    this.hostpath = "http://localhost:8081";

    this.fakeQuery = function(testdata){
        this.preloadIndi.show();
        $.ajax({
            url: this.hostpath+"/fakequery/",
            type: "post", //send it through get method
            dataType:"json",
            data :{
                string:testdata
            },
            success: function (response) {
                if (response == "3"){
                    console.log("App service has been closed");
                }else {
                    //console.log(response);
                    var par = JSON.parse(response);
                    //console.log(par);
                    view1Tab.trigger("click");
                    view1Tab.trigger("click");

                    listManager.updateList(par);
                    queryManagerInstance.preloadIndi.hide();
                }
            },
            error: function (xhr) {
                //Do Something to handle error
            }
        });
    }
}