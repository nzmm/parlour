<script lang="ts">
    import { library, currentView } from '../core/store';
    import { filterLibraryByAlbum, setToplevel } from '../core/actions';
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    const onDetails = (event: CustomEvent<IAlbum>) => {
        setToplevel(ToplevelViews.Songs);
        filterLibraryByAlbum(event.detail.id, event.detail.name);
    }
</script>


<PCoverArtGridView
    context="album"
    data={$library}
    on:details={onDetails}
    active={$currentView.toplevel === ToplevelViews.Albums}>

    <span let:item slot="label">
        <div class="pb-1">{item.name || '-'}</div>
        <small class="text-muted">{item.artist_name}</small>
    </span>

</PCoverArtGridView>
