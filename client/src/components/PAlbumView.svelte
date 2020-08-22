<script lang="ts">
    import { onMount } from "svelte";
    import { getAlbums } from '../core/api/queries';
    import { albums } from '../core/store';
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import type { AudioPlayer } from "../core/audio/player";

    import PCoverArtGridView from "./PCoverArtGridView.svelte";
    import PAlbumDetails from "./PAlbumDetails.svelte";

    export let player: AudioPlayer;

    onMount(async () => {
        if ($albums.ready) {
            return;
        }

        const res = await getAlbums();
        const data = await res.json();
        albums.set({ ready: true, data: data.albums });
    });

    let album: IAlbum;

</script>

{#if album}
    <PAlbumDetails
        {player}
        {album}
        on:back={() => album = null} />
{:else}
    <PCoverArtGridView
        heading="Albums"
        subheading="{$albums.data.length} albums"
        data={$albums.data}
        on:details={e => album = e.detail} />
{/if}
