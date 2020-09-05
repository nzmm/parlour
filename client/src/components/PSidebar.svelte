<script lang="ts">
    import { artists, queue, liked, library, currentView } from '../core/store';
    import { setToplevel } from '../core/actions';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import ScrolledView from './common/ScrolledView.svelte';
    import NavLink from './common/NavLink.svelte';

    export let trackCount: number = 0;
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">

            <NavLink
                href="#songs"
                label="Songs"
                count={trackCount}
                active={$currentView.toplevel === ToplevelViews.Songs}
                on:click={() => setToplevel(ToplevelViews.Songs)} />

            <NavLink
                href="#albums"
                label="Albums"
                count={$library.length}
                active={$currentView.toplevel === ToplevelViews.Albums}
                on:click={() => setToplevel(ToplevelViews.Albums)} />

            <NavLink
                href="#artists"
                label="Artists"
                count={$artists.length}
                active={$currentView.toplevel === ToplevelViews.Artists}
                on:click={() => setToplevel(ToplevelViews.Artists)} />

            <hr>

            <NavLink
                href="#queue"
                label="Play Queue"
                count={$queue.length}
                active={$currentView.toplevel === ToplevelViews.PlayQueue}
                on:click={() => setToplevel(ToplevelViews.PlayQueue)} />

            <NavLink
                href="#liked"
                label="Liked"
                count={$liked.length}
                active={$currentView.toplevel === ToplevelViews.Liked}
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
    hr {
        margin-left: 8px;
        margin-right: 8px;
        opacity: .5;
    }
</style>
