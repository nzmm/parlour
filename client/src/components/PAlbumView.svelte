<script lang="ts">
    import { onMount } from "svelte";
    import { getAlbums } from '../core/api/queries';
    import { albums } from '../core/store';

    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    onMount(async () => {
        if ($albums.ready) {
            return;
        }

        const res = await getAlbums();
        const data = await res.json();
        albums.set({ ready: true, data: data.albums });
    });
</script>

<PCoverArtGridView
    heading="Albums"
    subheading="{$albums.data.length} albums"
    data={$albums.data}
    on:details={e => console.log(e.detail)} />
