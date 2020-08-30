<script lang="ts">
    import { artists } from '../core/store';
    import { unfilterLibrary, filterLibrary } from '../core/actions';
    import ScrolledView from './common/ScrolledView.svelte';
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">
            <a
                href="#all"
                class="text-muted d-flex justify-content-between align-items-center artist-nav"
                on:click|preventDefault={() => unfilterLibrary()}>

                <strong>
                    All Artists
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            {#each $artists as artist}
            <a
                href="#artist"
                class="artist-nav"
                on:click|preventDefault={() => filterLibrary(artist.id)}
                title="{artist.track_count} tracks">

                {artist.name}
            </a>
            {/each}
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
    .badge {
        background-color: #6c757d;
        color: #fff;
        padding-top: 3px;
        padding-bottom: 4px;
    }
    .artist-nav {
        width: 280px;
        padding-left: 10px;
        padding-right: 5px;
        padding-top: 3px;
        padding-bottom: 3px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        color: #333;
        text-decoration: none;
    }
</style>
