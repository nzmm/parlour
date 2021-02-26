<script lang="ts">
    import { library, breadcrumbs } from '../core/store';
    import { enqueueNext, playNow } from '../core/playlist';
    import { intersectionObservable } from '../core/observable';
    import { currentTrack, playerState } from '../core/store';
    import { PlaybackState } from '../core/enums/PlaybackState';
    import type { ILibraryAlbum } from "../core/interfaces/IAlbum";
    import type { AudioPlayer } from "../core/audio/player";
    import type { ITrack } from "../core/interfaces/ITrack";
    import Page from './common/Page.svelte';
    import PCoverArt from "./PCoverArt.svelte";
    import PTrackListDropdown from './PTrackListDropdown.svelte';
    import PLibraryListItem from './PLibraryListItem.svelte';

    export let context = '';
    export let params: { id?: string }
    export let player: AudioPlayer;

    let releases: ILibraryAlbum[] = [];
    let loaded = {};

    let root: HTMLElement;
    let track: ITrack = null;
    let visible: boolean = false;
    let top: number = 0;
    let left: number = 0;

    const showDropdown = (event: CustomEvent) => {
        visible = true;
        top = event.detail.top;
        left = event.detail.left;
        track = event.detail.item;
    };

    const onPlayAlbum = (release: ILibraryAlbum) => {
        enqueueNext(player, release.tracks);
    }

    const getRealeases = (library: ILibraryAlbum[]) => {
        if (!params?.id) {
            return library;
        }

        const filter_id = parseInt(params.id);
        switch(context) {
            case 'artists':
                return library.filter(x => x.artist_id === filter_id);
            case 'albums':
                return library.filter(x => x.id === filter_id);
            default:
                return library;
        }
    }

    $: {
        console.log(params, context);
        releases = getRealeases($library);

        if (releases.length) {
            intersectionObservable(
                root,
                "section",
                releases,
                (e: HTMLElement) => { loaded[e.dataset.release] = true; });
        }
    }
</script>

<Page bind:root>
    {#if $breadcrumbs}
    <div class="breadcrumbs pb-4">
        {#each $breadcrumbs as crumb}
            {#if crumb.navigateTo}
            <a href="#back" class="crumb" on:click|preventDefault={() => crumb.navigateTo()}>{crumb.label}</a>
            <span class="crumb caret">〉</span>
            {:else}
            <span class="crumb">{crumb.label}</span>
            {/if}
        {/each}
    </div>
    {/if}

    {#each releases as release}
    <section class="mb-5 pb-3" data-release={release.id}>
        {#if loaded[release.id]}
        <div class="d-flex mb-3">
            <PCoverArt src={release.thumbnail} size="100px">
                <button on:click={() => onPlayAlbum(release)} title="Play album">
                    <i class="fas fa-play"></i>
                </button>
            </PCoverArt>

            <h4 class="pl-4 pt-2">
                {release.name}

                <p class="text-muted">
                    <small>
                        {release.artist_name || '?'} &middot; {release.year || '?'}<br/>
                    </small>
                </p>
            </h4>
        </div>

        <table class="w-100">
            <tbody>
                {#each release.tracks as item, i}
                <PLibraryListItem
                    {item}
                    number={item.number}
                    current={item.id === $currentTrack.id}
                    playing={$playerState.state === PlaybackState.Playing}
                    on:dropdown={showDropdown}
                    on:play={e => playNow(player, [e.detail])} />
                {/each}
            </tbody>
        </table>
        {:else}
        <!-- Placeholder -->
        <div class="placeholder-banner mb-3">
            <PCoverArt size="100px" />
        </div>
        <div style="height: {37 * release.track_count}px"></div>
        {/if}
    </section>
    {/each}
</Page>

<PTrackListDropdown
    {player}
    {track}
    {visible}
    {top}
    {left}
    on:hide={() => visible = false} />

<style>
    h4 > p {
        line-height: .9;
    }
    h4 small {
        font-size: 14px;
    }
    button {
        border: 0;
        outline: 0;
        font-size: 200%;
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        color: #fff;
        background-color: rgba(0, 0, 0, .25);
        opacity: 0;
        transition: opacity .5s;
        overflow: hidden;
    }
    button:hover {
        opacity: 1;
    }
    .placeholder-banner {
        height: 100px;
    }
    .crumb {
        color: #999;
        padding-right: 6px;
        font-size: 15px;
    }
    .caret {
        font-size: 11px;
    }
</style>