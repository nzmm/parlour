<script lang="ts">
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import { currentView, queue } from "../core/store";
    import type { AudioPlayer } from "../core/audio/player";
    import NavBar from './common/NavBar.svelte';
    import NavLink from './common/NavLink.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PSearchMusicInput from "./PSearchMusicInput.svelte";

    export let player: AudioPlayer;

    const setView = (toplevel: ToplevelViews) => {
        currentView.set({ toplevel });
        sessionStorage.setItem('view', toplevel.toString());
    }
</script>

<NavBar class="top-nav border-bottom">
    <a class="navbar-brand pr-2" href="/">
        <img src="/static/data/im/parlour-brand-32.png" alt="Parlour" height="32" />
    </a>

    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
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
                class="ml-3"
                active={$currentView.toplevel === ToplevelViews.PlayQueue}
                on:click={() => setView(ToplevelViews.PlayQueue)}/>
        </ul>
    </div>

    <PSearchMusicInput {player} />

    <button class="user btn p-0" style="margin-top: 1px;">
        <TextDropshadow size="smallest">
            <strong>MM</strong>
        </TextDropshadow>
    </button>
</NavBar>

<style>
    :global(.top-nav) {
        box-shadow: 0 -0.4rem 0.9rem 0.2rem rgba(0,0,0,.175);
    }
    .user {
        width: 36px;
        height: 36px;
        border-radius: 4px;
        background-color: #adadadff;
        color: #fff;
        line-height: 36px;
        text-align: center;
    }
</style>