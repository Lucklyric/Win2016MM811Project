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
            data :testdata,
            success: function (response) {
                //var par = JSON.parse(response);
               // console.log(par);
                view1Tab.trigger("click");
                view1Tab.trigger("click");

                listManager.updateList(response);
                queryManagerInstance.preloadIndi.hide();
            },
            error: function (xhr) {
                //Do Something to handle error
            }
        });
    }
}