<script lang="ts">
    import { filterLibraryByArtist, setToplevel } from '../core/actions';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { IArtist } from '../core/interfaces/IArtist';
    import { artists, currentView } from '../core/store';
    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    const onDetails = (event: CustomEvent<IArtist>) => {
        setToplevel(ToplevelViews.Songs);
        filterLibraryByArtist(event.detail.id, event.detail.name);
    }
</script>

<PCoverArtGridView
    context="artist"
    class="artist"
    data={$artists}
    on:details={onDetails}
    active={$currentView.toplevel === ToplevelViews.Artists} />

<style>
    :global(.artist.grid button, .artist.grid .p-cover, .artist.grid img) {
        border-radius: 50%;
    }
</style>
