<script lang="ts">
    const COVERART_PLACEHOLDER = "/static/data/im/coverart-placeholder.png";

    export let src = "";
    export let alt = "Cover art";
    export let size = "100px";
</script>

<div class="p-cover" style="--size:{size}">
    <img src={src || COVERART_PLACEHOLDER} {alt} />
    <slot />
</div>

<style>
    .p-cover {
        position: relative;
        width: var(--size);
        height: var(--size);
        background-color: #fff;
        border: 1px solid #999;
        overflow: hidden;
    }
    img {
        padding: 2px;
        width: 100%;
        height: 100%;
    }
</style>