<script lang="ts">
    import { artists, queue, liked, library, channels } from '../core/store';
    import ScrolledView from './common/ScrolledView.svelte';
    import NavLink from './common/NavLink.svelte';
    import NavHeader from './common/NavHeader.svelte';
    import PCreateChannel from './modals/PCreateChannel.svelte';
    import PCreatePlaylist from './modals/PCreatePlaylist.svelte';

    export let trackCount: number = 0;

    let createPlaylist = false;
    let createChannel = false;
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">

            <NavHeader>Library</NavHeader>

            <NavLink
                href="/"
                label="Songs"
                count={trackCount} />

            <NavLink
                href="/albums"
                label="Albums"
                activePath="/albums*"
                count={$library.length} />

            <NavLink
                href="/artists"
                label="Artists"
                activePath="/artists*"
                count={$artists.length} />

            <hr>

            <NavHeader>
                Playlists

                <button
                    slot="actions"
                    aria-label="Create playlist"
                    on:click={() => createPlaylist = true}>
                    <i class="fas fa-plus"></i>
                </button>
            </NavHeader>

            <NavLink
                href="/queue"
                label="Play Queue"
                count={$queue.length} />

            <NavLink
                href="/liked"
                label="Liked"
                count={$liked.length} />

            <hr>

            <NavHeader>
                Channels

                <button
                    slot="actions"
                    aria-label="Create channel"
                    on:click={() => createChannel = true}>
                    <i class="fas fa-plus"></i>
                </button>
            </NavHeader>

            {#each $channels as ch}
            <NavLink
                href="/channels/{ch.unique_id}"
                label={ch.name} />
            {/each}

        </div>
    </ScrolledView>
</aside>

{#if createChannel}
<PCreateChannel on:close={() => createChannel = false} />
{/if}
{#if createPlaylist}
<PCreatePlaylist on:close={() => createPlaylist = false} />
{/if}


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
