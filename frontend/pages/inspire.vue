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
                  >
                  <v-card-title class="text-h5">
                    課題名
                  </v-card-title>

                  <div class="text-center">
                    <v-chip
                      class="ma-2"
                      color="red"
                      text-color="white"
                    >
                      授業名
                    </v-chip>

                    <v-chip
                      class="ma-2"
                      color="green"
                      text-color="white"
                    >
                      期日
                    </v-chip>
                  </div>
                  
                  <v-card-subtitle
                    class ="text-center" >

                  
                    課題内容xxxxxxxxxxxxxxxxx
                  </v-card-subtitle>

                  <v-card-actions >
                    <v-col class ="text-right">
                      <v-btn>
                        完了
                      </v-btn>
                    </v-col>
                  </v-card-actions>
                </v-card>

                <v-col>
                </v-col>

                <v-card
                  color="#385F73"
                  dark
                  >
                  <v-card-title class="text-h5">
                    課題名
                  </v-card-title>

                  <div class="text-center">
                    <v-chip
                      class="ma-2"
                      color="red"
                      text-color="white"
                    >
                      授業名
                    </v-chip>

                    <v-chip
                      class="ma-2"
                      color="green"
                      text-color="white"
                    >
                      期日
                    </v-chip>
                  </div>
                  
                  <v-card-subtitle
                    class ="text-center" >

                  
                    課題内容xxxxxxxxxxxxxxxxx
                  </v-card-subtitle>

                  <v-card-actions >
                    <v-col class ="text-right">
                      <v-btn>
                        完了
                      </v-btn>
                    </v-col>
                  </v-card-actions>
                </v-card>

                <v-col>
                </v-col>

                <v-card
                  color="#385F73"
                  dark
                  >
                  <v-card-title class="text-h5">
                    課題名
                  </v-card-title>

                  <div class="text-center">
                    <v-chip
                      class="ma-2"
                      color="red"
                      text-color="white"
                    >
                      授業名
                    </v-chip>

                    <v-chip
                      class="ma-2"
                      color="green"
                      text-color="white"
                    >
                      期日
                    </v-chip>
                  </div>
                  
                  <v-card-subtitle
                    class ="text-center" >

                  
                    課題内容xxxxxxxxxxxxxxxxx
                  </v-card-subtitle>

                  <v-card-actions >
                    <v-col class ="text-right">
                      <v-btn>
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
      items: []
    }
  },
  // 通信で取得するデータ

}
</script>
