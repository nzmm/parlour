<script lang="ts">
    import { onMount } from "svelte";
    import { songs, queue, playerState } from '../core/store';
    import { getSongs } from '../core/api/queries';
    import { PlaybackState } from "../core/enums/PlaybackState";
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

    const _enqueue = (track: ITrack, method: (data: ITrack[]) => void) => {
        if ($playerState.state === PlaybackState.Stopped) {
            player.play(track);
        } else {
            queue.update(q => {
                method(q.data);
                return q;
            });
        }
    }

    const enqueue = (track: ITrack) => _enqueue(track, data => data.push(track));
    const enqueueNext = (track: ITrack) => _enqueue(track, data => data.splice(0, 0, track));

</script>

<PTrackListView
    heading="Songs"
    subheading="{$songs.data.length} songs"
    data={$songs.data}
    withQueueActions
    on:play={e => player.play(e.detail)}
    on:enqueue={e => enqueue(e.detail)}
    on:enqueueNext={e => enqueueNext(e.detail)} />
