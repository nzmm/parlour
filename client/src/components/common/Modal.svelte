<script lang="ts">
    import { createEventDispatcher, onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    import { registerGlobalKeyUpHandler } from "../../core/keys";
    import BoxDropshadow from "./BoxDropshadow.svelte";
    import Button from "./Button.svelte";

    export let title: string = "Modal";
    let ref: HTMLDivElement;

    const dispatch = createEventDispatcher();

    onMount(() => {
        document.body.appendChild(ref);
        return registerGlobalKeyUpHandler("Escape", () => dispatch("close"));
    });
</script>

<div
    bind:this={ref}
    transition:fade={{ duration: 150 }}
    class="p-modal-bg d-flex justify-content-center align-items-center"
    on:click|stopPropagation|preventDefault={() => null}>

    <BoxDropshadow>
        <div class="p-modal-dialog d-flex flex-column justify-content-between">
            <header class="border-bottom">
                <h3>{title}</h3>
                <button class="close" on:click|preventDefault={() => dispatch("close")} aria-label="Close">
                    <i class="fas fa-times"></i>
                </button>
            </header>

            <div class="p-modal-body">
                <slot />
            </div>

            <footer class="border-top d-flex justify-content-end align-items-center">
                <slot name="footer">
                    <Button
                        primary
                        ariaLabel="Close"
                        on:click={() => dispatch("close")}>
                        Close
                    </Button>
                </slot>
            </footer>
        </div>
    </BoxDropshadow>
</div>

<style type="text/scss">
    @import "../../scss/vars";

    .p-modal-bg {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 1500;
        background-color: rgba(0, 0, 0, .3);
        backdrop-filter: grayscale(60%);
    }
    .p-modal-dialog {
        min-height: 300px;
        max-height: 80vh;
        width: 800px;
        border-radius: 4px;
        background-color: $colour-grey;
    }
    .p-modal-body {
        padding: 15px;
        flex-grow: 1;
    }
    header {
        position: relative;
        text-align: center;
        padding: 15px;
        margin: 0;
    }
    footer {
        padding: 10px;
        padding-left: 15px;
        padding-right: 15px;
    }
    h3 {
        font-size: 16px;
        font-weight: bold;
        margin: 0;
    }
    .close {
        position: absolute;
        right: 15px;
        top: 15px;
        font-size: 16px;
        line-height: 19px;
        outline: 0;
    }
</style>
