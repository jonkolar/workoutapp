<template>
  <div id="confirm-window" class="bg-dark text-light rounded">
    <div id="confirm-window-content" class="d-flex flex-column align-items-center m-3">
        <h4>{{ title }}</h4>
        <p>{{ bodyText }}</p>
        <div class="d-flex justify-content-center">
            <button class="btn btn-success m-1" @click="confirm">{{ buttonText }}</button>
            <button class="btn btn-danger m-1" @click="cancel">Cancel</button>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ConfirmWindow',
    props: ['buttonText', 'title', 'bodyText', 'closeWindow', 'callback'],
    methods: {
        confirm() {
            this.callback(true)
            this.closeWindow()
        },
        cancel() {
            this.callback(false)
            this.closeWindow()
        }
    }
}
</script>

<style>
#confirm-window {
  z-index: 2000;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; 
}
</style>