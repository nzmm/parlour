<script lang="ts">
    import { currentView } from "../core/store";
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import { getChannelTracks } from "../core/api/queries";
    import type { IChannel } from "../core/interfaces/IChannel";
    import type { IChannelTrack } from "../core/interfaces/IChannelTrack";
    import Page from "./common/Page.svelte";
    import Button from "./common/Button.svelte";
    import PChannelListItem from "./PChannelListItem.svelte";

    let channel: IChannel;
    let tracks: IChannelTrack[] = [];

    $: active = $currentView.toplevel === ToplevelViews.Channel;
    $: if ($currentView.data) {
        channel = $currentView.data;
        console.log(channel);

        (async () => {
            const res = await getChannelTracks(channel.unique_id);
            const data = await res.json();
            tracks = data.tracks;
        })();
    }
</script>

{#if active}
<Page wide>
    <div class="header pt-4 pb-3">
        <h2>{ channel.name }</h2>
        <p><small>{ channel.description }</small></p>

        <Button
            narrow
            primary
            ariaLabel="Listen live">
            Listen live
        </Button>

        <Button
            narrow
            primary
            ariaLabel="Play all">
            Play all
        </Button>
    </div>

    <table class="w-100">
        <tbody>
            {#each tracks as item}
            <PChannelListItem
                {item}  />
            {/each}
        </tbody>
    </table>
</Page>
{/if}

<style lang="scss">
    .header {
        padding-left: 24px;
        padding-right: 24px;
    }
    h2 {
        font-weight: bold;
    }
</style>