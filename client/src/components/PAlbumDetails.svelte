<script lang="ts">
    import { onMount } from "svelte";
    import { enqueue, enqueueNext, playNow } from '../core/actions';
    import { getAlbumDetails } from "../core/api/queries";
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import type { ITrack } from "../core/interfaces/ITrack";
    import type { AudioPlayer } from "../core/audio/player";

    import PDetailsView from './PDetailsView.svelte';
    import PTrackListView from './PTrackListView.svelte';

    export let player: AudioPlayer;
    export let album: IAlbum;

    let tracks: ITrack[] = [];

    onMount(async () => {
        const res = await getAlbumDetails(album.id);
        const data = await res.json();
        album = data.album;
        tracks = data.tracks;
    });

</script>

<PDetailsView
    heading={album.name}
    subheading1={album.artist_name}
    subheading2={album.year}
    thumbnail={album.thumbnail}
    on:back>

    <PTrackListView
        data={tracks}
        withQueueActions
        on:play={e => playNow(player, e.detail)}
        on:enqueue={e => enqueue(player, e.detail)}
        on:enqueueNext={e => enqueueNext(player, e.detail)}/>

</PDetailsView>
