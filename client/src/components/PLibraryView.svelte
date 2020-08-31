<script lang="ts">
    import { currentView, library, libraryFilter } from '../core/store';
    import { enqueue, enqueueNext, playNow, likeTrack } from '../core/actions';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { ILibraryAlbum } from "../core/interfaces/IAlbum";
    import type { AudioPlayer } from "../core/audio/player";
    import type { ITrack } from "../core/interfaces/ITrack";
    import Page from './common/Page.svelte';
    import PTrackListView from "./PTrackListView.svelte";
    import PCoverArt from "./PCoverArt.svelte";
    import DropdownMenu from "./common/DropdownMenu.svelte";

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

    const initLazyLoading = (releases: ILibraryAlbum[]) => {
        const sections = root?.querySelectorAll('section');
        console.log(releases.length, sections?.length);

        if (!sections || sections.length !== releases.length) {
            setTimeout(() => initLazyLoading(releases), 300);
            return;
        }

        const options: IntersectionObserverInit = {
            root,
            rootMargin: '0px',
            threshold: 0.1
        }

        const callback: IntersectionObserverCallback = entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const elem = entry.target as HTMLElement;
                    loaded[elem.dataset.release] = true;
                }
            });
        }

        const observer = new IntersectionObserver(callback, options);
        sections.forEach(s => observer.observe(s));
    }

    libraryFilter.subscribe(() => {
        loaded = {};
    });

    $: active = $currentView.toplevel === ToplevelViews.Songs;

    $: if (active) {
        releases = $libraryFilter.fn($library);
        setTimeout(() => initLazyLoading(releases), 150);
    }
</script>

<Page {active} bind:root>
    {#each releases as release}
    <section class="mb-5 pb-3" data-release={release.id}>
        <div class="d-flex mb-3">
            <PCoverArt src={loaded[release.id] ? release.thumbnail : ""} size="100px" />

            <h4 class="pl-4">
                {release.name}

                <p class="text-muted">
                    <small>{release.artist_name}<br/>{release.year}</small>
                </p>
            </h4>
        </div>

        <div style="height: {37 * release.track_count}px">
            {#if loaded[release.id]}
            <PTrackListView
                data={release.tracks}
                on:dropdown={showDropdown}
                on:play={e => playNow(player, e.detail)} />
            {:else}
            <p class="text-muted">Loading...</p>
            {/if}
        </div>
    </section>
    {/each}
</Page>

<DropdownMenu {visible} {top} {left} on:hide={() => visible = false}>
    <a class="dropdown-item" href="#play" on:click|preventDefault={() => playNow(player, track)}>
        Play
    </a>

    <div class="dropdown-divider"></div>

    <a class="dropdown-item" href="#enqueue" on:click|preventDefault={() => enqueue(player, track)}>
        Add to queue
    </a>
    <a class="dropdown-item" href="#next" on:click|preventDefault={() => enqueueNext(player, track)}>
        Play next
    </a>

    <div class="dropdown-divider"></div>

    <a class="dropdown-item" href="#like" on:click|preventDefault={() => likeTrack(track)}>
        Like
    </a>
</DropdownMenu>

<style>
    h4 > p {
        line-height: .9;
    }
    h4 small {
        font-size: 14px;
    }
</style>