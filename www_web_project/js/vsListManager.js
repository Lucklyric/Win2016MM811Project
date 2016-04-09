/**
 * Created by Alvin on 2016-04-01.
 */
function VsListManager(apInstance,_vslistDiv,newqueryDiv,_mapInstance) {
    var vsListMangerInstance = this;
    this.currentData = [];
    this.vslistDiv = _vslistDiv;
    this.currentItem = null;
    this.currentItemData = null;
    this.mapInstance = _mapInstance;
    this.myList = apInstance.virtualList(this.vslistDiv,{
        items:[

        ],
        // Template 7 template to render each item
        //template: '<li class="item-content">' +
        //'<div class="item-media">Name:</div>' +
        //'<div class="item-inner">' +
        //'<div class="item-title">{{title}}</div>' +
        //'</div>' +
        //'</li>'
        //template:'<li class="vsItem" onclick="itemClick()">'+
        //        '<a href="#" class="item-link item-content " style="background-color: black">'+
        //        '<div class="item-media"><img src="img/icons/ranks/rank{{filename}}.png" width="44"></div>'+
        //            '<div class="item-inner">'+
        //               '<div class="item-title-row">'+
        //                    '<div class="item-title">{{name}}</div>'+
        //                '</div>'+
        //                '<div class="item-subtitle">{{score}} Points</div>'+
        //            '</div>'+
        //        '</a>'+
        //    '</li>'

        renderItem: function (index, item) {
            return'<li class="vsItem" id="'+index+'">'+
                    '<a href="#" class="item-link item-content " style="background-color: black">'+
                    '<div class="item-media"><img src="img/icons/ranks/rank'+item.filename+'.png" width="44"></div>'+
                        '<div class="item-inner">'+
                           '<div class="item-title-row">'+
                                '<div class="item-title">'+item.name+'</div>'+
                            '</div>'+
                            '<div class="item-subtitle">'+item.score+' Points</div>'+
                        '</div>'+
                    '</a>'+
                '</li>'
        }
    });

    this.updateList = function(data){
        console.log(data);
        vsListMangerInstance.currentData = data;
        newqueryDiv.hide();
        vsListMangerInstance.myList.deleteAllItems();
        for (var i = 0 ; i < vsListMangerInstance.currentData.length;i++){
            var nName =  vsListMangerInstance.currentData[i]["name"];
            var randIndex;
            if (i<3){
                randIndex = i+1;
            }else{
                randIndex = "l";
            }
                vsListMangerInstance.myList.appendItem(
                    {
                        filename:randIndex,
                        score:vsListMangerInstance.currentData[i]["score"].toFixed(0).toString(),
                        index:i,
                        name: nName.toString()
                    }
                );
        }

        //$(".vsItem").click(function(){
        //    console.log(this);
        ////});
        //$("li.vsItem").off('click');
        //$( "li.vsItem" ).click(function() {
        //
        //    if (vsListMangerInstance.currentItem) {
        //        vsListMangerInstance.currentItem.children().css("background-color", "black");
        //    }
        //    $(this).children().css("background-color", "gray");
        //    vsListMangerInstance.currentItem =$(this);
        //    vsListMangerInstance.updateMap($("li").index($(this)));
        //});
        this.clickedItem = function(item){
            console.log("click"+item.id);

            if (vsListMangerInstance.currentItem) {
                        vsListMangerInstance.currentItem.children().css("background-color", "black");
                    }
            $(item).children().css("background-color", "gray");
            vsListMangerInstance.currentItem =$(item);
            vsListMangerInstance.currentItemData = vsListMangerInstance.currentData[item.id];
            vsListMangerInstance.updateMap(item.id);
        };

    };


    this.updateMap = function(index){
        vsListMangerInstance.mapInstance.moveToNei(vsListMangerInstance.currentData[index]);
    };

    $(document).on('click', 'li.vsItem', function(){
        vsListMangerInstance.clickedItem(this);
    });
}
