<script lang="ts">
    import ScrolledView from './ScrolledView.svelte';

    export let root: HTMLElement = null;
    export let wide: boolean = false;
    export let active: boolean = true;
</script>

<ScrolledView overflowX="hidden" overflowY="scroll" class={active ? "" : "p-page-inactive"} bind:root>
    <div class="wrapper mx-2" class:wide>
        <slot />
    </div>
</ScrolledView>

<style>
    .wrapper:not(.wide) {
        padding: 24px;
    }
</style>