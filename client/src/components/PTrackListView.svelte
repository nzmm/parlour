<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    import type { ITrack } from "../core/interfaces/ITrack";
    import ScrolledView from "./common/ScrolledView.svelte";

    export let heading = "";
    export let subheading = "";
    export let data = [];

    const dispatch = createEventDispatcher();

    function onDblClick(item: ITrack) {
		dispatch('rowDblClick', item);
	}
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
        <button class="item d-flex py-2" on:dblclick={() => onDblClick(item)}>
            <div class="number">
                {item.number}
            </div>
            <div class="name">
                {#if item.playing}
                    <i class="fas fa-play pr-1"></i>
                {/if}
                {item.name}
            </div>
            <div class="length">
                {item.length_display}
            </div>
            <div class="artist">
                {item.artist_credit}
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
    .item:nth-child(odd) {
        background-color: #eee;
    }
    .item:focus {
        background-color: #ff2a2aff;
        color: #fff;
    }
    .item > .number {
        width: 32px;
        text-align: center;
    }
    .item > .name {
        width: 30%;
    }
    .item > .length {
        width: 50px;
    }
    .item > .artist {
        width: 30%;
    }
</style>