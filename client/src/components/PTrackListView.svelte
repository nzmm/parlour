<script lang="ts">
    import { currentTrack, playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ITrack } from "../core/interfaces/ITrack";

    import ScrolledView from "./common/ScrolledView.svelte";
    import PTrackListItem from './PTrackListItem.svelte';

    export let heading = "";
    export let subheading = "";
    export let data: ITrack[] = [];
    export let withQueueActions: boolean = false;

    $: currentId = $currentTrack.id;
    $: playbackState = $playerState.state;
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
        <PTrackListItem
            {item}
            {withQueueActions}
            current={item.id === currentId}
            playing={playbackState === PlaybackState.Playing}
            on:play
            on:enqueue
            on:enqueueNext
            on:liked />
        {/each}
    </div>
</ScrolledView>

<style>
    h2 {
        padding-left: 24px;
        font-weight: bold;
    }
    h2 > small {
        font-size: 18px;
    }
</style>