<script lang="ts">
    import { currentTrack } from '../core/store';
    import { likeTrack } from '../core/actions';

    import BoxDropshadow from './common/BoxDropshadow.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PCoverArt from './PCoverArt.svelte';

    $: track = $currentTrack;
</script>

<section class="d-flex align-items-center">
    <BoxDropshadow size="small">
        <PCoverArt
            src={track.thumbnail}
            size="70px" />
    </BoxDropshadow>

    <TextDropshadow>
        <div class="ml-3">
            <p class="m-0 pb-0">
                <strong>
                    <a href="#recording">{track.name}</a>
                </strong>

                {#if track.id}
                <a href="#like" class="px-1" on:click|preventDefault={() => likeTrack(track)}>
                    <i class="{track.liked ? "fas" : "text-muted far"} fa-heart"></i>
                </a>
                {/if}
            </p>
            <p class="m-0 pb-0">
                <small>
                    <a href="#artist">{track.artist_credit}</a>
                </small>
            </p>
        </div>
    </TextDropshadow>
</section>

<style>
    section {
        width: 33vw;
        overflow: hidden;
    }
    a {
        color: #212529;
    }
    .fas.fa-heart {
        color: #ff2a2aff;
    }
</style>