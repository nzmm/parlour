<script lang="ts">
    import BoxDropshadow from "./BoxDropshadow.svelte";
    import type { DropshadowSize } from "./enums/DropshadowSize";

    export let delayMs: number = 250;
    export let dropshadowSize: DropshadowSize = "big";

    let visible = false;
    let top: number = 0;
    let left: number = 0;

    const showDropdown = (event: MouseEvent) => {
        const element = event.currentTarget as HTMLElement;
        const rect = element.getBoundingClientRect();

        visible = true;
        top = rect.top + rect.height - 5;
        left = rect.left;
    };

    const hideWithDelay = () => setTimeout(() => visible = false, delayMs);
</script>

<div class="p-drop">
    <div class="p-drop-toggle" on:click={showDropdown}>
        <slot name="toggle">
            <i class="fas fa-caret-down p-2"></i>
        </slot>
    </div>

    {#if visible}
    <BoxDropshadow size={dropshadowSize}>
        <div class="p-drop-bg" on:click|stopPropagation={() => visible = false}></div>

        <div class="p-drop-menu py-2" style="top: {top}px; left: {left}px;" on:click={hideWithDelay} >
            <slot />
        </div>
    </BoxDropshadow>
    {/if}
</div>

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