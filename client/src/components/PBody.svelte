<script lang="ts">
    import { Views } from "../core/enums/Views";
    import { currentView } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";

    import FluidContainer from "./common/FluidContainer.svelte";
    import PArtistGridView from "./PArtistGridView.svelte";
    import PAlbumGridView from "./PAlbumGridView.svelte";
    import PSongListView from "./PSongListView.svelte";
    import PNowPlayingListView from "./PNowPlayingListView.svelte";

    const views = {
        [Views.Artists]: { component: PArtistGridView },
        [Views.Albums]: { component: PAlbumGridView },
        [Views.Songs]: { component: PSongListView },
        [Views.NowPlaying]: { component: PNowPlayingListView }
    }

    export let player: AudioPlayer;
</script>

<div class="content-view w-100 h-100">
    <FluidContainer>
        <svelte:component this={views[$currentView].component} {player} />
    </FluidContainer>
</div>

<style>
    .content-view {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
