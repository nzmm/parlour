<script lang="ts">
    import { playerState, playbackMode } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { AudioPlayer } from '../core/audio/player';
    import Loader from "./common/Loader.svelte";
    import GlyphButton from "./common/GlyphButton.svelte";
    import TextDropshadow from "./common/TextDropshadow.svelte";
    import PPlaybackProgressbar from './PPlaybackProgressbar.svelte';
    import { ShuffleMode } from '../core/enums/ShuffleMode';
    import { RepeatMode } from '../core/enums/RepeatMode';

    export let player: AudioPlayer;
</script>

<section class="d-flex flex-column align-items-center">
    <div class="d-flex align-items-center">
        <TextDropshadow>
            <GlyphButton
                glyphName="fas fa-random"
                ariaLabel="Shuffle"
                active={$playbackMode.shuffle !== ShuffleMode.None}
                on:click={() => player.toggleShuffle()} />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName="fas fa-fast-backward"
                ariaLabel="Previous track" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName={$playerState.state === PlaybackState.Playing  ? 'fas fa-pause' : 'fas fa-play'}
                ariaLabel="Play / Pause"
                on:click={() => player.toggle()}>

                {#if $playerState.state === PlaybackState.Loading}
                <div class="loader">
                    <Loader />
                </div>
                {/if}

            </GlyphButton>
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName="fas fa-fast-forward"
                ariaLabel="Next track"
                on:click={() => player.playNext()} />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName="fas fa-redo"
                ariaLabel="Repeat"
                active={$playbackMode.repeat !== RepeatMode.None}
                on:click={() => player.toggleRepeat()} />
        </TextDropshadow>
    </div>

    <PPlaybackProgressbar
        length={$playerState.length}
        position={$playerState.position} />

</section>

<style type="text/scss">
    section {
        width: 33vw;
    }
    .loader {
        position: absolute;
        top: -22px;
        left: -22px;
    }
</style>