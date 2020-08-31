<script lang="ts">
    import { artists, currentView, queue, liked } from '../core/store';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import ScrolledView from './common/ScrolledView.svelte';
import NavLink from './common/NavLink.svelte';

    const setToplevel = (view: ToplevelViews) => {
        $currentView = { toplevel: view }
        sessionStorage.setItem("view", view.toString());
    }
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">
            <NavLink
                href="#artists"
                label="Artists"
                count={$artists.length}
                on:click={() => setToplevel(ToplevelViews.Artists)} />

            <NavLink
                href="#albums"
                label="Albums"
                count={$artists.length}
                on:click={() => setToplevel(ToplevelViews.Albums)} />

            <NavLink
                href="#songs"
                label="Songs"
                count={$artists.length}
                on:click={() => setToplevel(ToplevelViews.Songs)} />

            <hr>

            <NavLink
                href="#queue"
                label="Play Queue"
                count={$queue.data.length}
                on:click={() => setToplevel(ToplevelViews.PlayQueue)} />

            <NavLink
                href="#liked"
                label="Liked"
                count={$liked.length}
                on:click={() => setToplevel(ToplevelViews.Liked)}/>

            <hr>

            <NavLink
                href="#channels"
                label="Channels"
                count={0} />

        </div>
    </ScrolledView>
</aside>

<style>
    aside {
        height: 100%;
        background-color: #eee;
        font-size: 13px;
    }
    .wrapper {
        padding-top: 24px;
        padding-bottom: 24px;
    }
</style>
