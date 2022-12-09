<template>
  <div>
  <v-row justify="center" align="center" v-if="showlink">
    <v-col cols="12" sm="8" md="6">
      <v-card-title class="headline">
        スケジュール管理を便利にするみんなで作るカレンダーアプリ
      </v-card-title>
      <v-btn text @click="$router.push({ path: 'calendar' , query:{id: username}})">
        <v-icon>mdi-apps</v-icon>
        カレンダー
      </v-btn>
      <v-btn text @click="$router.push({ path: 'todo' , query:{id: username}})">
        <v-icon>mdi-chart-bubble</v-icon>
        TODO
      </v-btn>
    </v-col>
  </v-row>
  <v-card v-if="!showlink">
    <v-card-title>
      <h1 class="display-1">ログイン</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" v-model="username" />
        <v-text-field prepend-icon="mdi-lock" type="password" label="パスワード" />\
        <v-btn
          class="mr-4"
          @click="submit"
        >
          login
        </v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</div>
</template>

<script>
export default {
  // 静的データ
  data() {
    return {
      showlink: false,
      username: '',
      pass: ''
    }
  },
  methods:{
    submit: function(e){
      console.log(this.username)
      this.showlink = true
    }
  }
}
</script>
