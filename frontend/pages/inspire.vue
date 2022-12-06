<template>
  <v-row>
    <v-col class="text-center">
      <img
        src="/v.png"
        alt="Vuetify.js"
        class="mb-5"
      >
      <blockquote class="blockquote">
        {{ data.message }}
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

export default {
  name: 'InspirePage',
  async asyncData () {
    let data = await axios.get('http://localhost/api')
    console.log(data)
    return data.data
  }
}
</script>
