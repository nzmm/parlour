<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { ITrack } from '../core/interfaces/ITrack';

    import Page from './common/Page.svelte';
    import PCoverArt from './PCoverArt.svelte';
    import PTrackListView from './PTrackListView.svelte';

    export let heading: string = "";
    export let subheading1: string = "";
    export let subheading2: string | number = "";
    export let thumbnail: string = "";
    export let tracks: ITrack[] = [];

    const dispatch = createEventDispatcher();
</script>

<Page>
    <div class="d-flex justify-content-between align-items-top" slot="header">
        <div class="d-flex">
            <PCoverArt src={thumbnail} size="170px" />

            <h2 class="pl-4">
                {heading}

                <p class="text-muted">
                    <small>{subheading1}<br/>{subheading2}</small>
                </p>
            </h2>
        </div>

        <a href="#back" title="Back to albums" on:click|preventDefault={() => dispatch("back", {})}>
            <i class="fas fa-times"></i>
        </a>
    </div>

    <hr/>

    <PTrackListView
        data={tracks}
        withQueueActions
        on:play
        on:enqueue
        on:enqueueNext />
</Page>

<style>
    h2 {
        font-weight: bold;
    }
    h2 > p {
        line-height: .9;
    }
    h2 small {
        font-size: 18px;
    }
</style>