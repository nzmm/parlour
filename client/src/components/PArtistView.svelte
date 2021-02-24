<script lang="ts">
    import { push } from 'svelte-spa-router';
    import type { IArtist } from '../core/interfaces/IArtist';
    import { artists } from '../core/store';
    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    const onDetails = (event: CustomEvent<IArtist>) => {
        push(`/artists/${event.detail.id}`);
    }
</script>

<PCoverArtGridView
    context="artist"
    class="artist"
    data={$artists}
    on:details={onDetails} />

<style>
    :global(.artist.grid button, .artist.grid .p-cover, .artist.grid img) {
        border-radius: 50%;
    }
</style>
