<script lang="ts">
    let className = "";

    export { className as class };
    export let ariaLabel: string;
    export let title: string = "";
    export let disabled: boolean = false;
    export let primary: boolean = false;
    export let narrow: boolean = false;
</script>

<button
    class="btn
    {className}"
    class:primary
    class:narrow
    {title}
    {disabled}
    on:click
    aria-label={ariaLabel}>
    <slot/>
</button>

<style type="text/scss">
    @import "../../scss/vars";

    .primary {
        background-color: $colour-primary;
        color: $colour-white;
        border: 1px solid darken($colour-primary, 20%)
    }
    .primary:hover:not(:disabled) {
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