<script lang="ts">
    import { currentView } from "../core/store";
    import { ToplevelViews } from "../core/enums/ToplevelViews";
    import type { IChannel } from "../core/interfaces/IChannel";
    import Page from "./common/Page.svelte";
    import Button from "./common/Button.svelte";

    let channel: IChannel;

    $: active = $currentView.toplevel === ToplevelViews.Channel;
    $: if ($currentView.data) {
        channel = $currentView.data;
        console.log(channel);

        if (channel.unique_id !== $currentView.data.unique_id) {
            // get channel
        }
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
            ariaLabel="Play all">
            Play all
        </Button>
    </div>

    <section></section>
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