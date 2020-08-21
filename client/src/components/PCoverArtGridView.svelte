<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { IAlbum } from "../core/interfaces/IAlbum";

    import ScrolledView from "./common/ScrolledView.svelte";
    import PCoverArt from "./PCoverArt.svelte";

    export let heading = "";
    export let subheading = "";
    export let data: IAlbum[] = [];

    const dispatch = createEventDispatcher();

    let w: number;
    $: columnTemplate = "1fr ".repeat(Math.max(1, Math.floor(w / 180))).trimEnd();
</script>

<ScrolledView overflowX="hidden" overflowY="scroll">
    <header class="px-2 pt-5">
        <h2>
            {heading}

            <small class="text-muted">
                {subheading}
            </small>
        </h2>
    </header>

    <div class="grid py-4 px-2" bind:clientWidth={w} style="--col-template:{columnTemplate}">
        {#each data as item}
        <div class="item">
            <button class="btn" on:click={() => dispatch("details", item)}>
                <PCoverArt size="120px" src={item.thumbnail} />
            </button>
            <div>
                <small>{item.name}</small>
            </div>
        </div>
        {/each}
    </div>
</ScrolledView>

<style>
    .grid {
        width: 100%;
        display: grid;
        grid-template-columns: var(--col-template);
        grid-auto-rows: 180px;
        column-gap: 15px;
    }
    .grid > .item {
        line-height: 1;
        text-align: center;
        justify-self: center;
    }
    .grid > .item > button {
        padding: 2px;
    }
    h2 {
        padding-left: 24px;
        font-weight: bold;
    }
    h2 > small {
        font-size: 16px;
    }
</style>