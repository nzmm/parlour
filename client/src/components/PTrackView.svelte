<script lang="ts">
    import type { ITrack } from "../core/interfaces/ITrack";

    import ScrolledView from "./common/ScrolledView.svelte";
    import PTrackListView from './PTrackListView.svelte';

    export let heading = "";
    export let subheading = "";
    export let data: ITrack[] = [];
    export let withQueueActions: boolean = false;

</script>

<ScrolledView overflowX="hidden" overflowY="scroll">
    <div class="wrapper mx-2 pt-5">
        <header>
            <h2>
                {heading}
                <small class="text-muted">
                    {subheading}
                </small>
            </h2>
        </header>

        <section class="list py-4">
            <PTrackListView
                {data}
                {withQueueActions}
                on:play
                on:enqueue
                on:enqueueNext />
        </section>
    </div>
</ScrolledView>

<style>
    h2 {
        padding-left: 24px;
        font-weight: bold;
    }
    h2 > small {
        font-size: 18px;
    }
</style>