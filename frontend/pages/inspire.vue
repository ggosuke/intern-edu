<template>
  <v-row>
    <v-col class="text-center">
      <template>
        <v-card
          max-width="400"
          class="mx-auto"
        >
          <v-container>
            <v-row dense>
              <v-col cols="12">
                <v-card
                  color="#385F73"
                  dark
                  class="ma-2"
                  v-for = "(item,index) in items"
                  >
                  <v-card-title class="text-h5">
                    {{item.task}}
                  </v-card-title>

                  <div class="text-center">
                    <v-chip
                      class="ma-2"
                      color="red"
                      text-color="white"
                    >
                      {{item.lesson}}
                    </v-chip>

                    <v-chip
                      class="ma-2"
                      color="green"
                      text-color="white"
                    >
                      {{item.due}}
                    </v-chip>
                  </div>
                  
                  <v-card-subtitle
                    class ="text-center" >

                  
                    課題内容xxxxxxxxxxxxxxxxx
                  </v-card-subtitle>

                  <v-card-actions >
                    <v-col class ="text-right">
                      <v-btn @click="done(index)">
                        完了
                      </v-btn>
                    </v-col>
                  </v-card-actions>
                </v-card>
              </v-col>

            </v-row>
          </v-container>

        </v-card>
      </template>
      <blockquote class="blockquote">
        
      </blockquote>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost';

export default {
  // 静的データ
  data() {
    return {
      items: [{
        lesson_id: 0,
        task: "task1",
        due: "12/1",
        lesson: "lesson1",
        task_detail: "task1xxxx"
      },{
        lesson_id: 1,
        task: "task2",
        due: "12/1",
        lesson: "lesson2",
        task_detail: "task2xxxx"
      }
      ]
    }
  },
  // 通信で取得するデータ
  methods: {
    done(index) {
      this.items.splice(index, 1)
      console.log(index)
    }
  }
}
</script>
