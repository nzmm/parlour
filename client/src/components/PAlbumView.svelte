<script lang="ts">
    import { push } from 'svelte-spa-router';
    import { library } from '../core/store';
    import { filterLibraryByAlbum } from '../core/actions';
    import type { IAlbum } from "../core/interfaces/IAlbum";
    import PCoverArtGridView from "./PCoverArtGridView.svelte";
    import NotFound from "./NotFound.svelte";

    export let params;
    console.log(params);

    const onDetails = (event: CustomEvent<IAlbum>) => {
        push(`/albums/${event.detail.id}`)
        filterLibraryByAlbum(event.detail.id, event.detail.name);
    }

    const routes = {
        '/:id': null,
        '*': NotFound,
    }
</script>


<PCoverArtGridView
    context="album"
    data={$library}
    on:details={onDetails}>

    <span let:item slot="label">
        <div class="pb-1">{item.name || '-'}</div>
        <small class="text-muted">{item.artist_name}</small>
    </span>

</PCoverArtGridView>
