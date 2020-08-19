<script lang="ts">
    import GlyphButton from "./common/GlyphButton.svelte";
    import TextDropshadow from "./common/TextDropshadow.svelte";
</script>

<section class="d-flex flex-column align-items-center">
    <div class="d-flex align-items-center">
        <TextDropshadow><GlyphButton glyphName="fa-random" /></TextDropshadow>
        <TextDropshadow><GlyphButton glyphName="fa-fast-backward" /></TextDropshadow>
        <TextDropshadow><GlyphButton glyphName="fa-play" /></TextDropshadow>
        <TextDropshadow><GlyphButton glyphName="fa-fast-forward" /></TextDropshadow>
        <TextDropshadow><GlyphButton glyphName="fa-redo" /></TextDropshadow>
    </div>

    <div class="progressbar d-flex align-items-center mt-2 px-2">
        <span class="text-muted px-2">1:12</span>
        <div>
            <div style="width: {'55%'}"></div>
        </div>
        <span class="text-muted px-2">3:58</span>
    </div>
</section>

<style>
    section {
        width: 33vw;
    }
    .progressbar {
        width: 100%;
    }
    .progressbar > span {
        font-size: small;
        overflow: hidden;
    }
    .progressbar > div {
        width: 100%;
        height: 4px;
        background-color: #adadadff;
    }
    .progressbar > div > div {
        background-color: #ff2a2aff;
        height: 100%;
    }
</style>