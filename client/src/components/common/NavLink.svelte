<script lang="ts">
    let className = "";

    export { className as class };
    export let label = "";
    export let href = "#";
    export let active: boolean = false;
</script>

<li class="px-3 {className}" class:active>
    <a class="nav-link px-0" {href} on:click|preventDefault>
        {label}
    </a>
</li>

<style>
    li {
        list-style-type: none;
        font-size: 14px;
    }
    li.active {
       background-color: #ff2a2aff;
    }
    li a {
        color: #333;
    }
    li.active a {
        color: #fff;
    }
</style>
