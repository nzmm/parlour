<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { ITrack } from "../core/interfaces/ITrack";

    export let number: number | string;
    export let item: ITrack;
    export let current: boolean = false;
    export let playing: boolean = false;
    export let indexed: boolean = false;

    const dispatch = createEventDispatcher();

    const onContextMenu = (event: MouseEvent) => {
        dispatch("dropdown", { item, top: event.clientY, left: event.clientX });
    }
</script>

<tr
    id="track:{item.id}"
    class="item d-flex py-2"
    class:playing={current}
    class:indexed
    tabindex="0"
    on:dblclick={() => dispatch('play', item)}
    on:contextmenu|preventDefault={onContextMenu}>

    <td class="p-col number">
        {#if current}
            <i class="fas {playing ? 'fa-play' : 'fa-pause'} pr-1"></i>
        {:else}
            {number || '-'}
        {/if}
    </td>

    <td class="p-col liked">
        {#if item.liked}
            <i class="fas fa-heart"></i>
        {:else}
            <i class="far fa-heart"></i>
        {/if}
    </td>

    <td class="p-col name">
        {item.name}
    </td>

    <td class="p-col artist">
        {item.artist_credit || '-'}
    </td>

    <td class="p-col release">
        {item.release_name  || '-'}
    </td>

    <td class="p-col length">
        {item.length_display}
    </td>
</tr>

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
        cursor: default;
    }
    .item.playing {
        font-weight: bold;
    }
    .item.indexed > .number {
        font-style: italic;
    }
    .item:nth-child(odd) {
        background-color: #f2f2f2;
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
        width: 36px;
        padding-left: 5px;
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
