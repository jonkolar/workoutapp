<template>
  <div id="confirm-window" class="position-absolute top-50 start-50 translate-middle bg-dark text-light rounded">
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
    props: ['buttonText', 'title', 'bodyText', 'closeWindow', 'resolvePromise', 'rejectPromise'],
    methods: {
        confirm() {
            this.resolvePromise(true)
            this.closeWindow()
        },
        cancel() {
            this.resolvePromise(false)
            this.closeWindow()
        }
    }
}
</script>

<style>
#confirm-window {
  z-index: 2000;
}
</style>