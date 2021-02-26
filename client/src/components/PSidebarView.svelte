<script lang="ts">
    import Router from 'svelte-spa-router';
    import { wrap } from 'svelte-spa-router/wrap';
    import type { AudioPlayer } from '../core/audio/player';

    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";
    import PLikedView from "./PLikedView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PArtistView from "./PArtistView.svelte";
    //import PChannelView from "./PChannelView.svelte";
    import PSidebar from "./PSidebar.svelte";
    import NotFound from "./NotFound.svelte";

    export let player: AudioPlayer;
    export let trackCount: number = 0;

    const routes = {
        '/': wrap({ component: PLibraryView, props: { player, context: "" }}),
        '/albums': PAlbumView,
        '/artists': PArtistView,
        '/albums/:id': wrap({ component: PLibraryView, props: { player, context: 'albums' }}),
        '/artists/:id': wrap({ component: PLibraryView, props: { player, context: 'artists' }}),
        '/queue': wrap({ component: PQueueView, props: { player }}),
        '/liked': wrap({ component: PLikedView, props: { player }}),
        //'/channel/:id': PChannelView,

        '*': NotFound,
    }
</script>


<PSidebar {trackCount} />
<Router {routes} />