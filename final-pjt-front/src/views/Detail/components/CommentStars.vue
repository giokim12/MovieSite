<template>
  <div>
    <div class="flex">
      <div class="font-bold text-8xl mr-3">
        {{rate ? rate : '0.0'}}
      </div>
      <svg style="display:none;">
        <defs>
          <symbol id="fivestars">
            <svg width="180" height="180" viewBox="0 0 130 130">
              <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd"/>
              <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(24)"/>
              <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(48)"/>
              <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(72)"/>
              <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd"  transform="translate(96)"/>
            </svg>
          </symbol>
        </defs>
      </svg>
      <div class="absolute top-[110px] left-[180px] text-2xl pl-4">
        {{ comment.length }}개 평점
      </div>
      <div class="rating">
      <!--   <div class="rating-bg" style="width: 90%;"></div> -->
        <progress class="rating-bg" :value="rate" max="5"></progress>
        <svg><use xlink:href="#fivestars"/></svg>
      </div>
    </div>
    <div>
      <CommentCreateVue
        :movie='movie'
        class="mt-5"
      />
    </div>
  </div>
</template>

<script>
import CommentCreateVue from './CommentCreate.vue'

export default {
  name:'CommentStars',
  props: {
    comment:Array,
    movie:Object
  },
  components: {
    CommentCreateVue
  },
  computed: {
    rate() {
      let totalRate = 0.0
      let result = 0.0
      if (this.comment.length > 0) {
        this.comment.forEach((el) => { totalRate += el.rate})
        result = (totalRate/this.comment.length).toFixed(1)
      }
      return result
    }
  },
}
</script>

<style>
* {
  box-sizing: border-box;
}

.rating {
  width: 165px;
  height: 50px;
  position: relative;
  background-color: black;
}

.rating progress.rating-bg {
  -webkit-appearance: none;
  -moz-appearence: none;
  appearance: none;
  border: none;
  display: inline-block;
  position: absolute;
  top: 20px;
  height: 32px;
  width: 100%;
  color: #EF4444;
}

.rating progress.rating-bg::-webkit-progress-value {
  background-color: #EF4444;
}

.rating progress.rating-bg::-moz-progress-bar {
  background-color: #EF4444;
}

.rating svg {
  position: absolute;
  top: 20px;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>