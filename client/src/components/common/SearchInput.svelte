<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import DropdownMenu from './DropdownMenu.svelte';

    export let matches = [];

    let value = '';
    let focus = false;

    let container: HTMLElement;
    let matchElements: HTMLElement[] = [];

    const dispatch = createEventDispatcher();

    $: visible = focus && value.length > 0 && matches.length > 0;

    const onKeyDown = (event: KeyboardEvent) => {
        if (!event.shiftKey && event.keyCode === 9) {
            event.preventDefault();
            matchElements[0].focus();
            return false;
        }
    }

    const onBlur = () => {
        setTimeout(() => {
            focus = container.contains(document.activeElement);
        }, 50);
    }

    const clear = () => {
        value = "";
        dispatch("clear");
    }
</script>

<div class="p-search" bind:this={container}>
    <input
        type="text"
        class="form-control pr-4"
        bind:value={value}
        on:focus={() => focus = true}
        on:blur={onBlur}
        on:keydown={onKeyDown}
        on:input />

    {#if value}
    <a class="clear" href="#search" on:click={clear} title="Clear">
        <i class="pr-2 fas fa-times"></i>
    </a>
    {:else}
    <i class="pr-2 fas fa-search"></i>
    {/if}

    <DropdownMenu
        {visible}
        interceptor={false}
        dropshadowSize="small"
        on:hide={() => focus = false}>

        {#each matches as match, i}
        <a tabindex="0"
            class="dropdown-item"
            href="#match"
            bind:this={matchElements[i]}
            on:blur={onBlur}>

            {match}
        </a>
        {/each}
    </DropdownMenu>
</div>

<style>
    .p-search {
        position: relative;
    }
    .p-search :global(.p-drop-menu) {
        top: 110%;
        width: 100%;
    }
    i {
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
    }
    i::before {
        vertical-align: -65%;
    }
</style>