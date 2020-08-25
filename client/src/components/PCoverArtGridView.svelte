<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { IAlbum } from "../core/interfaces/IAlbum";

    import Page from './common/Page.svelte';
    import PCoverArt from "./PCoverArt.svelte";

    export let heading = "";
    export let subheading = "";
    export let data: IAlbum[] = [];

    const dispatch = createEventDispatcher();

    let w: number;
    $: columnTemplate = "1fr ".repeat(Math.max(1, Math.floor(w / 200))).trimEnd();
</script>

<Page {heading} {subheading}>
    <section class="grid" bind:clientWidth={w} style="--col-template:{columnTemplate}">
        {#each data as item}
        <div class="item">
            <button class="btn" id="item-{item.id}" on:click={() => dispatch("details", item)}>
                <PCoverArt size="150px" src={item.thumbnail} />
            </button>
            <label for="item-{item.id}">
                <slot {item} name="label">
                    {item.name}
                </slot>
            </label>
        </div>
        {/each}
    </section>
</Page>

<style>
    .grid {
        width: 100%;
        display: grid;
        grid-template-columns: var(--col-template);
        grid-auto-rows: 230px;
        column-gap: 40px;
    }
    .grid > .item {
        line-height: 1;
        text-align: center;
        justify-self: center;
    }
    .grid > .item > button {
        padding: 2px;
    }
    .grid > .item > label {
        font-size: 14px;
    }
</style>