<script lang="ts">
    let className = "";

    export { className as class };
</script>

<button class="btn {className}" on:click >
    <slot/>
</button>