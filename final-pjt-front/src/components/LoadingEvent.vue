<template>
  <div>
    <div class="loading-body">
      <div class="loading font-bold">Loading JWT</div>
      
  <!-- dribbble -->
      <a class="dribbble" href="https://dribbble.com/shots/6616259-Loading-text-animation" target="_blank"><img src="@/assets/small-logo.png" alt=""></a>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';
export default {
  name:'LoadingEvent',
  data() {
    return{
      start:false
    }
  },
  created(){
    this.startLoading()
    this.start = true
  },
  methods:{
    startLoading() {
      let loading = $('.loading').wrapInner('<div></div>'),
        min = 20,
        max = 70,
        minMove = 10,
        maxMove = 20;

      startAnimation(loading);
// eslint-disable-next-line
      loading.on('animationend webkitAnimationEnd oAnimationEnd', 'span:last-child', e => {
          startAnimation(loading);
      });

      //Set CSS vars & generate spans if needed
      function setCSSVars(elem, min, max, minMove, maxMove) {
          let width = Math.ceil(elem.width()),
              text = elem.text();
          for(let i = 1; i < width; i++) {
              let num = Math.floor(Math.random() * (max - min + 1)) + min,
                  numMove = Math.floor(Math.random() * (maxMove - minMove + 1)) + minMove,
                  dir = (i % 2 == 0) ? 1 : -1,
                  spanCurrent = elem.find('span:eq(' + i + ')'),
                  span = spanCurrent.length ? spanCurrent : $('<span />');
              span.css({
                  '--x': i - 1 + 'px',
                  '--move-y': num * dir + 'px',
                  '--move-y-s': ((i % 2 == 0) ? num * dir - numMove : num * dir + numMove) + 'px',
                  '--delay': i * 10 + 'ms'
              });
              if(!spanCurrent.length) {
                  elem.append(span.text(text));
              }
          }
      }

      //Start animation
      function startAnimation(elem) {
          elem.removeClass('start');
          setCSSVars(elem, min, max, minMove, maxMove);
          void elem[0];
          elem.addClass('start');
      }
    }
  }
}

</script>

<style lang="scss">
.loading {
    --color: #F5F9FF;
    --duration: 2000ms;
    font-family: Roboto, Arial;
    font-size: 24px;
    position: relative;
    white-space: nowrap;
    user-select: none;
    color: var(--color);
    span {
        --x: 0;
        --y: 0;
        --move-y: 0;
        --move-y-s: 0;
        --delay: 0ms;
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        width: 1px;
        text-indent: calc(var(--x) * -1);
        overflow: hidden;
        transform: translate(var(--x), var(--y));
    }
    &.start {
        div {
            opacity: 0;
        }
        span {
            animation: move var(--duration) ease-in-out var(--delay);
        }
    }
}

@keyframes move {
    30% {
        transform: translate(var(--x), var(--move-y));
    }
    82% {
        transform: translate(var(--x), var(--move-y-s));
    }
}

html {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
}

* {
    box-sizing: inherit;
}

// Center & dribbble
.loading-body {
    min-height: 100vh;
    widows: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #151924;
    .dribbble {
        position: fixed;
        display: block;
        right: 20px;
        bottom: 20px;
        img {
            display: block;
            height: 28px;
        }
    }
}
</style>