<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { intersectionObservable } from "../core/observable";
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import Page from './common/Page.svelte';
    import PCoverArt from "./PCoverArt.svelte";

    let className = "";

    export { className as class };
    export let context: string;
    export let data: IAlbum[] = [];

    const dispatch = createEventDispatcher();

    let root: HTMLElement;
    let loaded: Record<string, boolean> = {};
    let w: number;

    $: columnTemplate = "1fr ".repeat(Math.max(1, Math.floor(w / 200))).trimEnd();

    $: if (data?.length) {
        intersectionObservable(
            root,
            ".cover",
            data,
            (e: HTMLElement) => { loaded[e.dataset.itemid] = true; });
    }

</script>

<Page bind:root>
    <section class="grid {className}" bind:clientWidth={w} style="--col-template:{columnTemplate}">
        {#each data as item}
        <div class="cover" data-itemid={item.id}>
            <button class="btn" id={`${context}-${item.id}`} on:click={() => dispatch("details", item)}>
                <PCoverArt size="150px" src={loaded[item.id] ? item.thumbnail : ''} />
            </button>
            <label class="pt-1" for="item-{item.id}">
                <slot {item} name="label">
                    {item.name || '-'}
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
    .cover {
        line-height: 1;
        text-align: center;
        justify-self: center;
    }
    .cover > button {
        padding: 2px;
    }
    .cover > label {
        display: block;
        font-size: 14px;
    }
</style>