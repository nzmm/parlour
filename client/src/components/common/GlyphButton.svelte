<script lang="ts">
    import Button from "./Button.svelte";

    export let glyphName: string;
    export let title: string = "";
</script>

<Button on:click bind:title >
    <i class="{glyphName}"></i>
</Button>

<style>
    :global(button) {
        padding: 1px 6px;
        margin: 3px;
        margin-top: 0;
    }
</style>
