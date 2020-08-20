<script lang="ts">
    import { currentTrack } from '../core/store';
    import { getThumbnail } from '../core/api/queries';

    import BoxDropshadow from './common/BoxDropshadow.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PCoverArt from './PCoverArt.svelte';

    const getThumb = async (id: string) => {
        const res = await getThumbnail(id);
        const data = await res.json();
        console.log(data);

        currentTrack.update(cur => ({
            ...cur,
            thumbnail: data.thumbnail
        }));
    };

    $: {
        const { id, thumbnail } = $currentTrack;
        if (id && !thumbnail) {
            getThumb(id);
        }
    }
</script>

<section class="d-flex align-items-center">
    <BoxDropshadow size="small">
        <PCoverArt
            src={$currentTrack.thumbnail}
            size="70px" />
    </BoxDropshadow>
    <TextDropshadow>
        <div class="ml-3">
            <p class="m-0 pb-0">
                <strong>
                    <a href="#recording">{$currentTrack.name}</a>
                </strong>
                {#if $currentTrack.id}
                &nbsp;
                <a href="#like">
                    <i class="far fa-heart text-muted px-1"></i>
                </a>
                {/if}
            </p>
            <p class="m-0 pb-0">
                <small>
                    <a href="#artist">{$currentTrack.artist_credit}</a>
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
</style>