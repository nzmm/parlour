<script lang="ts">
    import type { ITrack } from "../core/interfaces/ITrack";

    import Page from "./common/Page.svelte";
    import PTrackListView from './PTrackListView.svelte';

    export let heading = "";
    export let subheading = "";
    export let data: ITrack[] = [];
    export let withQueueActions: boolean = false;
</script>

<Page {heading} {subheading} wideBody>
    <section class="list">
        <PTrackListView
            {data}
            {withQueueActions}
            on:play
            on:enqueue
            on:enqueueNext />
    </section>
</Page>
