<script lang="ts">
    import type { AudioPlayer } from '../core/audio/player';

    import NavBar from './common/NavBar.svelte';
    import PCurrentTrack from './PCurrentTrack.svelte';
    import PPlaybackControls from './PPlaybackControls.svelte';
    import PMiscControls from './PMiscControls.svelte';

    export let player: AudioPlayer;
</script>

<NavBar placement="fixed-bottom" class="bottom-nav border-top">
    <div class="d-flex justify-content-between align-items-center w-100">
        <PCurrentTrack />
        <PPlaybackControls {player} />
        <PMiscControls {player} />
    </div>
</NavBar>

<style>
    :global(.bottom-nav) {
        box-shadow: 0 0.4rem 0.9rem 0.2rem rgba(0,0,0,.125);
    }
</style>