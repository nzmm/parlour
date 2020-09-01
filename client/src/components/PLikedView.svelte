<script lang="ts">
    import { currentView, liked } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { AudioPlayer } from '../core/audio/player';
    import PTrackView from "./PTrackView.svelte";

    export let player: AudioPlayer;
</script>

<PTrackView
    class="pb-5"
    {player}
    data={$liked}
    active={$currentView.toplevel === ToplevelViews.Liked}>

    <div class="header pt-4 pb-3">
        <h2>Liked</h2>
        <p class="text-muted">{$liked.length} tracks</p>
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