<template>
  <div>
    <svg style="display:none;">
      <defs>
        <symbol id="fivestars2">
          <svg width="100" height="100" viewBox="0 0 90 90">
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="white" fill-rule="evenodd"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="white" fill-rule="evenodd" transform="translate(24)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="white" fill-rule="evenodd" transform="translate(48)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="white" fill-rule="evenodd" transform="translate(72)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="white" fill-rule="evenodd"  transform="translate(96)"/>
          </svg>
        </symbol>
      </defs>
    </svg>
    <div class="rating-comment">
      <progress class="rating-bg" :value="comment.rate" max="5"></progress>
      <svg><use xlink:href="#fivestars2"/></svg>
    </div>
    <div>{{ comment }}</div>
  </div>
</template>

<script>
export default {
  name: "CommentListItem",
  props: {
    comment:Object
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

.rating-comment {
  width: 120px;
  height: 24px;
  position: relative;
  background-color: gray;
}

.rating2-comment progress.rating-bg {
  -webkit-appearance: none;
  -moz-appearence: none;
  appearance: none;
  border: none;
  display: inline-block;
  height: 24px;
  width: 100%;
  color: orange;
}

.rating-comment progress.rating-bg::-webkit-progress-value {
  background-color: orange;
}

.rating-comment progress.rating-bg::-moz-progress-bar {
  background-color: orange;
}

.rating-comment svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>