<script lang="ts">
    import { queue } from '../core/store';

    import PTrackListView from "./PTrackListView.svelte";
</script>

<PTrackListView
    heading="Play Queue"
    subheading="{$queue.data.length} songs queued"
    data={$queue.data} />
