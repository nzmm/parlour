<script lang="ts">
    import { onMount } from "svelte";
    import { getAlbums } from '../core/api/queries';
    import { albums } from '../core/store';
    import type { AudioPlayer } from "../core/audio/player";

    import PCoverArtGridView from "./PCoverArtGridView.svelte";

    export let player: AudioPlayer = null;
    console.log(player);

    onMount(async () => {
        if ($albums.ready) {
            return;
        }

        const res = await getAlbums();
        const data = await res.json();
        albums.set({ ready: true, data: data.albums });
    });
</script>

<PCoverArtGridView heading="Albums" subheading="{$albums.data.length} albums" data={$albums.data} />
