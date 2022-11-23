<template>
  <div class="mt-4">
    <div v-if="comment?.user_id === this.$store.state.userdata.id" class="float-right relative">
      <button id="dropdownMenuIconButton" @click="toggleOpen" class="inline-flex items-center float-right p-2 text-sm font-medium text-center rounded-lg focus:ring-4 focus:outline-none text-white focus:ring-gray-50 bg-gray-800 hover:bg-gray-700 hober:focus:ring-gray-600" type="button"> 
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"></path></svg>
      </button>
      <div v-if="open" @click="deleteComment" class="flex items-center cursor-pointer justify-center p-2 w-28 text-sm top-11 right-0.5 absolute text-center rounded-lg focus:ring-4 focus:outline-none text-red-600 focus:ring-gray-50 bg-gray-800 hover:bg-gray-700 hober:focus:ring-gray-600">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
          <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
          <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
        </svg>
        삭제하기
      </div>
    </div>

    <svg style="display:none;">
      <defs>
        <symbol id="fivestars2">
          <svg width="100" height="100" viewBox="0 0 120 120">
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(24)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(48)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(72)"/>
            <path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z M0 0 h24 v24 h-24 v-24" fill="black" fill-rule="evenodd" transform="translate(96)"/>
          </svg>
        </symbol>
      </defs>
    </svg>
    <div class="rating-comment">
      <progress class="rating-bg" :value="comment.rate" max="5"></progress>
      <svg><use xlink:href="#fivestars2"/></svg>
    </div>
    <div class="my-1 text-2xl">{{ comment.content }} {{ comment.likes }}</div>
    <div class="text-xs">{{ nickname }} • {{ comment.created_at.slice(0, 10) }}</div>
    <button 
      v-on="isLike ? {click:() => {commentDislike();}} : {click:() => {commentLike();}}" 
      class="rounded-full border w-32 border-slate-500 py-2 px-2 mt-2 flex justify-center"
      :class="isLike ? 'bg-white text-black' : 'bg-black'"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="21" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 -1 16 16">
        <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
      </svg>
      <div>
        &nbsp;&nbsp;좋아요 ({{comment.likes}})
      </div>
    </button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: "CommentListItem",
  data() {
    return {
      nickname: null,
      likes: null,
      isLike: false,
      open: false
    }
  },
  props: {
    comment:Object
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    },
    likesNum() {
      // console.log(this.likes)
      return this.likes
    },
  },
  created() {
    this.getUser()
    this.getCommentLike()    
  },
  mounted() {
    console.log(this.likes)
    // this.likes.forEach((el) => {
    //   console.log(el)
    // })
  },
  methods: {
    toggleOpen() {
      this.open = !this.open
    },
    toggleClose() {
      if (this.open === true) {
        this.open = false
      }
    },
    getUser() {
      axios({
          method: 'GET',
          url: `${API_URL}/accounts/get/user/${this.comment.user_id}/`,
      })
        .then((res) => {
          this.nickname = res.data.nickname
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCommentLike(){
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/comments/like/list/${this.comment.comment_id}/`,
      })
        .then((res) => {
          this.likes = res.data
          this.likes.forEach((el) => {
            if (el.user_id === this.$store.state.userdata.id) {
              this.isLike = true
            } else {
              this.isLike = false
            }
          })
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    commentLike() {
      if (!this.isLogin) {
        alert('로그인 하세용')
      } else {
        axios({
          method: 'POST',
          url: `${API_URL}/api/v1/comments/like/${this.comment.comment_id}/`,
          data: {
            user_id: this.$store.state.userdata.id,
            comment_id: this.comment.comment_id
          },
          headers: {
            Authorization: `Bearer ${this.$store.state.access}`
          }
        })
        // eslint-disable-next-line
          .then(() => {
            // console.log(res)
            this.isLike=true
            this.$emit('like')
            
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    commentDislike() {
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/comments/like/detail/${this.comment.comment_id}/`,
        data: {
          user_id: this.$store.state.userdata.username,
          comment_id: this.comment.comment_id
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.access}`
        }
      })
      // eslint-disable-next-line
        .then(() => {
          this.isLike = false
          this.likes -= 1
          this.getCommentLike()
          this.$emit('like')
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment() {
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/comments/${this.comment.comment_id}/`,
      })
      // eslint-disable-next-line
        .then(() => {
          this.$emit('del')
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

.rating-comment {
  width: 100px;
  height: 22px;
  position: relative;
  background-color: black;
}

.rating-comment progress.rating-bg {
  -webkit-appearance: none;
  -moz-appearence: none;
  appearance: none;
  border: none;
  display: inline-block;
  height: 19.5px;
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