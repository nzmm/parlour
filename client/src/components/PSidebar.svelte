<script lang="ts">
    import { artists } from '../core/store';
    import ScrolledView from './common/ScrolledView.svelte';
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">
            <div class="text-muted d-flex justify-content-between align-items-center artist-nav">
                <strong>
                    All Artists
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </div>

            {#each $artists as artist}
            <div class="artist-nav" on:click={() => null}>{artist.name}</div>
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
    }
</style>
