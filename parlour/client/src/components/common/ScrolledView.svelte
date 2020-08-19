<script lang="ts">
    export let overflowX: "auto" | "visible" | "hidden" | "scroll" = "auto";
    export let overflowY: "auto" | "visible" | "hidden" | "scroll" = "auto";
</script>

<div role="region" class="w-100 h-100" style="overflow-x: {overflowX}; overflow-y: {overflowY};">
    <slot />
</div>
