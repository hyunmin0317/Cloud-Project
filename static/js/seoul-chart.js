function highMaps() {

	var me = this;

	me.chart = null;
	me.selected = '0';
	me.event = {
		select : function(){

		},
		unselect : function(){

		},
		drillup : function(){

		}
	};

	me.init();
};

highMaps.prototype.init = function(){
	var me = this;
	// 전국단위 지도 로드
	$.getJSON('https://raw.githubusercontent.com/ssm-lim/bPolygon/master/bPolygon/highmap/json/11.json', function (geojson) {
        var data = Highcharts.geojson(geojson, 'map');
        $.each(data, function () {
        	this.drilldown = this.properties['code'];
        });
        $('#map').highcharts('Map', {
        	credits: { enabled: false },
            chart : {
                events: {
                	// drilldown : 클릭시 하위레벨로 진입
                    drilldown: function (e) {
                        window.location.href = '/hip/'+e.point.name;
                    },

                }
            },
            series : [{
                data : data,
                showInLegend: false,
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    allowOverlap: false,
                    shadow: false,
                    format: '{point.properties.name}'
                },
                states: {
                	// 상위 지도 hover 스타일 설정
                    hover: {
                        color: '#99004C',
                        borderColor: 'white'
                    }
                },
                tooltip: {
                	headerFormat: '',
                    pointFormat: '{point.properties.name}'
                }
            }],
            // 제목 제거
            title: null,
            // 부제목 제거
            subtitle: null,

            // 지역 선택시 하위 지도 띄우는 기능 설정
            drilldown: {
            	// 상위 지도 레이블 스타일 설정
                activeDataLabelStyle: {
                	color : '#000',
                	shadow: false,
                    textShadow: '0 0 0px #000000',
                    fontWeight: "none",
                    textDecoration: 'none'
                },
                // 상위 지도 버튼 스타일 설정
                drillUpButton: {
                    relativeTo: 'spacingBox'
                }
            },
            plotOptions: {
                series: {
                    point : {
                    	events: {
                            select: function () {
                            	// this.properties에 지정한 코드나 이름 값이 저장
                            	me.selected = this.properties.code;
                            	try {
                            		me.event.select();
                            	} catch(err){}
                            },
                            unselect: function () {
                            	// 기본적으로는 select 이벤트 발생 후 unselect가 발생
                            	// 아래의 코드를 사용하면 unselect 적용 후 select 이벤트가 발생
                            	var p = this.series.chart.getSelectedPoints();
                                if(p.length > 0 && p[0].x == this.x) {
                                	try {
                                		me.event.unselect();
                                	} catch(err){}
                                }
                                me.selected = this.properties.code.substring(0,2);
                            }
                        }
                    }
                }
            }
        });
        me.chart = $("#map").highcharts();
    });
};

var highMap = new highMaps();
highMap.init();