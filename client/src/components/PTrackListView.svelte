<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { currentTrack } from '../core/store';
    import type { ITrack } from "../core/interfaces/ITrack";

    import ScrolledView from "./common/ScrolledView.svelte";
    import Dropdown from './common/Dropdown.svelte';

    export let heading = "";
    export let subheading = "";
    export let data: ITrack[] = [];
    export let withQueueActions: boolean = false;

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
        <div class="item d-flex py-2 {item.id === currentId ? 'playing' : ''}" tabindex="0" on:dblclick={() => dispatch('play', item)}>
            <div class="p-col playing">
                {#if item.id === currentId}
                    <i class="fas fa-play pr-1"></i>
                {/if}
            </div>
            <div class="p-col liked">
                {#if item.liked}
                    <i class="fas fa-heart"></i>
                {/if}
            </div>
            <div class="p-col number">
                {item.number}
            </div>
            <div class="p-col name">
                {item.name}
            </div>
            <div class="p-col meatballs">
                <Dropdown>
                    <big slot="toggle">
                        <i class="fas fa-ellipsis-h"></i>
                    </big>

                    <a class="dropdown-item" href="#play" on:click|preventDefault={() => dispatch('play', item)}>
                        Play
                    </a>

                    <div class="dropdown-divider"></div>

                    {#if withQueueActions}
                    <a class="dropdown-item" href="#enqueue">
                        Add to queue
                    </a>
                    <a class="dropdown-item" href="#next">
                        Play next
                    </a>

                    <div class="dropdown-divider"></div>
                    {/if}

                    <a class="dropdown-item" href="#like">
                        Like
                    </a>
                </Dropdown>
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
        </div>
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
        height: 37px;
        margin: 0;
        padding-right: 24px;
        text-align: left;
        background: transparent;
        border: 0;
        outline: 0;
        font-size: 14px;
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
    .item > .playing {
        width: 24px;
        text-align: right;
    }
    .item > .liked {
        width: 24px;
        text-align: right;
    }
    .item > .number {
        width: 42px;
        text-align: center;
    }
    .item i {
        color: #6c757d;
    }
    .item.playing i {
        color: #212529;
    }
    .item:focus i,
    .item.playing:focus i {
        color: #fff;
    }
    .item > .name {
        flex-grow: 1;
    }
    .item > .meatballs {
        width: 32px;
    }
    .item > .meatballs i {
        opacity: 0;
        transition: opacity .3s;
    }
    .item:hover > .meatballs i {
        opacity: 1;
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