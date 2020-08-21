<script lang="ts">
    import { Views } from "../core/enums/Views";
    import { currentView } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";

    import FluidContainer from "./common/FluidContainer.svelte";
    import PArtistGridView from "./PArtistGridView.svelte";
    import PAlbumGridView from "./PAlbumGridView.svelte";
    import PSongListView from "./PSongListView.svelte";
    import PQueueListView from "./PQueueListView.svelte";

    export let player: AudioPlayer;

    const views = {
        [Views.Artists]: { component: PArtistGridView, props: {} },
        [Views.Albums]: { component: PAlbumGridView, props: {} },
        [Views.Songs]: { component: PSongListView, props: { player } },
        [Views.NowPlaying]: { component: PQueueListView, props: {} }
    }

    $: view = views[$currentView];
</script>

<div class="content-view w-100 h-100">
    <FluidContainer>
        <svelte:component this={view.component} {...view.props} />
    </FluidContainer>
</div>

<style>
    .content-view {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
