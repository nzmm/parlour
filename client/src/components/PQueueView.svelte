<script lang="ts">
    import { currentView, queue } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { AudioPlayer } from '../core/audio/player';
    import PTrackView from "./PTrackView.svelte";

    export let player: AudioPlayer;
</script>

<PTrackView
    class="pb-5"
    {player}
    data={$queue}
    active={$currentView.toplevel === ToplevelViews.PlayQueue}>

    <div class="header pt-4 pb-3">
        <h2>Play Queue</h2>
        <p class="text-muted">{$queue.length} tracks queued</p>
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