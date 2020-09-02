<script lang="ts">
    let className = "";

    export { className as class };
    export let title: string = "";
</script>

<button class="btn {className}" {title} on:click>
    <slot/>
</button>