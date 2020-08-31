<script lang="ts">
    import { artists } from '../core/store';
    //import { unfilterLibrary } from '../core/actions';
    import ScrolledView from './common/ScrolledView.svelte';
</script>

<aside class="border-right">
    <ScrolledView overflowX="hidden" overflowY="auto">
        <div class="wrapper">
            <a
                href="#artists"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Artists
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            <a
                href="#albums"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Albums
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            <a
                href="#albums"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Songs
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            <hr>

            <a
                href="#queue"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Play Queue
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            <a
                href="#liked"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Liked
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

            <hr>

            <a
                href="#channels"
                class="d-flex justify-content-between align-items-center artist-nav">

                <strong>
                    Channels
                </strong>
                <span class="badge badge-pill">{$artists.length}</span>
            </a>

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
        background-color: #9d9ea0;
        color: #fff;
        padding-top: 3px;
        padding-bottom: 4px;
    }
    .artist-nav {
        width: 280px;
        padding-left: 14px;
        padding-right: 8px;
        padding-top: 5px;
        padding-bottom: 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        color: #333;
        text-decoration: none;
    }
</style>
