<template>
  <v-app id="inspire">
    <navigation-drawer></navigation-drawer>
    <toolbar></toolbar>
    <v-content style="margin-left:50px;">
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
// import AnnouncementCard from './components/AnnouncementCard.vue'
import Toolbar from './components/ToolBar.vue'
import NavigationDrawer from './components/NavigationDrawer.vue'
export default {
  name: 'App',
  components: {
    // AnnouncementCard,
     NavigationDrawer,
     Toolbar
  },

  data: () => ({
    drawer: null,
  }),
};
</script>