<script lang="ts">
    import { currentView, liked } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import PTrackView from "./PTrackView.svelte";
</script>

<PTrackView data={$liked} active={$currentView.toplevel === ToplevelViews.Liked}>
    <div class="header py-4">
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