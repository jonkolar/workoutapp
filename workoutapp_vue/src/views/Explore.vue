<template>
    <div class="container">
        <div class="row height d-flex justify-content-center align-items-center">
            <div class="col-md-8">
                <div class="search"><input type="text" class="form-control" placeholder="Search for a routine..."> 
                    <button class="btn btn-primary"><i class="bi bi-search"></i></button>
                </div>
                <div class="container-fluid d-flex justify-content-center flex-wrap mt-5">
                    <RoutineCard 
                    v-for="routine in userRoutines"
                    v-bind:key="routine.id"
                    v-bind:routine="routine" />
                </div>
            </div>
        </div>
        <button v-if="!all_shown" type="button" class="btn btn-primary mt-5" @click="fetchUserRoutinesCurrentPage">Show More</button>
    </div>
</template>

<script>
import axios from 'axios'
import RoutineCard from '@/components/RoutineCard'

export default {
    name: 'Explore',
    components: {
        RoutineCard
    },
    data () {
        return {
            userRoutines: [],
            currentPage: 0,
            all_shown: false
        }
    },
    mounted() {
        this.$root.toggleIsLoading(true)

        this.fetchUserRoutinesCurrentPage()

        this.$root.toggleIsLoading(false)
    },
    methods: {
        async fetchUserRoutinesCurrentPage() {
            this.currentPage++
            await axios.get(`/api/public/routines/all/${this.currentPage}`)
            .then((response) => {
                let routines = response.data['routines']
                for(let i = 0; i < routines.length; i++){
                    this.userRoutines.push(routines[i])
                }
                if (!response.data['has_more']) { this.all_shown = true }
            })
        },
    }
}
</script>

<style scoped>
.search {
    position: relative;
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
    box-shadow: 0 0 40px rgba(51, 51, 51, .1)
}

.search input {
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
    font-size: 1.5rem;
    height: 60px;
    border: 2px solid #d6d4d4
}

.search input:focus {
    box-shadow: none;
    border: 2px solid blue
}

.search button {
    border-radius: 50%;
    position: absolute;
    top: 5px;
    right: 6px;
    height: 50px;
    width: 50px;
    background: blue
}


</style>