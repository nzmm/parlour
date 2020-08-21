<script lang="ts">
    import { onMount } from "svelte";
    import { songs, queue } from '../core/store';
    import { getSongs } from '../core/api/queries';
    import type { AudioPlayer } from "../core/audio/player";
    import type { ITrack } from "../core/interfaces/ITrack";

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

    const enqueue = (item: ITrack) => {
        queue.update(q => {
            q.data.push(item);
            return q;
        });
    }
</script>

<PTrackListView
    heading="Songs"
    subheading="{$songs.data.length} songs"
    data={$songs.data}
    withQueueActions
    on:play={e => player.play(e.detail)}
    on:enqueue={e => enqueue(e.detail)} />
