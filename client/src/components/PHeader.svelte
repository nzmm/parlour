<script lang="ts">
    import type { IUser } from '../core/interfaces/IUser';
    import NavBar from './common/NavBar.svelte';
    import PSearchMusicInput from "./PSearchMusicInput.svelte";
    import PUserDropdown from './PUserDropdown.svelte';

    export let user: IUser = null;
</script>

<NavBar class="top-nav border-bottom d-flex justify-content-between align-items-center">
    <a class="navbar-brand pr-2" href="/" id="totallywired">
        <img src="/static/data/im/tw-monogram-logo.png" alt="Totally Wired" height="32" />
    </a>

    <PSearchMusicInput />

    {#if user}
    <PUserDropdown {user} />
    {/if}
</NavBar>

<style>
    :global(.top-nav) {
        box-shadow: 0 -0.4rem 0.9rem 0.2rem rgba(0,0,0,.175);
    }
</style>