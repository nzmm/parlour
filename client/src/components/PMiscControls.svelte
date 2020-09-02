<script>
    import GlyphButton from "./common/GlyphButton.svelte";
    import TextDropshadow from "./common/TextDropshadow.svelte";
    import PPictureInPicture from "./PPictureInPicture.svelte";
</script>

<section class="d-flex justify-content-end">
    <TextDropshadow>
        <PPictureInPicture />
        <GlyphButton glyphName="fas fa-volume-up" />
    </TextDropshadow>
</section>

<style>
    section {
        width: 33vw;
    }
</style>
