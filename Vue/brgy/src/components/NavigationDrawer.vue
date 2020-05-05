<template>
      <v-navigation-drawer
        enable-resize-watcher
        :color="color"
        :expand-on-hover="true"
        :permanent="true"
        dark
        absolute
      >
        <v-list
          dense
          nav
          class="py-0"
        >
          <v-list-item two-line class="px-0">
            <v-list-item-avatar>
              <img src="https://media-exp1.licdn.com/dms/image/C5103AQFN-hhgLGjtNQ/profile-displayphoto-shrink_200_200/0?e=1593648000&v=beta&t=dJURGjRj9M-f0QsBq2IGHHFvcyi0xd2JtBsBjIQsKIw">
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{user}}</v-list-item-title>
              <v-list-item-subtitle>{{position}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-divider></v-divider>

          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            :to ="item.path"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        user: 'Marvin de Guzman',
        position: 'SK Kagawad',
        items: [
          { title: 'Announcements', icon: 'mdi-view-dashboard', path:'/AnnouncementCard' },
          { title: 'About', icon: 'mdi-image', path:'/About' }
        ],
        color: 'primary'
      }
    },
    computed: {
      bg () {
        return this.background ? 'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg' : undefined
      },
    },
  }
</script>