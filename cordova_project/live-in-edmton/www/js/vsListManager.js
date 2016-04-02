/**
 * Created by Alvin on 2016-04-01.
 */
function VsListManager(apInstance,_vslistDiv,newqueryDiv,_mapInstance) {
    var vsListMangerInstance = this;
    this.currentData = [];
    this.vslistDiv = _vslistDiv;
    this.currentItem = null;
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
        template:'<li class="vsItem">'+
                '<a href="#" class="item-link item-content " style="background-color: black">'+
                '<div class="item-media"><img src="img/icons/ranks/rank{{filename}}.png" width="44"></div>'+
                    '<div class="item-inner">'+
                       '<div class="item-title-row">'+
                            '<div class="item-title">{{name}}</div>'+
                        '</div>'+
                        '<div class="item-subtitle">{{score}} Points</div>'+
                    '</div>'+
                '</a>'+
            '</li>'
    });

    this.updateList = function(data){
        console.log(data);
        vsListMangerInstance.currentData = data[0];
        vsListMangerInstance.currentData.push(data[0][1]);
        vsListMangerInstance.currentData.push(data[0][1]);
        vsListMangerInstance.currentData.push(data[0][1]);

        newqueryDiv.hide();
        for (var i = 0 ; i < vsListMangerInstance.currentData.length;i++){
            var nName;
            var randIndex;
            if (i<3){
                randIndex = i+1;
            }else{
                randIndex = "l";
            }
            for (nName in vsListMangerInstance.currentData[i]){
                vsListMangerInstance.myList.appendItem(
                    {
                        filename:randIndex,
                        score:vsListMangerInstance.currentData[i][nName]["attributes"][0].toString(),
                        index:i,
                        name: nName.toString()
                    }
                );
            }
        }

        $("li.vsItem").off('click');
        $( "li.vsItem" ).click(function() {
            console.log($("li").index($(this)));
            if (vsListMangerInstance.currentItem) {
                vsListMangerInstance.currentItem.children().css("background-color", "black");
            }
            $(this).children().css("background-color", "gray");
            vsListMangerInstance.currentItem =$(this);
            vsListMangerInstance.updateMap($("li").index($(this)));
        });

    };

    this.updateMap = function(index){
        vsListMangerInstance.mapInstance.moveToNei(vsListMangerInstance.currentData[index]);
    }
}