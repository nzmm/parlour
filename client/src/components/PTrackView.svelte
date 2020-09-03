<script lang="ts">
    import { enqueue, enqueueNext, playNow, likeTrack } from '../core/actions';
    import type { AudioPlayer } from '../core/audio/player';
    import type { ITrack } from "../core/interfaces/ITrack";
    import Page from "./common/Page.svelte";
    import DropdownMenu from "./common/DropdownMenu.svelte";
    import PTrackListView from './PTrackListView.svelte';

    let className = "";

    export let player: AudioPlayer;
    export let active: boolean = true;
    export { className as class };
    export let data: ITrack[] = [];

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
</script>

<Page {active} wide>
    <slot></slot>
    <section class="list {className}">
        <PTrackListView
            {data}
            on:dropdown={showDropdown}
            on:play={e => playNow(player, e.detail, data)} />
    </section>
</Page>

<DropdownMenu {visible} {top} {left} on:hide={() => visible = false}>
    <a class="dropdown-item" href="#play" on:click|preventDefault={() => playNow(player, track, data)}>
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

