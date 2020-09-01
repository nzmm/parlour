<script lang="ts">
    import { currentView, queue } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import PTrackView from "./PTrackView.svelte";
</script>

<PTrackView
    class="pb-5"
    data={$queue.data}
    active={$currentView.toplevel === ToplevelViews.PlayQueue}>

    <div class="header pt-4 pb-3">
        <h2>Play Queue</h2>
        <p class="text-muted">{$queue.data.length} tracks queued</p>
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