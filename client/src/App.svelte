<script lang="ts">
	import { AudioPlayer } from './core/audio/player';

	import PHeader from './components/PHeader.svelte';
	import PBody from './components/PBody.svelte';
	import PFooter from './components/PFooter.svelte';

	const player = new AudioPlayer();
</script>

<main>
	<PHeader />
	<PBody {player} />
	<PFooter {player} />
</main>

<style>
</style>
