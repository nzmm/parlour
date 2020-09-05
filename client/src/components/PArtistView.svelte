<script lang="ts">
    import { filterLibraryByArtist, setToplevel } from '../core/actions';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { IArtist } from '../core/interfaces/IArtist';
    import { artists, currentView } from '../core/store';
    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    const onDetails = (event: CustomEvent<IArtist>) => {
        setToplevel(ToplevelViews.Songs);
        filterLibraryByArtist(event.detail.id);
    }
</script>

<PCoverArtGridView
    data={$artists}
    on:details={onDetails}
    active={$currentView.toplevel === ToplevelViews.Artists} />
