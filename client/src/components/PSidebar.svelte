<script lang="ts">
    import { artists, queue, liked, library } from '../core/store';
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
                href="#artists"
                label="Artists"
                count={$artists.length}
                on:click={() => setToplevel(ToplevelViews.Artists)} />

            <NavLink
                href="#albums"
                label="Albums"
                count={$library.length}
                on:click={() => setToplevel(ToplevelViews.Albums)} />

            <NavLink
                href="#songs"
                label="Songs"
                count={trackCount}
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
