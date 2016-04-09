/**
 * Created by Alvin on 2016-04-02.
 */
Highcharts.createElement('link', {
    href: '//fonts.googleapis.com/css?family=Unica+One',
    rel: 'stylesheet',
    type: 'text/css'
}, null, document.getElementsByTagName('head')[0]);

Highcharts.theme = {
    colors: ["#2b908f", "#90ee7e", "#f45b5b", "#7798BF", "#aaeeee", "#ff0066", "#eeaaee",
        "#55BF3B", "#DF5353", "#7798BF", "#aaeeee"],
    chart: {
        backgroundColor: {
            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
            stops: [
                [0, '#2a2a2b'],
                [1, '#3e3e40']
            ]

        },
        style: {
            fontFamily: "'Unica One', sans-serif"
        },
        plotBorderColor: '#606063'
    },
    title: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase',
            fontSize: '33px'
        }
    },
    subtitle: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase'
        }
    },
    xAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        title: {
            style: {
                color: '#A0A0A3'

            }
        }
    },
    yAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        tickWidth: 1,
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.45)',
        style: {
            color: '#F0F0F0'
        }
    },
    plotOptions: {
        series: {
            dataLabels: {
                color: '#B0B0B3'
            },
            marker: {
                lineColor: '#333'
            }
        },
        boxplot: {
            fillColor: '#505053'
        },
        candlestick: {
            lineColor: 'white'
        },
        errorbar: {
            color: 'white'
        }
    },
    legend: {
        itemStyle: {
            color: '#E0E0E3'
        },
        itemHoverStyle: {
            color: '#FFF'
        },
        itemHiddenStyle: {
            color: '#606063'
        }
    },
    credits: {
        style: {
            color: '#666'
        }
    },
    labels: {
        style: {
            color: '#707073'
        }
    },

    drilldown: {
        activeAxisLabelStyle: {
            color: '#F0F0F3'
        },
        activeDataLabelStyle: {
            color: '#F0F0F3'
        }
    },

    navigation: {
        buttonOptions: {
            symbolStroke: '#DDDDDD',
            theme: {
                fill: '#505053'
            }
        }
    },

    // scroll charts
    rangeSelector: {
        buttonTheme: {
            fill: '#505053',
            stroke: '#000000',
            style: {
                color: '#CCC'
            },
            states: {
                hover: {
                    fill: '#707073',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                },
                select: {
                    fill: '#000003',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        inputBoxBorderColor: '#505053',
        inputStyle: {
            backgroundColor: '#333',
            color: 'silver'
        },
        labelStyle: {
            color: 'silver'
        }
    },

    navigator: {
        handles: {
            backgroundColor: '#666',
            borderColor: '#AAA'
        },
        outlineColor: '#CCC',
        maskFill: 'rgba(255,255,255,0.1)',
        series: {
            color: '#7798BF',
            lineColor: '#A6C7ED'
        },
        xAxis: {
            gridLineColor: '#505053'
        }
    },

    scrollbar: {
        barBackgroundColor: '#808083',
        barBorderColor: '#808083',
        buttonArrowColor: '#CCC',
        buttonBackgroundColor: '#606063',
        buttonBorderColor: '#606063',
        rifleColor: '#FFF',
        trackBackgroundColor: '#404043',
        trackBorderColor: '#404043'
    },

    // special colors for some of the
    legendBackgroundColor: 'rgba(0, 0, 0, 0.3)',
    background2: '#505053',
    dataLabelsColor: '#B0B0B3',
    textColor: '#C0C0C0',
    contrastTextColor: '#F0F0F3',
    maskColor: 'rgba(255,255,255,0.3)'
};

// Apply the theme
Highcharts.setOptions(Highcharts.theme);
function TableManager(tableContainer,vsInstance,floatButtionDiv,labelDiv,type){
    var tableManagerInstance = this;
    this.tableDiv = tableContainer;
    var highChartTable = null;
    this.type = type;
    this.vsIntance = vsInstance;
    this.label = labelDiv;
    this.title = "";
    this.categories = [];
    if (type == 1){
        this.categories=['Playgrounds', 'Public Schools', 'Catholic School', 'SingleHouse', 'DuplexHouse','RowHouse','Apartment Five', 'Apartment Four', 'Hotel'];
        this.defaultdata = [0,0,0,0,0,0,0,0,0];
        this.title = "Environment Matching"
    }else{
        this.categories=[ 'Age<14', '14<Age<35','35<Age<60', '60<Age', 'Student', 'UnEmployed', 'Employed'];
        this.defaultdata = [0,0,0,0,0,0,0];
        this.title = "Background Matching"

    }
    floatButtionDiv.click(function(){
       // console.log(tableManagerInstance.vsIntance.currentItem["name"]);
        tableManagerInstance.label.text(tableManagerInstance.vsIntance.currentItemData["name"]);
        if (tableManagerInstance.type == 1) {
            tableManagerInstance.highChartTable.series[0].setData(tableManagerInstance.vsIntance.currentItemData["attributes"].slice(0,8));
        }else{
            tableManagerInstance.highChartTable.series[0].setData(tableManagerInstance.vsIntance.currentItemData["attributes"].slice(9,15));
        }
    });

    this.initTable = function(){
        tableManagerInstance.highChartTable = new Highcharts.Chart({
            title:{
                text: tableManagerInstance.title,
                style: {

                    font: 'normal 14px Verdana'

                },
                y:10
            },

            chart: {
                type: 'bar',
                renderTo:tableManagerInstance.tableDiv

            },

            xAxis: {
                categories: tableManagerInstance.categories

            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Counts',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                },
                opposite:false
            },
            tooltip: {
                valueSuffix: ' units'
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            //legend: {
            //    layout: 'vertical',
            //    align: 'right',
            //    verticalAlign: 'top',
            //    x: -40,
            //    y: 80,
            //    floating: true,
            //    borderWidth: 1,
            //    shadow: true
            //},
            credits: {
                enabled: false
            },
            series: [{
                name: "Number of Unites",
                data: tableManagerInstance.defaultdata
            }]
        });

    }


}