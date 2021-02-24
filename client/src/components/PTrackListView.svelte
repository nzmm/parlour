<script lang="ts">
    import { currentTrack, playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ITrack } from "../core/interfaces/ITrack";

    import PTrackListItem from './PTrackListItem.svelte';

    export let data: ITrack[] = [];
    export let indexed: boolean = false;
</script>

<table class="w-100">
    <tbody>
        {#each data as item, i}
        <PTrackListItem
            {item}
            bind:indexed
            number={indexed ? i+1 : item.number}
            current={item.id === $currentTrack.id}
            playing={$playerState.state === PlaybackState.Playing}
            on:dropdown
            on:play />
        {/each}
    </tbody>
</table>
