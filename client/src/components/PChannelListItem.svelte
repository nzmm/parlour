<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { IChannelTrack } from "../core/interfaces/IChannelTrack";
    import TextDropshadow from "./common/TextDropshadow.svelte";
import PCoverArt from './PCoverArt.svelte';

    export let item: IChannelTrack;
    export let current: boolean = false;
    //export let playing: boolean = false;

    const dispatch = createEventDispatcher();

    const onContextMenu = (event: MouseEvent) => {
        dispatch("dropdown", { item, top: event.clientY, left: event.clientX });
    }
</script>

<div
    id="track:{item.track_id}"
    class="item d-flex py-2"
    class:playing={current}
    tabindex="0"
    on:dblclick={() => dispatch('play', item)}
    on:contextmenu|preventDefault={onContextMenu}>

    <PCoverArt size="78px" src={item.track_thumbnail} />

    <h4 class="pl-4 pt-2">
        <strong>{item.track_name}</strong>

        <p>
            <small>
                {item.track_release_name || '?'}<br/>
                {item.track_artist_credit || '?'} &middot; {item.track_year || '?'}
            </small>
        </p>
    </h4>

    <!--
    <div class="name">
        {item.track_name}
    </div>

    <div class="artist">
        {item.track_artist_credit || '-'}
    </div>

    <div class="release">
        {item.track_release_name  || '-'}
    </div>

    <div class="length">
        {item.track_length_display}
    </div>
    -->
</div>

<style>
    .item {
        width: 100%;
        min-height: 52px;
        margin: 0;
        padding-right: 24px;
        text-align: left;
        background: transparent;
        border: 0;
        outline: 0;
        font-size: 14px;
        cursor: default;
        border-radius: 4px;
        padding-left: 24px;
        padding-right: 24px;

    }
    .item.playing {
        font-weight: bold;
    }
    .item:focus {
        background-color: #ff2a2aff;
        color: #fff;
    }
    h4 {
        font-size: 16px;
        margin: 0;
    }
    h4 > p {
        line-height: 1.25;
        margin: 0;
        opacity: .85;
    }
    h4 small {
        font-size: 14px;
    }
    /*
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
    } */
</style>
