import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignupView from "../views/SignupView.vue";
import LoginView from "../views/LoginView.vue";
import MainView from "@/views/Main/MainView";
import MovieDetailView from "@/views/Detail/MovieDetailView.vue";
import MyProfileView from "@/views/Profile/MyProfileView";
import UnseenMovieView from "@/views/Profile/components/UnseenMovieView.vue";
import SearchView from "@/views/SearchView.vue";
// import AccountDeleteView from '../views/AccountDeleteView.vue'

Vue.use(VueRouter);

const routes = [
  {
    // 처음 시작 페이지
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    //
    path: "/signup",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/main",
    name: "main",
    component: MainView,
  },
  {
    path: "/main/:user_id",
    name: "main",
    component: MainView,
  },
  {
    path: "/detail/:movie_id",
    name: "detail",
    component: MovieDetailView,
  },
  {
    path: "/profile",
    name: "profile",
    component: MyProfileView,
  },
  {
    path: "/profile/unseen",
    name: "unseen",
    component: UnseenMovieView,
  },
  {
    path: "/search/:search",
    name: "search",
    component: SearchView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
