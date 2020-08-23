<script lang="ts">
    import { onMount } from "svelte";
    import { getArtists } from '../core/api/queries';
    import { artists, currentView } from '../core/store';
    import { SublevelViews } from "../core/enums/SublevelViews";
    import type { AudioPlayer } from "../core/audio/player";
    import type { IView } from "../core/interfaces/IView";

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
        currentView.update(cur => ({
            ...cur,
            sublevel: SublevelViews.ArtistDetails,
            data: event.detail
        }));
    }

    const onBack = () => {
        currentView.update(cur => ({
            ...cur,
            sublevel: null,
            data: null
        }));
    }

    $: view = $currentView;
</script>

{#if view.sublevel === SublevelViews.ArtistDetails && view.data}
    <PArtistDetails
        {player}
        artist={view.data}
        on:back={onBack} />
{:else}
    <PCoverArtGridView
        heading="Artists"
        subheading="{$artists.data.length} artists"
        data={$artists.data}
        on:details={onDetails} />
{/if}
