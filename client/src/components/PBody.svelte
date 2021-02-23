<script lang="ts">
    import Router from 'svelte-spa-router';
    import { wrap } from 'svelte-spa-router/wrap';

    import type { AudioPlayer } from "../core/audio/player";
    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";
    import PLikedView from "./PLikedView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PArtistView from "./PArtistView.svelte";
    import PChannelView from "./PChannelView.svelte";
    import PSidebar from "./PSidebar.svelte";
    import NotFound from "./NotFound.svelte";

    export let player: AudioPlayer;
    export let trackCount: number = 0;

    const routes = {
        '/': wrap({ component: PLibraryView, props: { player }}),
        '/albums': PAlbumView,
        '/albums/*': PAlbumView,
        '/artists': PArtistView,
        '/artists/*': PArtistView,
        '/queue': wrap({ component: PQueueView, props: { player }}),
        '/liked': wrap({ component: PLikedView, props: { player }}),
        '/channel/:id': PChannelView,

        '*': NotFound,
    }
</script>

<div class="container-fluid h-100 px-0">
    <div class="d-flex h-100 w-100">
        <PSidebar {trackCount} />
        <Router {routes} />
    </div>
</div>

<style>
    .container-fluid {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
