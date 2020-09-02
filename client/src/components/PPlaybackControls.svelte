<script lang="ts">
    import { playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { AudioPlayer } from '../core/audio/player';
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
                on:click={() => player.toggle()} />
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

<style>
    section {
        width: 33vw;
    }
</style>