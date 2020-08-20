<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { currentTrack } from '../core/store';
    import type { ITrack } from "../core/interfaces/ITrack";

    import ScrolledView from "./common/ScrolledView.svelte";

    export let heading = "";
    export let subheading = "";
    export let data: ITrack[] = [];

    const dispatch = createEventDispatcher();

    $: currentId = $currentTrack.id;
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

    <div class="list px-2 py-4">
        {#each data as item}
        <button class="item d-flex py-2 {item.id === currentId ? 'playing' : ''}" on:dblclick={() => dispatch('rowDblClick', item)}>
            <div class="p-col number">
                {item.number}
            </div>
            <div class="p-col name">
                {#if item.id === currentId}
                    <i class="fas fa-play pr-1"></i>
                {/if}
                {item.name}
            </div>
            <div class="p-col artist">
                {item.artist_credit}
            </div>
            <div class="p-col release">
                {item.release_name}
            </div>
            <div class="p-col length">
                {item.length_display}
            </div>
        </button>
        {/each}
    </div>
</ScrolledView>

<style>
    h2 {
        padding-left: 24px;
        font-weight: bold;
    }
    h2 > small {
        font-size: 16px;
    }
    .item {
        width: 100%;
        margin: 0;
        padding-left: 24px;
        padding-right: 24px;
        text-align: left;
        background: transparent;
        border: 0;
        outline: 0;
        font-size: small;
    }
    .item.playing {
        font-weight: bold;
    }
    .item:nth-child(odd) {
        background-color: #eee;
    }
    .item:focus {
        background-color: #ff2a2aff;
        color: #fff;
    }
    .item > .p-col {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .item > .number {
        width: 42px;
        text-align: center;
        color: #6c757d;
    }
    .item:focus > .number {
        color: #fff;
    }
    .item > .name {
        flex-grow: 1;
    }
    .item > .artist {
        width: 27%;
    }
    .item > .release {
        width: 27%;
    }
    .item > .length {
        text-align: right;
        width: 56px;
    }
</style>