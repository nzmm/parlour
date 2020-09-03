<script lang="ts">
    import { onMount } from "svelte";
    import type { AudioPlayer } from "../core/audio/player";
    import GlyphButton from "./common/GlyphButton.svelte";
    import TextDropshadow from "./common/TextDropshadow.svelte";
    import PPictureInPicture from "./PPictureInPicture.svelte";

    let pipable: boolean = false;
    export let player: AudioPlayer;

    onMount(() => {
        pipable = 'pictureInPictureEnabled' in document;
    });
</script>

<section class="d-flex justify-content-end">
    <TextDropshadow>
        {#if pipable}
        <PPictureInPicture {player} />
        {/if}
        <GlyphButton glyphName="fas fa-volume-up" />
    </TextDropshadow>
</section>

<style>
    section {
        width: 33vw;
    }
</style>
