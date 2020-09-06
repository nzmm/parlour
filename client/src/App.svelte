<script lang="ts">
    import { onMount } from "svelte";
    import { getLibrary } from "./core/api/queries";
    import { library, artists } from "./core/store";
	import { AudioPlayer } from './core/audio/player';
	import Loader from "./components/common/Loader.svelte";
	import PHeader from './components/PHeader.svelte';
	import PBody from './components/PBody.svelte';
	import PFooter from './components/PFooter.svelte';

	const player = new AudioPlayer();

	let ready: boolean = false;
    let trackCount: number = 0;

    onMount(async () => {
        const res = await getLibrary();
        const data = await res.json();
        trackCount = data.track_count;
        $artists = data.artists;
        $library = data.releases;

		setTimeout(() => {
			ready = true;
		}, 500);
    });
</script>

<main>
	{#if ready}
	<PHeader />
	<PBody {player} {trackCount} />
	<PFooter {player} />
	{:else}
	<div class="loader d-flex justify-content-center align-items-center">
		<Loader bold scale={1.25} />
	</div>
	{/if}
</main>

<style type="text/scss">
	@import "./scss/vars";

	.loader {
		z-index: 9999999;
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background-color: $colour-white;

		:global(.lds-roller div::after) {
			background-color: $colour-primary !important;
		}
	}
</style>
