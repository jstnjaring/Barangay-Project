import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../views/About'
import AnnouncementCard from '../components/AnnouncementCard'
Vue.use(VueRouter)


  const routes = [
  {
    path: '/About',
    name: 'About',
    component: About
  },
  {
    path:'/AnnouncementCard',
    name: 'AnnouncementCard',
    component: AnnouncementCard
  }
]

const router = new VueRouter({
  routes
})

export default router
