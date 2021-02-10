<script lang="ts">
    import { onMount } from "svelte";
    import { bootstrapTW } from "./core/bootstrap";
    import { registerGlobalKeyUpHandler } from "./core/keys";
    import { AudioPlayer } from './core/audio/player';
    import type { IUser } from './core/interfaces/IUser';
    import PHeader from './components/PHeader.svelte';
    import PBody from './components/PBody.svelte';
    import PFooter from './components/PFooter.svelte';
    import PSplash from "./components/PSplash.svelte";

    const player = new AudioPlayer();

    let user: IUser;
    let ready: boolean = false;
    let trackCount: number = 0;

    onMount(async () => {
        ({ user, trackCount } = await bootstrapTW());

        setTimeout(() => {
                ready = true;
        }, 500);

        return registerGlobalKeyUpHandler(" ", () => player.toggle());
    });
</script>

<main>
    <PHeader {user} />
    <PBody {player} {trackCount} />
    <PFooter {player} />
    <PSplash {ready} {user} />
</main>
