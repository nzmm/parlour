<script lang="ts">
    import DropdownMenu from './DropdownMenu.svelte';

    export let matches = [];

    let value = '';
    let focus = false;

    $: visible = focus && value.length > 0 && matches.length > 0;
</script>

<div class="p-search mx-1">
    <input
        type="text"
        class="form-control pr-4"
        bind:value={value}
        on:focus={() => focus = true}
        on:blur={() => focus = false}
        on:input />

    {#if value}
    <a class="clear" href="#search" on:click={() => value = ""}>
        <i class="pr-2 fas fa-times"></i>
    </a>
    {:else}
    <i class="pr-2 fas fa-search"></i>
    {/if}

    <DropdownMenu
        {visible}
        dropshadowSize={"small"}
        on:hide={() => focus = false}>

        {#each matches as match}
        <a class="dropdown-item" href="#match">
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
        opacity: .3;
    }
    i::before {
        vertical-align: -65%;
    }
</style>