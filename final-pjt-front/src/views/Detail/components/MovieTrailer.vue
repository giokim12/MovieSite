<template>
  <transition name="modal">
    <div class="modal-mask" @click="$emit('close')">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
            </slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <div id="ytplayer"></div>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "MovieTrailer",
  props: {
    movieKey: String
  },
  created() {
    onYouTubePlayerAPIReady(this.movieKey)
  }
}
let tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
let firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Replace the 'ytplayer' element with an <iframe> and
// YouTube player after the API code downloads.
// eslint-disable-next-line
let player;
// eslint-disable-next-line
function onYouTubePlayerAPIReady(movieKey) {
  console.log('qkwpodkqwpodkp')
  // eslint-disable-next-line
  player = new YT.Player('ytplayer', {
    height: '860',
    width: '700',
    videoId: movieKey,
    playerVars: {
        'rel': 0,    //연관동영상 표시여부(0:표시안함)
        'controls': 0,    //플레이어 컨트롤러 표시여부(0:표시안함)
        'autoplay' : 1,   //자동재생 여부(1:자동재생 함, mute와 함께 설정)
        'mute' : 0,   //음소거여부(1:음소거 함)
        'loop' : 1,    //반복재생여부(1:반복재생 함)
        'playsinline' : 1,    //iOS환경에서 전체화면으로 재생하지 않게
        'modestbranding' : 1
      },
  });
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  opacity: 0.9;
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper{
  display: table-cell;
  vertical-align: middle;
}

.modal-container{
  position: fixed;
  z-index: 100;
  top: 200;
  left: 200;
  width: 900px;
  height: 500px;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 20px;
  transition: all 0.3s ease;
}
</style>