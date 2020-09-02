<script lang="ts">
    import { currentTrack } from '../core/store';
    import { getThumbnail } from '../core/api/queries';
    import { likeTrack } from '../core/actions';

    import BoxDropshadow from './common/BoxDropshadow.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PCoverArt from './PCoverArt.svelte';
import PPictureInPicture from './PPictureInPicture.svelte';

    const getThumb = async (id: number) => {
        console.log('Fetching thumbnail...',  id);
        const res = await getThumbnail(id);
        const data = await res.json();
        console.log(`Thumbnail url response... "${data.thumbnail}"`);

        if (!data.thumbnail) {
            return;
        }

        currentTrack.update(cur => ({
            ...cur,
            thumbnail: data.thumbnail
        }));
    };

    $: track = $currentTrack;

    $: if (track.id && !track.thumbnail) {
        getThumb(track.id);
    }
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