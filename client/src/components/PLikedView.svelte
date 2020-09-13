<script lang="ts">
    import { currentView, liked } from '../core/store';
    import { playNow } from '../core/playlist';
    import { getHms } from '../core/utils';
    import { ToplevelViews } from '../core/enums/ToplevelViews';
    import type { AudioPlayer } from '../core/audio/player';
    import Button from './common/Button.svelte';
    import PTrackView from "./PTrackView.svelte";

    export let player: AudioPlayer;

    $: duration = getHms($liked.reduce((acc, cur) => acc + cur.length, 0));
</script>

<PTrackView
    class="pb-5"
    indexed
    {player}
    data={$liked}
    active={$currentView.toplevel === ToplevelViews.Liked}>

    <div class="header pb-3">
        <h2>Liked</h2>
        <p class="text-muted"><small>{$liked.length} tracks liked{$liked.length ? `, ${duration[0]} ${duration[1]}` : ''}</small></p>

        <Button
            narrow
            primary
            disabled={!$liked.length}
            on:click={() => playNow(player, $liked)}
            ariaLabel="Play all">
            Play all
        </Button>
    </div>
</PTrackView>

<style>
    h2 {
        font-weight: bold;
    }
</style>