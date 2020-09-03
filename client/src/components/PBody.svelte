<script lang="ts">
    import { onMount } from "svelte";
    import { getLibrary } from "../core/api/queries";
    import { library, artists } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";
    import PLibraryView from "./PLibraryView.svelte";
    import PQueueView from "./PQueueView.svelte";
    import PLikedView from "./PLikedView.svelte";
    import PSidebar from "./PSidebar.svelte";

    export let player: AudioPlayer;

    let trackCount: number = 0;

    onMount(async () => {
        const res = await getLibrary();
        const data = await res.json();
        trackCount = data.track_count;
        $artists = data.artists;
        $library = data.releases;
    });

</script>

<div class="container-fluid h-100 px-0">
    <div class="d-flex h-100 w-100">
        <PSidebar {trackCount} />
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
