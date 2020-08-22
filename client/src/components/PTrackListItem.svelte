<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ITrack } from "../core/interfaces/ITrack";

    import Dropdown from './common/Dropdown.svelte';

    export let item: ITrack;
    export let current: boolean = false;
    export let playing: boolean = false;
    export let withQueueActions: boolean = false;

    const dispatch = createEventDispatcher();
</script>

<div class="item d-flex py-2 {current ? 'playing' : ''}" tabindex="0" on:dblclick={() => dispatch('play', item)}>
    <div class="p-col number">
        {#if current}
            <i class="fas {playing ? 'fa-play' : 'fa-pause'} pr-1"></i>
        {:else}
            {item.number || '-'}
        {/if}
    </div>
    <div class="p-col liked">
        {#if item.liked}
            <i class="fas fa-heart"></i>
            {:else}
            <i class="far fa-heart"></i>
        {/if}
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
            <a class="dropdown-item" href="#enqueue" on:click|preventDefault={() => dispatch('enqueue', item)}>
                Add to queue
            </a>
            <a class="dropdown-item" href="#next" on:click|preventDefault={() => dispatch('enqueueNext', item)}>
                Play next
            </a>

            <div class="dropdown-divider"></div>
            {/if}

            <a class="dropdown-item" href="#like" on:click|preventDefault={() => dispatch("liked", item)}>
                Like
            </a>
        </Dropdown>
    </div>
    <div class="p-col artist">
        {item.artist_credit || '-'}
    </div>
    <div class="p-col release">
        {item.release_name  || '-'}
    </div>
    <div class="p-col length">
        {item.length_display}
    </div>
</div>

<style>
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
    .item > .liked {
        width: 28px;
        text-align: left;
    }
    .item > .number {
        width: 48px;
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
