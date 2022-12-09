<template v-if="initialData">
  <v-card
      color="grey lighten-4"
      min-width="350px"
      flat
  >
      <v-toolbar  :color="color" dark>
      <profile-edit-dialog
        :initial-data="profile"
        @submitted="submitted"
      />
      <v-toolbar-title v-html="profile.name"></v-toolbar-title>
      <v-spacer></v-spacer>
      </v-toolbar>
      <v-card-text>
      <div>
        <v-card class="ma-auto pa-4" max-width="400" tile>
          <v-card-subtitle class="pb-1 font-weight-bold">講義名</v-card-subtitle>
          <v-card-text class="pt-0 pb-1">
            {{ profile.name }}
          </v-card-text>
          <v-card-subtitle class="pt-0 pb-1 font-weight-bold">教員</v-card-subtitle>
          <v-card-text class="pt-0 pb-1">
            {{ profile.teacher }}
          </v-card-text>
          <v-card-subtitle class="pt-0 pb-1 font-weight-bold">教室</v-card-subtitle>
          <v-card-text class="pt-0 pb-1">
            {{ profile.classroom }}
          </v-card-text>
          <div v-if="(profile.links.length!=0)">
            <v-card-subtitle class="pt-0 pb-1 font-weight-bold">
              授業リンク
            </v-card-subtitle>
            <ul>
            <li v-for="(link, index) in profile.links" class="pt-0 pb-1" :key="index+'_link'" v-if="(link!=null)">
                {{ link }}
            </li>
            </ul>
          </div>
          <div v-if="(profile.tasks.length!=0)">
            <v-card-subtitle class="pt-0 pb-1 font-weight-bold">
              課題
            </v-card-subtitle>
            <ul>
            <li v-for="(task, index) in profile.tasks" class="pt-0 pb-1" :key="index+'_task'" v-if="(task!=null)">
              <v-row no-gutters>
              課題名 : {{ task.name }}
            </v-row>
              <v-row no-gutters>
              課題リンク : {{ task.link }}
            </v-row>
            <v-row no-gutters>
              期限 : {{ task.limitdate }}
            </v-row>
            </li>
            </ul>
          </div>
        </v-card>
      </div>
      </v-card-text>
      <v-card-actions>
      <v-btn
          text
          color="secondary"
          @click="closeCard"
      >
          Cancel
      </v-btn>
      </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    initialData: Object,
    color: String,
  },
  data: function() {
    return {
      profile: {} 
    }
  },
  created: function (){
    this.profile = this.initialData
  },
  methods: {
    submitted: function (p){
      this.$emit("submitted", p)
      this.profile = p
    },
    closeCard: function() {
      this.$emit("close")
    }
  }
}
</script>

<style>
.theme--dark.v-card > .v-card__text, .theme--dark.v-card > .v-card__subtitle {
    color: rgba(255, 255, 255, 1);
    font-size: 15px;
}
</style>