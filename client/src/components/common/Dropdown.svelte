<script lang="ts">
    import DropdownMenu from "./DropdownMenu.svelte";

    let visible: boolean = false;
    let top: number = 0;
    let left: number = 0;

    const showDropdown = (event: MouseEvent) => {
        const element = event.currentTarget as HTMLElement;
        const rect = element.getBoundingClientRect();
        visible = true;
        top = rect.top + rect.height - 5;
        left = rect.left;
    };
</script>

<div class="p-drop">
    <div class="p-drop-toggle" on:click={showDropdown}>
        <slot name="toggle">
            <i class="fas fa-caret-down p-2"></i>
        </slot>
    </div>

    <DropdownMenu {visible} {top} {left}>
        <slot />
    </DropdownMenu>
</div>