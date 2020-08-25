<script lang="ts">
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import { currentView } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";
    import FluidContainer from "./common/FluidContainer.svelte";
    import PArtistView from "./PArtistView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";

    export let player: AudioPlayer;

    const views = {
        [ToplevelViews.Artists]: { component: PArtistView, props: { player } },
        [ToplevelViews.Albums]: { component: PAlbumView, props: { player } },
        [ToplevelViews.Library]: { component: PLibraryView, props: { player } },
        [ToplevelViews.PlayQueue]: { component: PQueueView, props: {} }
    }

    $: view = views[$currentView.toplevel];
</script>

<div class="content-view w-100 h-100">
    <FluidContainer>
        <svelte:component this={view.component} {...view.props} />
    </FluidContainer>
</div>

<style>
    .content-view {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
