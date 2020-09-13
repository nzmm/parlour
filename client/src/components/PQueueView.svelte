<script lang="ts">
    import { currentView, queue } from '../core/store';
    import { getHms } from '../core/utils';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { AudioPlayer } from '../core/audio/player';
    import PTrackView from "./PTrackView.svelte";

    export let player: AudioPlayer;

    $: duration = getHms($queue.reduce((acc, cur) => acc + cur.length, 0));
</script>

<PTrackView
    class="pb-5"
    {player}
    indexed
    data={$queue}
    active={$currentView.toplevel === ToplevelViews.PlayQueue}>

    <div class="header pb-3">
        <h2>Play Queue</h2>
        <p class="text-muted"><small>{$queue.length} tracks queued{$queue.length ? `, ${duration[0]} ${duration[1]}` : ''}</small></p>
    </div>

</PTrackView>

<style>
    h2 {
        font-weight: bold;
    }
</style>