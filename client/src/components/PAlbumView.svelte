<script lang="ts">
    import { onMount } from "svelte";
    import { getAlbums } from '../core/api/queries';
    import { albums, currentView } from '../core/store';
    import { setAlbumDetailsView, goBack } from '../core/actions';
    import { SublevelViews } from "../core/enums/SublevelViews";
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

    const onDetails = (event: CustomEvent) => {
        setAlbumDetailsView(event.detail);
    }

    $: view = $currentView;
</script>

{#if view.sublevel === SublevelViews.AlbumDetails && view.data}
    <PAlbumDetails
        {player}
        album={view.data}
        on:back={goBack} />
{:else}
    <PCoverArtGridView
        heading="Albums"
        subheading="{$albums.data.length} albums"
        data={$albums.data}
        on:details={onDetails}>

        <span let:item slot="label">
            <div class="pb-1">{item.name || '-'}</div>
            <small class="text-muted">{item.artist_name}</small>
        </span>

    </PCoverArtGridView>
{/if}
