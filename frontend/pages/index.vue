<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card-title class="headline">
        スケジュール管理を便利にするみんなで作るカレンダーアプリ
      </v-card-title>
      <v-btn text to="/calendar">
        <v-icon>mdi-apps</v-icon>
        カレンダー
      </v-btn>
      <v-btn text  to="/todo">
        <v-icon>mdi-chart-bubble</v-icon>
        TODO
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  // 静的データ
  data() {
    return {
      items: []
    }
  },
}
</script>
