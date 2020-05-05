<template>
<div>
    <div v-for="(Announcement, x) in AnnouncementDetails" :key="x">
  <v-card
    class="mx-auto"
    max-width="auto"
    outlined
  >
    <v-list-item three-line >
      <v-list-item-content>
        <div class="overline mb-4">{{Announcement.Date}}</div>
        <v-list-item-title class="headline mb-1">{{Announcement.Title}}</v-list-item-title>
        <v-list-item-subtitle>{{Announcement.CreatedBy}}</v-list-item-subtitle>
        <v-card-text>{{Announcement.Message}}</v-card-text>
      </v-list-item-content>
      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
    </v-list-item>
  </v-card>
  <v-spacer></v-spacer>
  <v-spacer></v-spacer>
  <v-spacer></v-spacer>
    </div>
</div>
</template>
<script>

import vuebase from '../firebase.js'

export default {
    name : 'AnnouncementCard',
    data() {
      return {
      AnnouncementDetails:[]

      }
    },
    mounted() {
      let self = this;
      vuebase.database().ref('Barangay/7ivdJvY8c3WMSlHdkwty/Announcements').on('value', function(snapshot){
        let returnArr = [];
        snapshot.forEach(function(childSnapshot) {
          returnArr.push(childSnapshot.val())
        })
          self.AnnouncementDetails = returnArr
          console.log(self.AnnouncementDetails)
      })
    }
}
</script>