<script lang="ts">
    import type { AudioPlayer } from "../core/audio/player";
    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";
    import PLikedView from "./PLikedView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PArtistView from "./PArtistView.svelte";
    import PSidebar from "./PSidebar.svelte";

    export let player: AudioPlayer;
    export let trackCount: number = 0;
</script>

<div class="container-fluid h-100 px-0">
    <div class="d-flex h-100 w-100">
        <PSidebar {trackCount} />
        <PAlbumView />
        <PArtistView />
        <PLibraryView {player} />
        <PQueueView {player} />
        <PLikedView {player} />
    </div>
</div>

<style>
    .container-fluid {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
