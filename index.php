<html>
    <head>
        <meta charset="utf-8">
        <script src="lib/esl.js"></script>
        <script src="lib/config.js"></script>
    </head>
    <body>
      <?php

      $m = new MongoClient(); // connect
      $db = $m->selectDB("test");

      ?>
        <style>
            html, body, #main {
                width: 100%;
                height: 100%;
            }
        </style>
        <div id="main"></div>
        <script>

            require([
                'echarts'
                // 'echarts/chart/scatter',
                // 'echarts/component/legend',
                // 'echarts/component/grid',
                // 'echarts/component/tooltip',
                // 'echarts/component/toolbox'
            ], function (echarts) {

                var chart = echarts.init(document.getElementById('main'));

                var data1 = [];
                var data2 = [];
                var data3 = [];

                var names = [
                    'diamond, red, show inside label only on hover',
                    'green, show top label only on hover',
                    'indigo, show inside label on normal'
                ];

                var random = function (max) {
                    return (Math.random() * max).toFixed(3);
                }

                for (var i = 0; i < 50; i++) {
                    data1.push([random(5), random(5), random(2)]);
                    data2.push([random(10), random(10), random(2)]);
                    data3.push([random(15), random(10), random(2)]);
                }

                chart.setOption({
                    aria: {
                        show: true
                    },
                    legend: {
                        data: names.slice()
                    },
                    toolbox: {
                        left: 'left',
                        feature: {
                            dataView: {},
                            saveAsImage: {},
                            dataZoom: {}
                        }
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross'
                        }
                    },
                    xAxis: {
                        type: 'value',
                        splitLine: {
                            show: false
                        },
                        min: 0,
                        max: 15,
                        splitNumber: 30
                    },
                    yAxis: {
                        type: 'value',
                        splitLine: {
                            show: false
                        }
                    },
                    series: [{
                        name: names[0],
                        type: 'scatter',
                        label: {
                            emphasis: {
                                show: true
                            }
                        },
                        symbol: 'diamond',
                        symbolSize: function (val) {
                            return val[2] * 40;
                        },
                        data: data1
                    },
                    {
                        name: names[1],
                        type: 'scatter',
                        emphasis: {
                            label: {
                                show: true,
                                position: 'top',
                                formatter: function (params) {
                                    return params.value;
                                }
                            }
                        },
                        symbolSize: function (val) {
                            return val[2] * 40;
                        },
                        itemStyle: {
                            color: function (params) {
                                return 'rgba(30, 70, 50, ' + params.value[2] + ')';
                            }
                        },
                        data: data2
                    },
                    {
                        name: names[2],
                        type: 'scatter',
                        label: {
                            show: true
                        },
                        symbolSize: function (val) {
                            return val[2] * 40;
                        },
                        data: data3
                    }],
                    animationDelay: function (idx) {
                        return idx * 20;
                    },
                    animationDelayUpdate: function (idx) {
                        return idx * 20;
                    }
                });

                chart.on('click', function (params) {
                    console.log(params.data);
                });
            })

        </script>
    </body>
</html>