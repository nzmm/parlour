<script lang="ts">
    import { Views } from "../core/enums/Views";
    import { currentView } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";

    import FluidContainer from "./common/FluidContainer.svelte";
    import PArtistView from "./PArtistView.svelte";
    import PAlbumView from "./PAlbumView.svelte";
    import PSongView from "./PSongView.svelte";
    import PQueueView from "./PQueueView.svelte";

    export let player: AudioPlayer;

    const views = {
        [Views.Artists]: { component: PArtistView, props: {} },
        [Views.Albums]: { component: PAlbumView, props: { player } },
        [Views.Songs]: { component: PSongView, props: { player } },
        [Views.PlayQueue]: { component: PQueueView, props: {} }
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
