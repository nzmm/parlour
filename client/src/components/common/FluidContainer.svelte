<script lang="ts">
    let className = "";
    export { className as class };
</script>

<div class="container-fluid {className}">
    <slot />
</div>

<style>
    .container-fluid {
        padding: 0;
        height: 100%;
    }
</style>