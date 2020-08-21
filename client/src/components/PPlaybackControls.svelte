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
            <GlyphButton glyphName="fa-random" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton glyphName="fa-fast-backward" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton
                glyphName={$playerState.state === PlaybackState.Playing  ? 'fa-pause' : 'fa-play'}
                on:click={() => player.toggle()} />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton glyphName="fa-fast-forward" />
        </TextDropshadow>

        <TextDropshadow>
            <GlyphButton glyphName="fa-redo" />
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