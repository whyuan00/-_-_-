<template>
<body>
  <div>
        <h3 class="title">내 주변의 은행을 찾아볼까요?</h3>
        <p class="fontstyle">* 주소를 입력하고, 찾기 버튼을 누르면 해당 지역 은행 정보가 나타납니다.</p>
        <hr>
    </div>
    <div style="display:flex;">
        
        <div class="selectbox">
            <div class="form-group">
                <select v-model="selectedCity" @change="onChangeCity" class="form-control selectedBank">
                    <option value="">시/도 선택</option>
                    <option v-for="(v, city) in data" :value="city">{{ city }}</option>
                </select>
            </div>
            <div class="form-group">
                <select v-model="selectedDistrict" class="form-control selectedBank">
                    <option value="">시/군/구 선택</option>
                    <option v-for="district in districtvalue" :value="district">{{ district }}</option>
                </select>
            </div>
            <div class="form-group">
                <select v-model="selectedBank" class="form-control selectedBank">
                    <option value="">은행 선택</option>
                    <option v-for="bank in banks" :value="bank">{{ bank }}</option>
                </select>
            </div>
            <button @click="searchBank" class="btn btn-primary">찾기</button>
        </div>
    </div>


</body>
<p style="color:brown"> {{ msg }} </p>
  <div class="map_wrap">
    <div id="map" style="width: 100%; height: 100%; "></div>

    <div id="menu_wrap" class="bg_white">
      <hr />
      <ul id="placesList"></ul>
      <div id="pagination"></div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, watch } from "vue";
import data from "../../../../final-pjt-back/map/city_district.json"; // 로컬 파일 가져오기

const selectedCity = ref(""); // 선택된 city
const selectedDistrict = ref(""); // 선택된 district
const selectedBank = ref(""); //선택된 은행
const districtvalue = ref(""); // 선택된 시도의 시/군/구(array)
const keyword = ref(""); // selected 반영한 검색 키워드
const msg = ref(""); // select 안하면 주의메세지

const banks = ref([
  "KEB하나은행",
  "SC제일은행",
  "경남은행",
  "광주은행",
  "국민은행",
  "기업은행",
  "농협",
  "대구은행",
  "부산은행",
  "수협",
  "신한은행",
  "외환은행",
  "우리은행",
  "전북은행",
  "제주은행",
  "특수은행",
  "한국산업은행",
  "한국 스탠다드 차타드 은행",
  "한국수출입은행",
  "한국시티은행",
]);

// selectedcity 가 바뀌면 districtvalue가 바뀜
const onChangeCity = function () {
  selectedDistrict.value = ""; // 시도 바뀌면 시군구 초기화
  if (selectedCity.value) {
    districtvalue.value = data[selectedCity.value]; // data 는 {key:[value,value,...], ...} 로 저장됨
  } else {
    // 선택된 도시가 없을 경우 districtvalue를 비움
    districtvalue.value = [];
  }
};

let MAP_API_KEY;
let map; // 지도 객체
let ps; // 검색시 새로운 place 객체
let markers = [];
let infowindow; // 인포 윈도우
let iwContent; // 인포 내용

let listEl
let menuEl 
let fragment
let bounds 
let listStr 
let placePosition
let itemEl
let marker
// let imageSize 
// let imgOptions
// let spriteSize
// let spriteOrigin
// let offset

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/map/api_key/",
  })
    .then((response) => {
      MAP_API_KEY = response.data;
      console.log("GET MAP_API_KEY");
      const script = document.createElement("script");
      //
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${MAP_API_KEY.MAP_API_KEY}&libraries=services&autoload=false`;
      document.head.appendChild(script);
      script.onload = () => {
        window.kakao.maps.load(() => {
          const mapContainer = document.getElementById("map");
          const mapOption = {
            center: new window.kakao.maps.LatLng(37.5012969, 127.0396119), // 지도의 중심좌표
            level: 3, // 지도의 확대 레벨
          };
          // 지도 객체는 반응형이 아님
          map = new window.kakao.maps.Map(mapContainer, mapOption);
          console.log("MAP LOAD COMPLETE");
          makeMarker();
        });
      };
    })
    .catch((error) => {
      console.log("지도apikey실패", error);
    });
});


// select변할때 검색하는 함수
watch(
  [selectedCity, selectedDistrict, selectedBank],
  ([newCity, newDistrict, newBank]) => {
    keyword.value = `${newCity} ${newDistrict} ${newBank}`;
  }
);

// 은행 검색하는 함수
const searchBank = function () {
  if (!keyword.value.trim()) {
    msg.value = "장소를 선택해 주세요";
  } else {
    msg.value = null;

    ps = new window.kakao.maps.services.Places();
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    ps.keywordSearch(keyword.value, placesSearchCB);
  }
};


// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    // 정상적으로 검색이 완료됐으면
    // 검색 목록과 마커를 표출합니다
    console.log(data); // data 표출

    displayPlaces(data);
    // 페이지 번호를 표출합니다
    displayPagination(pagination);
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    msg.value = "검색 결과가 존재하지 않습니다.";
    return;
  } else if (status === kakao.maps.services.Status.ERROR) {
    msg.value = "검색 결과 중 오류가 발생했습니다.";
    return;
  }
}

// 검색 결과 목록과 마커를 표출하는 함수입니다
function displayPlaces(places) {

listEl = document.getElementById("placesList")
menuEl = document.getElementById("menu_wrap")
fragment = document.createDocumentFragment()
bounds = new kakao.maps.LatLngBounds()
listStr = ""

if (listEl){
    // 검색 결과 목록에 추가된 항목들을 제거합니다
    removeAllChildNods(listEl);
}

// 지도에 표시되고 있는 마커를 제거합니다
removeMarker();

  for (var i = 0; i < places.length; i++) {
    // 마커를 생성하고 지도에 표시합니다
    placePosition = new kakao.maps.LatLng(places[i].y, places[i].x)
    marker = addMarker(placePosition, i)
    itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    bounds.extend(placePosition);

    // 마커와 검색결과 항목에 mouseover 했을때
    // 해당 장소에 인포윈도우에 장소명을 표시합니다
    // mouseout 했을 때는 인포윈도우를 닫습니다
    (function (marker, title) {
      kakao.maps.event.addListener(marker, "mouseover", function () {
        displayInfowindow(marker, title);
      });
      kakao.maps.event.addListener(marker, "mouseout", function () {
        infowindow.close();
      });
      itemEl.onmouseover = function () {
        displayInfowindow(marker, title);
      };
      itemEl.onmouseout = function () {
        infowindow.close();
      };
    })(marker, places[i].place_name);
    fragment.appendChild(itemEl);
  }

  // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
  if (listEl) {
    listEl.appendChild(fragment);
    menuEl.scrollTop = 0;

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds);
  }

} // end displayPlace

// 검색결과 항목을 Element로 반환하는 함수입니다
function getListItem(index, places) {
  var el = document.createElement("li"),
    itemStr ='<span class="markerbg marker_' +(index + 1) +'"></span>' +
      '<div class="info">' +
      "   <h5>" +
      places.place_name +
      "</h5>";
  if (places.road_address_name) {
    itemStr +=
      "    <span>" +
      places.road_address_name +
      "</span>" +
      '   <span class="jibun gray">' +
      places.address_name +
      "</span>";
  } else {
    itemStr += "    <span>" + places.address_name + "</span>";
  }

  itemStr += '  <span class="tel">' + places.phone + "</span>" + "</div>";

  el.innerHTML = itemStr;
  el.className = "item";

  return el;
}

// 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
function addMarker(position, idx, title) {
    var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
        imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
        imgOptions =  {
            spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
            spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
            offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
            marker = new kakao.maps.Marker({
            position: position, // 마커의 위치
            image: markerImage 
        });

    marker.setMap(map); // 지도 위에 마커를 표출합니다
    markers.push(marker);  // 배열에 생성된 마커를 추가합니다

    return marker;
}

// 지도 위에 표시되고 있는 마커를 모두 제거합니다
function removeMarker() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers = [];
}

//  검색결과 목록 하단에 페이지번호를 표시는 함수입니다
function displayPagination(pagination) {
    var paginationEl = document.getElementById('pagination'),
        fragment = document.createDocumentFragment(),
        i; 

    // 기존에 추가된 페이지번호를 삭제합니다
    while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild (paginationEl.lastChild);
    }

    for (i=1; i<=pagination.last; i++) {
        var el = document.createElement('a');
        el.href = "#";
        el.innerHTML = i;

        if (i===pagination.current) {
            el.className = 'on';
        } else {
            el.onclick = (function(i) {
                return function() {
                    pagination.gotoPage(i);
                }
            })(i);
        }

        fragment.appendChild(el);
    }
    paginationEl.appendChild(fragment);
}

// 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
// 인포윈도우에 장소명을 표시합니다
function displayInfowindow(marker, title) {
    var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
  infowindow.setContent(content);
  infowindow.open(map, marker);
}

// 검색결과 목록의 자식 Element를 제거하는 함수입니다
function removeAllChildNods(el) {   
    while (el.hasChildNodes()) {
        el.removeChild (el.lastChild);
    }
}

//시작위치(싸피) 마커 만드는 함수
function makeMarker() {
  const markerPosition = new window.kakao.maps.LatLng(37.5012969, 127.0396119);
  const marker = new window.kakao.maps.Marker({
    position: markerPosition,
  });
  marker.setMap(map);
  iwContent = '<div style="width:170px; padding:5px;">"Hi Im now in SSAFY"</div>'
  // 인포윈도우를 생성합니다
  infowindow = new window.kakao.maps.InfoWindow({
    position: markerPosition,
    content: iwContent,
  });
  
  infowindow.open(map, marker);
}

</script>


<style>

.fontstyle {
  font-family: 'Noto Sans KR', sans-serif;
}

h1 {
   font-family: 'Noto Sans KR', sans-serif;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 500;
  color: #339af0; /* 토스 느낌의 연한 파란색 */
}

.selectbox {
    font-family: 'Noto Sans KR', sans-serif;
    margin: 0 auto;
    padding: 20px;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
.form-group {
    font-family: 'Noto Sans KR', sans-serif;
    margin-bottom: 10px;
}

.form-control {
    font-family: 'Noto Sans KR', sans-serif;
    border-radius: 25px;
    font-size: 16px;
}

.btn-primary {
    font-family: 'Noto Sans KR', sans-serif;
    width: 100%;
    border-radius: 25px;
    padding: 10px;
    font-size: 16px;
}

.btn-primary:hover {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #0056b3;
    border-color: #004085;
}

.title {
    font-family: 'Noto Sans KR', sans-serif;
    margin-top: 100px; /* Nav 바의 높이만큼 여백 추가 */
    font-size: 30px;
    font-weight: bold;
    color: #333;
}

<!-- 구글 폰트 추가 -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500&display=swap">


.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#f7f3f3;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:370px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}
</style>