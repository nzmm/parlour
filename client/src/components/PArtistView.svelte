<script lang="ts">
    import { onMount } from "svelte";
    import { getArtists } from '../core/api/queries';
    import { setArtistDetailsView, goBack } from '../core/actions';
    import { artists, currentView } from '../core/store';
    import { SublevelViews } from "../core/enums/SublevelViews";
    import type { AudioPlayer } from "../core/audio/player";

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

    const onDetails = (event: CustomEvent) => {
        setArtistDetailsView(event.detail);
    }

    $: view = $currentView;
</script>

{#if view.sublevel === SublevelViews.ArtistDetails && view.data}
    <PArtistDetails
        {player}
        artist={view.data}
        on:back={goBack} />
{:else}
    <PCoverArtGridView
        heading="Artists"
        subheading="{$artists.data.length} artists"
        data={$artists.data}
        on:details={onDetails} />
{/if}
