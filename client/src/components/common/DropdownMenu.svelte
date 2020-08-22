<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    import BoxDropshadow from "./BoxDropshadow.svelte";
    import type { DropshadowSize } from "./enums/DropshadowSize";

    export let visible: boolean = false;
    export let top: number = null;
    export let left: number = null;
    export let dropshadowSize: DropshadowSize = "big";

    const dispatch = createEventDispatcher();
</script>

{#if visible}
<div class="p-drop-bg" on:click|stopPropagation={() => dispatch("hide")}></div>

<BoxDropshadow size={dropshadowSize}>
    <div
        class="p-drop-menu py-2"
        style="{top == null ? '' : `top: ${top}px;`}{left == null ? '' : `left: ${left}px;`}"
        on:click={() => dispatch("hide")}>
        <slot />
    </div>
</BoxDropshadow>
{/if}

<style>
    .p-drop-bg {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 1500;
    }
    .p-drop-menu {
        position: absolute;
        min-width: 200px;
        min-height: 50px;
        color: #000;
        background-color: #fff;
        border: 1px solid #a5a5a5;
        z-index: 1501;
        border-radius: 4px;
        overflow: hidden;
    }
    .p-drop-menu :global(.dropdown-item:hover) {
        background-color: #ff2a2aff;
        color: #fff;
    }
    .p-drop-menu :global(.dropdown-item:active) {
        background-color: #fff;
        color: #000;
    }
</style>
