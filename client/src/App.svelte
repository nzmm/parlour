<script lang="ts">
    import { onMount } from "svelte";
    import { getCurrentUser, getLibrary } from "./core/api/queries";
    import { library, artists } from "./core/store";
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

    const initUser = async () => {
        const res = await getCurrentUser();
        const data = await res.json();
        user = data.user;
    }

    const initLibrary = async () => {
        const res = await getLibrary();
        const data = await res.json();
        trackCount = data.track_count;
        $artists = data.artists;
        $library = data.releases;
    }

    onMount(async () => {
        await initUser();
        await initLibrary();

        setTimeout(() => {
            ready = true;
        }, 500);
    });
</script>

<main>
    <PHeader {user} />
    <PBody {player} {trackCount} />
    <PFooter {player} />
    <PSplash {ready} {user} />
</main>
