<template>
  <v-row>
    <v-col class="text-center">
      <img
        src="/v.png"
        alt="Vuetify.js"
        class="mb-5"
      >
      <blockquote class="blockquote">
        {{ data.classdata }}
        <footer>
          <small>
            <em>&mdash;John Johnson</em>
          </small>
        </footer>
      </blockquote>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost';

export default {
  name: 'Todo',
  // 静的データ
  data() {
    return {
      items: []
    }
  },
  // 通信で取得するデータ
  async asyncData () {
    const data = await axios.get('/api/getCalenderDetail/00001')
    return data
  }
}
</script>
