<script lang="ts">
    let className = "";

    export { className as class };
    export let label = "";
    export let href = "#";
    export let active: boolean = false;
</script>

<li class="px-2 {className}" class:active>
    <a class="nav-link px-0" {href} on:click>
        {label}
        <slot/>
    </a>
</li>

<style>
</style>
