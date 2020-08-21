<script lang="ts">
    import { onMount } from "svelte";
    import { songs } from '../core/store';
    import { getSongs } from '../core/api/queries';
    import type { AudioPlayer } from "../core/audio/player";

    import PTrackListView from "./PTrackListView.svelte";

    export let player: AudioPlayer;

    onMount(async () => {
        if ($songs.ready) {
            return;
        }

        const res = await getSongs();
        const data = await res.json();
        songs.set({ ready: true, data: data.songs });
    });
</script>

<PTrackListView
    heading="Songs"
    subheading="{$songs.data.length} songs"
    data={$songs.data}
    withEnqueuAction
    on:rowDblClick={e => player.play(e.detail)} />
