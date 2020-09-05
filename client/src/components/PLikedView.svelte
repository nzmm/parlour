<script lang="ts">
    import { currentView, liked } from '../core/store';
    import { playNow } from '../core/playlist';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { AudioPlayer } from '../core/audio/player';
    import Button from './common/Button.svelte';
    import PTrackView from "./PTrackView.svelte";

    export let player: AudioPlayer;
</script>

<PTrackView
    class="pb-5"
    indexed
    {player}
    data={$liked}
    active={$currentView.toplevel === ToplevelViews.Liked}>

    <div class="header pt-4 pb-3">
        <h2>Liked</h2>
        <Button
            narrow
            primary
            on:click={() => playNow(player, $liked)}>
            Play
        </Button>
    </div>
</PTrackView>

<style>
    .header {
        padding-left: 24px;
        padding-right: 24px;
    }
    h2 {
        font-weight: bold;
    }
</style>