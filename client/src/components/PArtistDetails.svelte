<script lang="ts">
    import { onMount } from "svelte";
    import { enqueue, enqueueNext, playNow } from '../core/actions';
    import { getArtistDetails } from "../core/api/queries";
    import type { IArtist } from "../core/interfaces/IArtist";
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import type { AudioPlayer } from "../core/audio/player";

    import PDetailsView from './PDetailsView.svelte';
    import PTrackListView from "./PTrackListView.svelte";
    import PCoverArt from "./PCoverArt.svelte";

    export let player: AudioPlayer;
    export let artist: IArtist;

    let releases: IAlbum[] = [];

    onMount(async () => {
        const res = await getArtistDetails(artist.id);
        const data = await res.json();
        artist = data.artist;
        releases = data.releases;
    });

</script>

<PDetailsView
    heading={artist.name}
    thumbnail={artist.thumbnail}
    on:back>

    {#each releases as release}
        <section class="mb-4 pt-3">

            <div class="d-flex mb-3">
                <PCoverArt src={release.thumbnail} size="100px" />

                <h4 class="pl-4">
                    {release.name}

                    <p class="text-muted">
                        <small>{release.name}<br/>{release.year}</small>
                    </p>
                </h4>
            </div>

            <PTrackListView
                data={release.tracks}
                on:play={e => playNow(player, e.detail)}
                on:enqueue={e => enqueue(player, e.detail)}
                on:enqueueNext={e => enqueueNext(player, e.detail)}/>

        </section>
    {/each}

</PDetailsView>

<style>
    h4 > p {
        line-height: .9;
    }
    h4 small {
        font-size: 14px;
    }
</style>