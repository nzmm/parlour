<script lang="ts">
    import { playNow } from '../core/playlist';
    import type { AudioPlayer } from '../core/audio/player';
    import type { ITrack } from "../core/interfaces/ITrack";
    import Page from "./common/Page.svelte";
    import PTrackListView from './PTrackListView.svelte';
    import PTrackListDropdown from './PTrackListDropdown.svelte';

    let className = "";

    export { className as class };
    export let player: AudioPlayer;
    export let active: boolean = true;
    export let data: ITrack[] = [];
    export let indexed: boolean = false;

    let track: ITrack = null;
    let visible: boolean = false;
    let top: number = 0;
    let left: number = 0;

    const showDropdown = (event: CustomEvent) => {
        visible = true;
        top = event.detail.top;
        left = event.detail.left;
        track = event.detail.item;
    };
</script>

<Page {active}>
    <slot></slot>
    <section class="list {className}">
        <PTrackListView
            {data}
            bind:indexed
            on:dropdown={showDropdown}
            on:play={e => playNow(player, [e.detail])} />
    </section>
</Page>

<PTrackListDropdown
    {player}
    {track}
    {visible}
    {top}
    {left}
    on:hide={() => visible = false} />

