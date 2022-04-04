<template>
    <div class="container">
        <div class="row height d-flex justify-content-center align-items-center">
            <div class="col-md-8">
                <div class="search"><input type="text" class="form-control" placeholder="Search for a routine..."> 
                    <button class="btn btn-primary"><i class="bi bi-search"></i></button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Explore',
  components: {
    data () {
      return {

      }
    }
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