<template>
  <div>
    <div class="d-flex justify-content-center align-items-center">
      <h1>{{routine.name}}</h1>

      <i v-if="!routine.is_private"
           class="bi bi-eye-fill ms-2 h2"
           data-bs-toggle="tooltip"
           data-bs-placement="right"
           title="Public routine"
           v-tooltip></i>

      <i v-else
          class="bi bi-eye-slash-fill ms-2 h2"
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          title="Private routine"
          v-tooltip></i>
    </div>

    <p>By: {{routine.user.username}}</p>
    <div class="bg-light d-inline-block p-2">
      <span class="badge bg-dark ms-1" v-for="category in routine.categories" :key="category.id">{{category.name}}</span>
    </div>
  </div>

  <WorkoutCard v-for="userWorkout in routine.user_workouts" :key="userWorkout.id"
               @deletedWorkoutEmit="fetchRoutineData"
               :setEditWorkoutWindowCurrentWorkout="setEditWorkoutWindowCurrentWorkout"
               :setConfirmWindow="setConfirmWindow"
               :workout="userWorkout" 
               :isOwner="isOwner" />

  <div class="mt-4 d-flex justify-content-center">
    <div class="ms-1" v-if="isOwner">
      <i class="pointerButton bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click="toggleCreateWorkoutWindow"></i>
    </div>
    <div class="ms-1" v-if="isOwner">
      <i class="pointerButton bi bi-gear-fill ms-2" style="font-size: 40px" @click="toggleEditRoutineWindow"></i>
    </div>
    <i class="pointerButton bi bi-trash-fill ms-2" style="font-size: 40px; color: red;" @click="destroyRoutine"></i>
  </div>

  <CreateWorkoutWindow v-if="showCreateWorkoutWindow" 
                        :routineId="routine.id"
                        :setConfirmWindow="setConfirmWindow"
                        @createWorkoutEmit="fetchRoutineData"
                        @closeWindowEmit="toggleCreateWorkoutWindow" />

  <EditWorkoutWindow v-if="editWorkoutWindow.showWindow"
                        @editWorkoutEmit="fetchRoutineData"
                        @closeWindowEmit="toggleEditWorkoutWindow"
                        :userWorkoutId="editWorkoutWindow.currentWorkout.id"
                        :currentWorkoutName="editWorkoutWindow.currentWorkout.name"
                        :currentUserExercises="editWorkoutWindow.currentWorkout.user_exercises"
                        :setConfirmWindow="setConfirmWindow" />

  <EditRoutineWindow v-if="editRoutineWindow.showWindow"
                     :routine="routine"
                     :setConfirmWindow="setConfirmWindow"
                     @closeWindowEmit="toggleEditRoutineWindow" 
                     @updateRoutineEmit="fetchRoutineData"/>

  <ConfirmWindow v-if="confirmWindow.showWindow"
                :title="confirmWindow.title"
                :bodyText="confirmWindow.bodyText"
                :buttonText="confirmWindow.buttonText"
                :callback="confirmWindow.callback"
                :closeWindow="() => {confirmWindow.showWindow = false}" />

</template>

<script>
import axios from 'axios'
import WorkoutCard from '@/components/WorkoutCard'
import CreateWorkoutWindow from '@/components/CreateWorkoutWindow'
import EditWorkoutWindow from '@/components/EditWorkoutWindow'
import EditRoutineWindow from '@/components/EditRoutineWindow'
import ConfirmWindow from '@/components/ConfirmWindow'
import jwt_decode from "jwt-decode";

export default {
  name: 'Routine',
  components: {
    WorkoutCard, CreateWorkoutWindow, EditWorkoutWindow, EditRoutineWindow, ConfirmWindow
  },
  data () {
      return {
        routine: {
          id: 0,
          user: {
            username: "",
            id: 1
          },
          user_workouts: []
        },
        isOwner: false,
        showCreateWorkoutWindow: false,
        editWorkoutWindow: {
          showWindow: false,
          currentWorkout: {}
        },
        confirmWindow: {
          showWindow: false,
          title: "",
          bodyText: "",
          buttonText: "",
          callback: undefined
        },
        editRoutineWindow: {
          showWindow: false
        }
      }
  },
  mounted() {
      this.fetchRoutineData()
      this.isRoutineOwner()
  },
  methods: {
    async fetchRoutineData() {
      this.$root.toggleIsLoading(true)

      await axios.get(`/api/public/routines/${this.$route.params.id}`)
          .then((response) => {
            this.routine = response.data
          })
      this.$root.toggleIsLoading(false)
    },
    isRoutineOwner() {
      if (this.$store.state.isAuthenticated) {
        let authenticatedUser = jwt_decode(this.$store.state.accessToken)
        this.isOwner = authenticatedUser.user_id === this.routine.user.id
      }
    },
    toggleCreateWorkoutWindow() {
      this.showCreateWorkoutWindow = !this.showCreateWorkoutWindow
    },
    toggleEditWorkoutWindow() {
      this.editWorkoutWindow.showWindow = !this.editWorkoutWindow.showWindow
    },
    toggleEditRoutineWindow() {
      this.editRoutineWindow.showWindow = !this.editRoutineWindow.showWindow
    },
    destroyRoutine() {
      const deleteRoutineCallback = (answer) => {
        this.$root.toggleIsModalOpen(false)
          if(answer){
            axios.delete('/api/dashboard/routines/delete', { data: {
              routineId: this.routine.id
            }})
            .then((response) => {
                window.location.replace("/dashboard/routines")
            })
          }
        }

      this.setConfirmWindow("Delete Routine?", 
                              "Once a routine is deleted it cannot be recovered." + 
                              "Are you sure you'd like to delete this routine",
                              "Confirm Deletion", deleteRoutineCallback)
    },
    setEditWorkoutWindowCurrentWorkout(workout) {
      this.editWorkoutWindow.currentWorkout = workout
      this.toggleEditWorkoutWindow()
    },
    setConfirmWindow(title, bodyText, buttonText, callback) {
      this.confirmWindow.title = title
      this.confirmWindow.bodyText = bodyText
      this.confirmWindow.buttonText = buttonText
      this.confirmWindow.callback = callback
      this.confirmWindow.showWindow = true
      this.$root.toggleIsModalOpen(true)
    }
  }
}
</script>