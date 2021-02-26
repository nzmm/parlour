<script lang="ts">
    import { fade } from "svelte/transition";
    import Loader from "./common/Loader.svelte";

    export let ready: boolean = false;
</script>

{#if !ready}
    <div
        transition:fade
        class="loader d-flex justify-content-center align-items-center"
    >
        <Loader bold scale={1.25} />
    </div>
{/if}

<style type="text/scss">
    @import "../scss/vars";

    .loader {
        z-index: 1100;
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        background-color: $colour-white;
    }
</style>
