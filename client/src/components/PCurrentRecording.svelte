<script lang="ts">
    import type { ICurrentRecording } from '../core/interfaces/ICurrentRecording';

    import BoxDropshadow from './common/BoxDropshadow.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PCoverArt from './PCoverArt.svelte';

    export let currentRecording: ICurrentRecording = {
        id: "",
        title: "Villans",
        coverArt: "/static/data/im/albumart.png",
        artistName: "Queens of the Stone Age",
        albumName: "Villans",
        duration: 123,
        position: 10
    }
</script>

<section class="d-flex align-items-center">
    <BoxDropshadow size="small">
        <PCoverArt
            src={currentRecording.coverArt}
            size="70px" />
    </BoxDropshadow>
    <TextDropshadow>
        <div class="ml-3">
            <p class="m-0 pb-0">
                <strong>
                    <a href="#recording">{currentRecording.title}</a>
                </strong>
                &nbsp;
                <a href="#like">
                    <i class="far fa-heart text-muted px-1"></i>
                </a>
            </p>
            <p class="m-0 pb-0">
                <small>
                    <a href="#artist">{currentRecording.artistName}</a>
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