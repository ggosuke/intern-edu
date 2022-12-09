<template>
      <v-dialog v-model="editDialog" max-width="500" @click:outside="revert">
        <template v-slot:activator="{ on, attrs }">
          <v-btn text rounded v-bind="attrs" v-on="on">
            <v-icon>mdi-pencil</v-icon>
            編集
          </v-btn>
        </template>
        <v-card class="ma-auto pa-4">
          <profile-edit-form v-model="profile" :key="('edit_form_'+count)" />
          <v-card-actions>
            <v-btn color="primary" @click="submit">変更する</v-btn>
            <v-btn color="primary" @click="revert">元に戻す</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </template>

<script>

function clone(e){
    return JSON.parse(JSON.stringify(e))
}

export default {
    name: "ProfileEditDialog",
    props: {
        initialData : Object
    },
    data: function(){
        return {
            editDialog: false,
            profile: {},
            count: 0
        }
    },
    methods: {
        submit: function(){
            this.$emit("submitted", clone(this.profile))
            this.editDialog = false
        },
        revert: function() {
            this.profile = clone(this.initialData)
            this.count++
            this.$forceUpdate()
        }
    },
    created: function(){
        this.profile = clone(this.initialData)
    }
}

</script>