<script lang="ts">
    import type { ITrack } from "../core/interfaces/ITrack";
    import Page from "./common/Page.svelte";
    import PTrackListView from './PTrackListView.svelte';

    let className = "";

    export let active: boolean = true;
    export { className as class };
    export let data: ITrack[] = [];
</script>

<Page {active} wide>
    <slot></slot>
    <section class="list {className}">
        <PTrackListView {data}/>
    </section>
</Page>
