<script lang="ts">
    import { likeTrack } from '../core/actions';
    import { channels } from '../core/store';
    import { enqueue, enqueueNext, playNow } from '../core/playlist';
    import { createChannelTrack } from '../core/api/commands';
    import type { ITrack } from "../core/interfaces/ITrack";
    import type { AudioPlayer } from '../core/audio/player';
    import type { IChannel } from '../core/interfaces/IChannel';
    import DropdownMenu from "./common/DropdownMenu.svelte";
    import DropdownSubMenu from "./common/DropdownSubMenu.svelte";

    export let player: AudioPlayer;
    export let track: ITrack;
    export let visible: boolean = false;
    export let top: number = 0;
    export let left: number = 0;

    const onAddToChannel = async (ch: IChannel) => {
        const res = await createChannelTrack(ch.unique_id, track.id);
        const data = await res.json();
        if (data.success) {

        }
    }
</script>

<DropdownMenu {visible} {top} {left} on:hide >
    <a class="dropdown-item" href="#play" on:click|preventDefault={() => playNow(player, [track])}>
        Play
    </a>

    <div class="dropdown-divider"></div>

    <a class="dropdown-item" href="#enqueue" on:click|preventDefault={() => enqueue(player, [track])}>
        Add to queue
    </a>
    <a class="dropdown-item" href="#next" on:click|preventDefault={() => enqueueNext(player, [track])}>
        Play next
    </a>

    <DropdownSubMenu label="Add to playlist…" />

    <DropdownSubMenu label="Add to channel…">
        {#each $channels as ch}
        <a
            class="dropdown-item"
            href="#channels/{ch.unique_id}"
            on:click={() => onAddToChannel(ch)} >
            {ch.name}
        </a>
        {/each}
    </DropdownSubMenu>

    <div class="dropdown-divider"></div>

    <a class="dropdown-item" href="#like" on:click|preventDefault={() => likeTrack(track)}>
        {track.liked ? "Dislike" : "Like"}
    </a>
</DropdownMenu>