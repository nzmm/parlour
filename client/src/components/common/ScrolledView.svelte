<script lang="ts">
    export let overflowX: "auto" | "visible" | "hidden" | "scroll" = "auto";
    export let overflowY: "auto" | "visible" | "hidden" | "scroll" = "auto";
    export let root: HTMLElement = null;

    let className = "";
    export { className as class };
</script>

<div
    role="region"
    class="w-100 h-100 {className}"
    style="overflow-x: {overflowX}; overflow-y: {overflowY};"
    bind:this={root}>
    <slot />
</div>