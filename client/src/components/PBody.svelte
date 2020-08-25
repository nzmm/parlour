<script lang="ts">
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import { currentView } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";
    import PArtistView from "./PArtistView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";
    import PSidebar from "./PSidebar.svelte";

    export let player: AudioPlayer;

    const views = {
        [ToplevelViews.Artists]: { component: PArtistView, props: { player } },
        [ToplevelViews.Albums]: { component: PAlbumView, props: { player } },
        [ToplevelViews.Library]: { component: PLibraryView, props: { player } },
        [ToplevelViews.PlayQueue]: { component: PQueueView, props: {} }
    }

    $: view = views[$currentView.toplevel];
</script>

<div class="container-fluid h-100 px-0">
    <div class="d-flex h-100 w-100">
        <PSidebar />
        <svelte:component this={view.component} {...view.props} />
    </div>
</div>

<style>
    .container-fluid {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
