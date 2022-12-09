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
                  color="white"
                  light
                  class="ma-2"
                  v-for = "(item,index) in items"
                  >
                  <v-card-title class="text-h5">
                    {{item.task}}
                  </v-card-title>

                  <div class="text-left ml-3" >
                    <v-chip label
                      class="ma-1"
                      color="blue"
                      text-color="white"
                      

                    >
                      {{item.lesson}}
                    </v-chip>

                    <v-chip label
                      class="ma-1"
                      style= "font-weight:bold" 
                      color="green"
                      text-color="white"
                    >
                      あと
                      {{remainDay(item.due)}}
                      日！
                    </v-chip>
                  </div>
                  
                  <v-card-subtitle
                    class ="text-left" >
                  
                    {{item.task_detail}}
                  </v-card-subtitle>

                  <v-card-actions >
                    <v-col class ="text-right">
                      <v-btn @click="done(index)"
                        color=#B0BEC5>
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
        task: "課題1",
        due: "2022/12/20",
        lesson: "線形代数1",
        task_detail: "練習問題2-20"
      },{
        lesson_id: 1,
        task: "課題2",
        due: "2023/1/20",
        lesson: "古典中世音楽",
        task_detail: "歴史について"
      },{
        lesson_id: 2,
        task: "課題3",
        due: "2023/2/23",
        lesson: "古典中世音楽",
        task_detail: "歴史について"
      },{
        lesson_id: 3,
        task: "課題4",
        due: "2023/1/22",
        lesson: "古典中世音楽",
        task_detail: "歴史について"
      },{
        lesson_id: 4,
        task: "課題5",
        due: "2022/12/15",
        lesson: "古典中世音楽",
        task_detail: "歴史について"
      }
      ]
    }
  },
  // 通信で取得するデータ
  methods: {
    done(index) {
      this.items.splice(index, 1)
      console.log(index)
    },

    
    remainDay(due) {
      console.log(due);
      let date = new Date();
      let dueDate = new Date(due);
      let remain = parseInt((dueDate - date) / 1000/ 60/ 60/ 24);
      return remain;
    },

    sortDate(items) {
      console.log(items);
      const sortedItems = items.sort((a,b) => {
        const dateA = a.due;
        const dateB = b.due;
        if (dateA < dateB) {
          return -1;
        } 
        if (dateA > dateB) { 
          return 1;
        }
        return 0;
      })
      console.log("111111");
      console.log(sortedItems);
      return sortedItems;
    }

  },

  created() {
    console.log("created");
    this.sortDate(this.items);
  } 
  
}
</script>
