<script lang="ts">
import { createDebouncer } from "../../core/utils";

    import DropdownMenu from "./DropdownMenu.svelte";

    export let label: string = "…";

    let ref: HTMLDivElement;
    let visible: boolean = false;
    let left: string = "100%";

    const debounce = createDebouncer();
    const onEnter = () => debounce(() => visible = true);
    const onLeave = () => debounce(() => visible = false);

    $: if (visible && ref) {
        const clientLeft = ref.getBoundingClientRect().left;
        left = clientLeft + 2*200 < window.innerWidth ? "100%" : "-100%";
    }
</script>

<div
    href="#sub-menu"
    class="dropdown-item p-submenu-item"
    bind:this={ref}
    on:mouseenter={onEnter}
    on:mouseleave={onLeave}>

    {label}

    <i class="fas fa-caret-right"></i>

    <DropdownMenu {visible} {left} top={-9} interceptor={false}>
        <slot>
            <em class="dropdown-item disabled">Empty</em>
        </slot>
    </DropdownMenu>
</div>

<style lang="scss">
    .p-submenu-item {
        position: relative;
        padding-right: 8px;
        cursor: pointer;
    }
    .fa-caret-right {
        float: right;
        line-height: 24px;
    }
</style>