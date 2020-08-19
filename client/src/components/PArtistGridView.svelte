<script lang="ts">
    import { onMount } from "svelte";
    import { getAlbums } from '../core/api/graph';
    import { artists } from '../core/store';

    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    onMount(async () => {
        if ($artists.ready) {
            return;
        }

        const res = await getAlbums();
        const data = await res.json();
        artists.set({ ready: true, data: data.value });
    });
</script>

<PCoverArtGridView heading="Artists" subheading="{$artists.data.length} artists" data={$artists.data} />
