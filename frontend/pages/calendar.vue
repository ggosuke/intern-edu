<template>
    <div>
        <v-row class="fill-height">
        <v-col>
        <v-sheet height="64">
            <v-toolbar
            flat
            >
            <v-btn
                outlined
                class="mr-4"
                color="grey darken-2"
                @click="setToday"
            >
                Today
            </v-btn>
            <v-btn
                fab
                text
                small
                color="grey darken-2"
                @click="prev"
            >
                <v-icon small>
                mdi-chevron-left
                </v-icon>
            </v-btn>
            <v-btn
                fab
                text
                small
                color="grey darken-2"
                @click="next"
            >
                <v-icon small>
                mdi-chevron-right
                </v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar">
                {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-menu
                bottom
                right
            >
                <template v-slot:activator="{ on, attrs }">
                <v-btn
                    outlined
                    color="grey darken-2"
                    v-bind="attrs"
                    v-on="on"
                >
                    <span>{{ typeToLabel[type] }}</span>
                    <v-icon right>
                    mdi-menu-down
                    </v-icon>
                </v-btn>
                </template>
                <v-list>
                <v-list-item @click="type = 'week'">
                    <v-list-item-title>Week</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = 'month'">
                    <v-list-item-title>Month</v-list-item-title>
                </v-list-item>
                </v-list>
            </v-menu>
            </v-toolbar>
        </v-sheet>
        <v-sheet height="600">
            <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
            @click:more="viewWeek"
            @click:date="viewWeek"
            @change="updateRange"
            ></v-calendar>
            <template v-if="selectedEvent">
            <v-menu
            v-model="selectedOpen"
            :close-on-content-click="false"
            :activator="selectedElement"
            offset-x
            >
            <profile-card :key="selectedEvent.details.id" :initial-data="selectedEvent.details" 
              :color="selectedEvent.color" @close="closeCard" @submitted="submitted"/>
            </v-menu></template>
        </v-sheet>
        </v-col>
    </v-row>
    </div>
</template>
  
<script>
  import axios from 'axios'
  axios.defaults.baseURL = 'http://localhost';
  globalThis.calendar = []
  export default {
    data: () => ({
      focus: '',
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
      },
      selectedEvent: null,
      selectedElement: null,
      selectedOpen: false,
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      calendardata: []
    }),
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      viewWeek ({ date }) {
        this.focus = date
        this.type = 'week'
      },
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
        }
        if (this.selectedOpen) {
          this.selectedOpen = false
          this.selectedEvent = null
          requestAnimationFrame(() => requestAnimationFrame(() => open()))
        } else {
          open()
        }
        nativeEvent.stopPropagation()
      },
      closeCard () {
        this.selectedOpen = false
        this.selectedEvent = null
      },
      submitted (newevent){
        console.log(newevent.name)
        const bind_this = this
        axios.put("/api/putCalenderDetail/" + newevent.id, newevent).then(res =>{
          console.log(res)
          for (let i = 0; i < bind_this.calendardata.length; i++){
            let elem = bind_this.calendardata[i]
            if (elem.id != newevent.id){
              continue
            }
            bind_this.$set(bind_this.calendardata, i, newevent) 
          }
          this.updateRange({start: 0, end: 0})
          this.$forceUpdate()
        }).catch(err=>{console.log(err)})
      },
      updateRange ({ start, end }) {
        const events = []
        this.calendardata.forEach((e)=>{
          events.push({
            name: e.name,
            start: e.starttime,
            end: e.endtime,
            color: "blue",
            timed: true,
            details: e
          })
        }, this)
        this.events = events
      },
    },
    created: function(){
      console.log(JSON.parse(JSON.stringify(this.calendardata)))
    },
    async asyncData () {
      const data = await axios.get('/api/getCalender')
      return {calendardata: data.data.calendar}
    }
  }
</script>

<style>
.v-application .grey.lighten-4 {
    background-color: #333333 !important;
    border-color: #ffffff !important;
}

</style>