import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import User from "../components/User";
import UserDetail from "../components/UserDetail";

Vue.use(Router)

export default new Router({
  routes: [
      {path: '/',name: 'Home', redirect: "/home"},
      {path: '/home', name: 'Home', component: Home},
      {path: '/user', name: 'User', component: User},
      {path: '/detail:id', name: 'UserDetail', component: UserDetail,}

  ]
})
