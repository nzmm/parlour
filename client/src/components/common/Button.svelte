<script lang="ts">
    let className = "";

    export { className as class };
    export let title: string = "";
    export let primary: boolean = false;
    export let narrow: boolean = false;
</script>

<button class="btn {className}" class:primary class:narrow {title} on:click>
    <slot/>
</button>

<style type="text/scss">
    @import "../../scss/vars";

    .primary {
        background-color: $colour-primary;
        color: $colour-white;
        border: 1px solid darken($colour-primary, 20%)
    }
    .primary:hover {
        background-color: lighten($colour-primary, 10%);
    }
    .primary:active {
        background-color: darken($colour-primary, 15%);
    }
    .narrow {
        font-size: 15px;
        padding-top: 2px;
        padding-bottom: 2px;
        padding-left: 18px;
        padding-right: 18px;
    }
</style>