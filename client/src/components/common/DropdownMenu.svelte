<script lang="ts">
    import { createEventDispatcher, onMount } from 'svelte';
    import { registerGlobalKeyUpHandler } from '../../core/keys';
    import BoxDropshadow from "./BoxDropshadow.svelte";
    import type { DropshadowSize } from "./enums/DropshadowSize";

    export let visible: boolean = false;
    export let top: number | string = null;
    export let left: number | string = null;
    export let dropshadowSize: DropshadowSize = "big";
    export let interceptor: boolean = true;

    let deregister: () => void;
    const dispatch = createEventDispatcher();

    const onClick = (event: MouseEvent) => {
        if ((event.target as HTMLElement).classList.contains("p-submenu-item")) {
            return;
        }

        dispatch("hide");
    }

    $: if (top >= 0 && left >= 0) {
        if (visible) {
            deregister = registerGlobalKeyUpHandler("Escape", () => dispatch("hide"));
        } else {
            deregister?.();
        }
    }

    $: style = `${top == null ? '' : `top: ${typeof top === 'number' ? `${top}px` : top};`}` +
               `${left == null ? '' : `left: ${typeof left === 'number' ? `${left}px` : left};`}`;
</script>

{#if visible}
{#if interceptor}
<div class="p-drop-bg" on:click|stopPropagation={() => dispatch("hide")}></div>
{/if}

<BoxDropshadow size={dropshadowSize}>
    <div
        class="p-drop-menu py-2"
        {style}
        on:click={onClick}>
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
        min-height: 30px;
        color: #000;
        background-color: #fff;
        border: 1px solid #a5a5a5;
        z-index: 1501;
        border-radius: 4px;
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
