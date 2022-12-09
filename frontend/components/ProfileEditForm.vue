<template>
    <div v-if="form">
        <v-card-title>授業データ</v-card-title>
        <v-card-text>
        <v-form>
            <v-container>
                <div class="mb-2 text-subtitle-1 font-weight-bold">開始時間</div>
                <v-text-field
                    label=""
                    v-model="form.starttime"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">終了時間</div>
                <v-text-field
                    label=""
                    v-model="form.endtime"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">講義名</div>
                <v-text-field
                    label=""
                    v-model="form.name"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">教員</div>
                <v-text-field
                    label=""
                    v-model="form.teacher"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">教室</div>
                <v-text-field
                    label=""
                    v-model="form.classroom"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">
                    リンク
                    <v-btn
                        class="mx-2" fab dark small absolute right
                        @click="addnewlink"
                    >
                    <v-icon>mdi-plus</v-icon>
                    </v-btn>
                </div>
                <div v-for="(link, index) in form.links" :key="'edit_link_'+index">
                    <v-text-field
                        label=""
                        v-model="form.links[index]"
                        @blur="checkblank(form.links, index)"
                        v-if="(form.links[index]!=null)"
                    ></v-text-field>
                </div>
                <v-text-field
                    label=""
                    v-model="newlink"
                    @blur="checknewlink"
                    v-if="(newlink!=null)"
                ></v-text-field>
                <div class="mb-2 text-subtitle-1 font-weight-bold">
                    課題
                    <v-btn
                        class="mx-2" fab dark small absolute right
                        @click="addnewtask"
                    >
                    <v-icon>mdi-plus</v-icon>
                    </v-btn>
                </div>
                <div v-for="(task, index) in form.tasks" :key="'edit_task_'+index" v-if="(task!=null)">
                    <v-row no-gutters :key="'edit_task_'+index+'_row'" >
                    <v-text-field
                        label="課題名"
                        @blur="checktask(form.tasks, index)"
                        v-model="task.name"
                        :key="'edit_task_'+index+'_name'"
                    ></v-text-field>
                    <v-text-field
                        label="課題リンク"
                        @blur="checktask(form.tasks, index)"
                        v-model="task.link"
                        :key="'edit_task_'+index+'_link'"
                    ></v-text-field>
                    <v-row no-gutters :key="'edit_task_'+index+'_row2'" ></v-row>
                    <v-text-field
                        label="期限"
                        @blur="checktask(form.tasks, index)"
                        v-model="task.limitdate"
                        :key="'edit_task_'+index+'_limit'"
                    ></v-text-field>
                    </v-row>
                </div>
                <template v-if="(newtask!=null)">
                    <v-row no-gutters :key="'new_'+task_index+'_row'">
                    <v-text-field
                        label="課題名"
                        @blur="checknewtask"
                        v-model="newtask.name"
                        :key="'new_'+task_index+'_name'"
                    ></v-text-field>
                    <v-text-field
                        label="課題リンク"
                        @blur="checknewtask"
                        v-model="newtask.link"
                        :key="'new_'+task_index+'_link'"
                    ></v-text-field>
                    </v-row>
                    <v-row no-gutters :key="'new_'+task_index+'_row2'">
                    <v-text-field
                        @blur="checknewtask"
                        label="期限"
                        v-model="newtask.limitdate"
                        :key="'new_'+task_index+'_limit'"
                    ></v-text-field>
                    </v-row>
                </template>
            </v-container>
        </v-form>
        </v-card-text>
    </div>
</template>

<script>
export default {
    name: "ProfileEditForm",
    props: {
        value: Object
    },
    data: function(){
        return {
            form: null,
            newlink: null,
            newtask: null,
            task_index: 0,
        }
    },
    methods: {
        checkblank: function(listdata, index) {
            if (listdata[index] == "") {
                this.$set(listdata, index, null)
            }
        },
        addnewlink: function(){
            if (this.newlink == null){
                this.newlink = ""
            }
        },
        checknewlink: function(){
            if (this.newlink == ""){
                this.newlink = null
            } else if (this.newlink != "" && this.newlink != null){
                this.form.links.push(this.newlink)
                this.newlink = null
            }
        },
        isempty: function(emptyObj){
            return Object.values(emptyObj).every(e=>e=="")
        },
        addnewtask: function(){
            if (this.newtask == null){
                this.task_index++
                this.newtask = (()=>{
                    return {
                    name: "",
                    link: "",
                    limitdate: ""
                }})()
            }
        },
        checktask: function(listdata, index){
            if (this.isempty(listdata[index])) {
                this.$set(listdata, index, null)
            }
        },
        checknewtask: function(){
            if (!this.isempty(this.newtask)){
                this.form.tasks.push(this.newtask)
            }
            this.newtask = null
        },
    },
    created: function() {
        this.form = this.value
    },
}
</script>