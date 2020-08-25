<script lang="ts">
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import { currentView, queue } from "../core/store";
    import NavLink from './common/NavLink.svelte';

    const setView = (toplevel: ToplevelViews) => {
        setTimeout(() => {
            currentView.set({ toplevel });
            sessionStorage.setItem('view', toplevel.toString());
        }, 100);
    }

</script>

<aside class="border-right py-3">
    <NavLink
        label="Artists"
        href="#artists"
        active={$currentView.toplevel === ToplevelViews.Artists}
        on:click={() => setView(ToplevelViews.Artists)}/>

    <NavLink
        label="Albums"
        href="#albums"
        active={$currentView.toplevel === ToplevelViews.Albums}
        on:click={() => setView(ToplevelViews.Albums)}/>

    <NavLink
        label="Library"
        href="#library"
        active={$currentView.toplevel === ToplevelViews.Library}
        on:click={() => setView(ToplevelViews.Library)}/>

    <NavLink
        label="Play Queue{$queue.data.length ? ` (${$queue.data.length})` : ''}"
        href="#play-queue"
        active={$currentView.toplevel === ToplevelViews.PlayQueue}
        on:click={() => setView(ToplevelViews.PlayQueue)}/>
</aside>

<style>
    aside {
        width: 350px;
        height: 100%;
        background-color: #eee;
    }
</style>