<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { currentTrack, playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ITrack } from "../core/interfaces/ITrack";

    import DropdownMenu from "./common/DropdownMenu.svelte";
    import PTrackListItem from './PTrackListItem.svelte';

    export let data: ITrack[] = [];
    export let withQueueActions: boolean = false;

    const dispatch = createEventDispatcher();

    $: currentId = $currentTrack.id;
    $: playbackState = $playerState.state;

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

<table class="w-100">
    <tbody>
        {#each data as item}
        <PTrackListItem
            {item}
            current={item.id === currentId}
            playing={playbackState === PlaybackState.Playing}
            on:dropdown={showDropdown}
            on:play />
        {/each}
    </tbody>
</table>

<DropdownMenu {visible} {top} {left} on:hide={() => visible = false}>
    <a class="dropdown-item" href="#play" on:click|preventDefault={() => dispatch('play', track)}>
        Play
    </a>

    <div class="dropdown-divider"></div>

    {#if withQueueActions}
    <a class="dropdown-item" href="#enqueue" on:click|preventDefault={() => dispatch('enqueue', track)}>
        Add to queue
    </a>
    <a class="dropdown-item" href="#next" on:click|preventDefault={() => dispatch('enqueueNext', track)}>
        Play next
    </a>

    <div class="dropdown-divider"></div>
    {/if}

    <a class="dropdown-item" href="#like" on:click|preventDefault={() => dispatch("liked", track)}>
        Like
    </a>
</DropdownMenu>
