<script lang="ts">
    const COVERART_PLACEHOLDER = "/static/data/im/coverart-placeholder.png";

    export let src = "";
    export let alt = "Cover art";
    export let size = "100px";
    export let playing: boolean = false;
</script>

<div class="p-cover" class:playing style="--size:{size}">
    <img src={src || COVERART_PLACEHOLDER} {alt} />
    {#if playing}
        <div class="p-badge">
            <i class="fas fa-play"></i>
        </div>
    {/if}
</div>

<style>
    .p-cover {
        width: var(--size);
        height: var(--size);
        background-color: #fff;
        border: 1px solid #999;
        border-radius: 3%;
    }
    .p-cover > img {
        padding: 4%;
        width: 100%;
        height: 100%;
    }
    .p-badge {
        position: relative;
    }
    .p-badge > i {
        color: #fff;
        position: absolute;
        font-size: 130%;
        margin: 6%;
        bottom: -100%;
        right: 5%;
        padding-bottom: 5%;
        text-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
</style>