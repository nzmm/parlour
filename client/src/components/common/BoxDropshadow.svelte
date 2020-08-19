<script lang="ts">
    export let size: "smallest" | "small" | "normal" | "big" | "biggest" = "normal";
</script>

<div class="dropshadow {size}">
    <slot />
</div>

<style>
    .dropshadow.smallest :global(div) {
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    }

    .dropshadow.small :global(div) {
        box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    }

    .dropshadow.normal :global(div) {
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    }

    .dropshadow.big :global(div) {
        box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
    }

    .dropshadow.biggest :global(div) {
        box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
    }
</style>
