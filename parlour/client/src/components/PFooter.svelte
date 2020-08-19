<script>
    import NavBar from './common/NavBar.svelte';
    import PCurrentRecording from './PCurrentRecording.svelte';
    import PPlaybackControls from './PPlaybackControls.svelte';
    import PMiscControls from './PMiscControls.svelte';
</script>

<NavBar placement="fixed-bottom" class="border-top">
    <div class="d-flex justify-content-between align-items-center w-100">
        <PCurrentRecording />
        <PPlaybackControls />
        <PMiscControls />
    </div>
</NavBar>
