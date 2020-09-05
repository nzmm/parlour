<script lang="ts">
    import Button from "./Button.svelte";

    export let glyphName: string;
    export let title: string = "";
    export let active: boolean = false;
</script>

<button {title} class="btn" class:active on:click>
    <i class="{glyphName}"></i>
    <slot/>
</button>

<style>
    button {
        position: relative;
    }
</style>
