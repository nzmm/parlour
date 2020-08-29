<script lang="ts">
    import { currentTrack, playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ITrack } from "../core/interfaces/ITrack";

    import PTrackListItem from './PTrackListItem.svelte';

    export let data: ITrack[] = [];

    $: currentId = $currentTrack.id;
    $: playbackState = $playerState.state;
</script>

<table class="w-100">
    <tbody>
        {#each data as item}
        <PTrackListItem
            {item}
            current={item.id === currentId}
            playing={playbackState === PlaybackState.Playing}
            on:dropdown
            on:play />
        {/each}
    </tbody>
</table>
