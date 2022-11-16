import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import MainView from '@/views/Main/MainView'
import MovieDetailView from '@/views/Detail/MovieDetailView.vue'
// import MyProfileView from '../views/MyProfileView.vue'
// import UnseenMovieView from '../views/UnseenMovieView.vue'
// import AccountDeleteView from '../views/AccountDeleteView.vue'

Vue.use(VueRouter)

const routes = [
  {
  // 처음 시작 페이지
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    // 
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/main',
    name: 'main',
    component: MainView
  },
  {
    path: "/detail/:id",
    name: "detail",
    component: MovieDetailView,
  },
  // {
  //   path: "/profile",
  //   name: "profile",
  //   component: MyProfileView,
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
