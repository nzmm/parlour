<script lang="ts">
    import { Views } from "../core/enums/Views";
    import { currentView, queue } from "../core/store";

    import NavBar from './common/NavBar.svelte';
    import NavLink from './common/NavLink.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
</script>

<NavBar class="top-nav border-bottom">
    <a class="navbar-brand" href="/">
        <img src="/static/data/im/parlour-brand-32.png" alt="Parlour" height="32" />
    </a>

    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
            <NavLink
                label="Artists"
                href="#artists"
                active={$currentView === Views.Artists}
                on:click={() => currentView.set(Views.Artists)}/>

            <NavLink
                label="Albums"
                href="#albums"
                active={$currentView === Views.Albums}
                on:click={() => currentView.set(Views.Albums)}/>

            <NavLink
                label="Songs"
                href="#songs"
                active={$currentView === Views.Songs}
                on:click={() => currentView.set(Views.Songs)}/>

            <NavLink
                label="Play Queue{$queue.data.length ? ` (${$queue.data.length})` : ''}"
                href="#play-queue"
                class="ml-3"
                active={$currentView === Views.NowPlaying}
                on:click={() => currentView.set(Views.NowPlaying)}/>
        </ul>
    </div>

    <button class="user btn p-0">
        <TextDropshadow size="smallest">
            <strong>MM</strong>
        </TextDropshadow>
    </button>
</NavBar>

<style>
    :global(.top-nav) {
        box-shadow: 0 3px 6px rgba(0,0,0,0.11), 0 3px 6px rgba(0,0,0,0.18);
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