import Vue from 'vue'
import Router from 'vue-router'
import BookInfo from '@/components/BookInfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'BookInfo',
      component: BookInfo
    }
  ]
})
