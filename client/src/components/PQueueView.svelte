<script lang="ts">
    import { queue } from '../core/store';

    import PTrackView from "./PTrackView.svelte";
</script>

<PTrackView
    heading="Play Queue"
    subheading="{$queue.data.length} songs queued"
    data={$queue.data} />
