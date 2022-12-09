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
            @contextmenu:day="showAddEvent"
            @contextmenu:time="showAddEvent"
            @change="updateRange"
            ></v-calendar>
            <template v-if="selectedEvent">
            <v-menu
            v-model="selectedOpen"
            :close-on-content-click="false"
            :activator="selectedElement"
            offset-x
            >
            <profile-card :key="selectedEvent.details.id" :initial-data="selectedEvent.details" :classnames="classnames"
              :color="selectedEvent.color" @close="closeCard" @submitted="submitted" @delete="deleteevent"/>
            </v-menu></template>
            <template v-if="createNew">
              <v-menu
                v-model="createNew"
                :close-on-content-click="false"
                :position-x="x"
                :position-y="y"
                absolute
                offset-x
              >
            <profile-edit-dialog :key="('createNew_'+createNewCount)" :initial-data="newevent" :classnames="classnames" :show-delete="false" @submitted="addEvent"/>
            </v-menu>
            </template>
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
      createNew: false,
      createNewCount: 0,
      newevent: null,
      x:0,
      y:0,
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      calendardata: [],
      classnames: {},
      username: ''
    }),
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      clickTime ({date,time }){
        console.log(date, time)
      },
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
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
      closeCard () {
        this.selectedOpen = false
        this.selectedEvent = null
      },
      showAddEvent({ date, time, hasTime }, e) {
          const date_suffix = hasTime ? `T${time}` : "T00:00"
          this.x = e.clientX
          this.y = e.clientY
          this.newevent = (()=>{
            return {
            name: "",
            id: "newcreated_"+this.createNewCount,
            classroom: "",
            teacher: "",
            links: [],
            tasks: [],
            starttime: date+date_suffix ,
            endtime: date+date_suffix
          }})()
          this.createNewCount ++
          this.createNew = true
      },
      addEvent(newevent) {
        newevent.id = this.classnames[newevent.name] + "-" + newevent.id
        axios.post("/api/newCalenderDetail", newevent)
        this.calendardata.push(newevent)
        this.createNew = false
        this.updateRange({start: 0, end: 0})
        this.$forceUpdate()
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
      deleteevent: function(e){
        axios.delete("/api/deleteCalenderDetail/" + e.id)
        for(let i = 0; i < this.calendardata.length; i++){
          let elem = this.calendardata[i]
          if (elem.id != e.id) {continue}
          this.calendardata.splice(i, 1)
          break
        }
        this.updateRange({start: 0, end: 0})
        this.$forceUpdate()
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
      this.calendardata.forEach(e=>{
        this.classnames[e.name] = e.id.split("-")[0]
      })
      const binded = this
      const username = this.username
      setInterval(
        function() {
          axios.get('/api/getCalender/' + username).then(e=>{
              binded.calendardata.splice(0, binded.calendardata.length)
              binded.calendardata.push(...e.data.calendar)
              binded.updateRange({start: 0, end: 0})
              binded.$forceUpdate()
          })
        }, 2500
      )
    },
    async asyncData () {
      const params = new URL(location.href).searchParams
      let user = "all"
      if (params.has("id")){
        user = params.get("id")
      }
      console.log()
      const data = await axios.get('/api/getCalender/' + user)
      return {calendardata: data.data.calendar, username: user}
    }
  }
</script>

<style>
.v-application .grey.lighten-4 {
    background-color: #333333 !important;
    border-color: #ffffff !important;
}
.v-menu__content {
  background-color: #4e4e4e !important;
}
</style>