<script lang="ts">
    import type { AudioPlayer } from '../core/audio/player';

    import NavBar from './common/NavBar.svelte';
    import PCurrentTrack from './PCurrentTrack.svelte';
    import PPlaybackControls from './PPlaybackControls.svelte';
    import PMiscControls from './PMiscControls.svelte';

    export let player: AudioPlayer;
</script>

<NavBar placement="fixed-bottom" class="border-top">
    <div class="d-flex justify-content-between align-items-center w-100">
        <PCurrentTrack />
        <PPlaybackControls {player} />
        <PMiscControls {player} />
    </div>
</NavBar>
