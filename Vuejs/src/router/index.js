import Vue from 'vue'
import Router from 'vue-router'
import Challenge from '@/components/Challenge'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/challenge',
      name: 'Challenge',
      component: Challenge
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
