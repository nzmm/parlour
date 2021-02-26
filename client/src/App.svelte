<script lang="ts">
    import { onMount } from "svelte";
    import { bootstrapTW } from "./core/bootstrap";
    import { user } from "./core/store";
    import { registerGlobalKeyUpHandler } from "./core/keys";
    import { AudioPlayer } from './core/audio/player';
    import PHeader from './components/PHeader.svelte';
    import PBody from './components/PBody.svelte';
    import PFooter from './components/PFooter.svelte';
    import PSplash from "./components/PSplash.svelte";

    const player = new AudioPlayer();

    let ready: boolean = false;
    let trackCount: number = 0;

    onMount(async () => {
        const session = await bootstrapTW();
        user.set(session.user);
        trackCount = session.trackCount;

        setTimeout(() => ready = true, 500);
        return registerGlobalKeyUpHandler(" ", () => player.toggle());
    });
</script>

<main>
    <PHeader user={$user} />
    <PBody {player} {trackCount} />
    <PFooter {player} />
    <PSplash {ready} />
</main>
