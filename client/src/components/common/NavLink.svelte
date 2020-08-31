<script lang="ts">
    let className = "";

    export { className as class };
    export let label = "";
    export let href = "#";
    export let count = null;
    //export let active: boolean = false;
</script>

<a
    {href}
    class="d-flex justify-content-between align-items-center side-nav {className}"
    on:click
    >
    <strong>{label}</strong>
    {#if count != null}
    <span class="badge badge-pill">{count}</span>
    {/if}
</a>

<style>
    .badge {
        background-color: #9d9ea0;
        color: #fff;
        padding-top: 3px;
        padding-bottom: 4px;
    }
    .side-nav {
        width: 280px;
        padding-left: 14px;
        padding-right: 8px;
        padding-top: 5px;
        padding-bottom: 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        color: #333;
        text-decoration: none;
    }
</style>
