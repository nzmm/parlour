<script lang="ts">
    import { onMount } from "svelte";
    import { enqueue, enqueueNext, playNow } from '../core/actions';
    import { getLibrary, getAlbumDetails } from "../core/api/queries";
    import type { IArtist } from "../core/interfaces/IArtist";
    import type { ILibraryAlbum } from "../core/interfaces/IAlbum";
    import type { AudioPlayer } from "../core/audio/player";

    import Page from './common/Page.svelte';
    import PTrackListView from "./PTrackListView.svelte";
    import PCoverArt from "./PCoverArt.svelte";

    export let player: AudioPlayer;

    let library: ILibraryAlbum[] = [];
    let loaded = {};

    let root: HTMLElement;

    const initLazyLoading = () => {
        const sections = root.querySelectorAll('section');
        if (sections.length !== library.length) {
            setTimeout(initLazyLoading, 300);
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

    onMount(async () => {
        const res = await getLibrary();
        const data = await res.json();
        library = data.library;
        initLazyLoading();
    });

</script>

<Page bind:root>
    {#each library as release}
    <section class="mb-5 pb-3" data-release={release.id}>
        <div class="d-flex mb-3">
            <PCoverArt src={release.thumbnail} size="80px" />

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
                withQueueActions
                on:play={e => playNow(player, e.detail)}
                on:enqueue={e => enqueue(player, e.detail)}
                on:enqueueNext={e => enqueueNext(player, e.detail)} />
            {:else}
            <p class="text-muted">Loading...</p>
            {/if}
        </div>
    </section>
    {/each}
</Page>

<style>
    h4 > p {
        line-height: .9;
    }
    h4 small {
        font-size: 14px;
    }
</style>