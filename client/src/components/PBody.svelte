<script lang="ts">
    import Router from 'svelte-spa-router';
    import { wrap } from 'svelte-spa-router/wrap';

    import type { AudioPlayer } from "../core/audio/player";
    import PAccount from './PAccount.svelte';
    import PSidebarView from './PSidebarView.svelte';

    export let player: AudioPlayer;

    const routes = {
        '/account': PAccount,
        '*': wrap({ component: PSidebarView, props: { player }})
    }
</script>

<div class="container-fluid h-100 px-0">
    <div class="d-flex h-100 w-100">
        <Router {routes} />
    </div>
</div>

<style>
    .container-fluid {
        padding-top: 60px;
        padding-bottom: 87px;
    }
</style>
