<script lang="ts">
    let className = "";

    export { className as class };
    export let label = "";
    export let href = "#";
    export let active: boolean = false;
</script>

<li class="nav-item mx-2 {className}" class:active>
    <a class="nav-link px-0" {href} on:click|preventDefault>{label}</a>
</li>

<style>
    .nav-link {
	    padding-top: 12px;
	    padding-bottom: 4px;
    }
    .nav-item.active {
	    border-bottom: 3px solid #ff2a2aff;
    }
</style>
