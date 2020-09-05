<script lang="ts">
    import { playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { AudioPlayer } from '../core/audio/player';
    import Loader from "./common/Loader.svelte";
    import GlyphButton from "./common/GlyphButton.svelte";
    import TextDropshadow from "./common/TextDropshadow.svelte";
    import PPlaybackProgressbar from './PPlaybackProgressbar.svelte';

    export let player: AudioPlayer;
</script>

<section class="d-flex flex-column align-items-center">
    <div class="d-flex align-items-center">
        <TextDropshadow>
            <GlyphButton glyphName="fas fa-random" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton glyphName="fas fa-fast-backward" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName={$playerState.state === PlaybackState.Playing  ? 'fas fa-pause' : 'fas fa-play'}
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
                on:click={() => player.playNext()} />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton glyphName="fas fa-redo" />
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