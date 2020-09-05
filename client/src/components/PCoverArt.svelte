<script lang="ts">
    const COVERART_PLACEHOLDER = "/static/data/im/coverart-placeholder.png";

    export let src = "";
    export let alt = "Cover art";
    export let size = "100px";
</script>

<div class="p-cover" style="--size:{size}">
    <img src={src || COVERART_PLACEHOLDER} {alt} />
</div>

<style>
    .p-cover {
        width: var(--size);
        height: var(--size);
        background-color: #fff;
        border: 1px solid #999;
    }
    img {
        padding: 3px;
        width: 100%;
        height: 100%;
    }
</style>