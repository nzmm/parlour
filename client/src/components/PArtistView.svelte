<script lang="ts">
    import { onMount } from "svelte";
    import { getArtists } from '../core/api/queries';
    import { artists } from '../core/store';
    import type { AudioPlayer } from "../core/audio/player";
    import type { IAlbum } from "../core/interfaces/IAlbum";

    import PCoverArtGridView from "./PCoverArtGridView.svelte";
    import PArtistDetails from "./PArtistDetails.svelte";

    export let player: AudioPlayer;

    onMount(async () => {
        if ($artists.ready) {
            return;
        }

        const res = await getArtists();
        const data = await res.json();
        artists.set({ ready: true, data: data.artists });
    });

    let artist: IAlbum;

</script>

{#if artist}
    <PArtistDetails
        {player}
        {artist}
        on:back={() => artist = null} />
{:else}
    <PCoverArtGridView
        heading="Artists"
        subheading="{$artists.data.length} artists"
        data={$artists.data}
        on:details={e => artist = e.detail} />
{/if}
