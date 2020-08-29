<script lang="ts">
    import { currentView, queue } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import PTrackView from "./PTrackView.svelte";
</script>

<PTrackView data={$queue.data} active={$currentView.toplevel === ToplevelViews.PlayQueue}>
    <div class="header">
        <h2 class="py-4">Play Queue</h2>
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