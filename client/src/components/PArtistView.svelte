<script lang="ts">
    import { onMount } from "svelte";
    import { getArtists } from '../core/api/queries';
    import { artists } from '../core/store';

    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    onMount(async () => {
        if ($artists.ready) {
            return;
        }

        const res = await getArtists();
        const data = await res.json();
        artists.set({ ready: true, data: data.artists });
    });
</script>

<PCoverArtGridView
    heading="Artists"
    subheading="{$artists.data.length} artists"
    data={$artists.data} />
