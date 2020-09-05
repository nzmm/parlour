<script lang="ts">
    import { DropdownPlacement } from "../../core/enums/DropdownPlacement";
    import DropdownMenu from "./DropdownMenu.svelte";

    export let placement: DropdownPlacement = DropdownPlacement.BottomLeft;

    let visible: boolean = false;
    let top: number = 0;
    let left: number = 0;

    const showDropdown = (event: MouseEvent) => {
        const element = event.currentTarget as HTMLElement;
        const rect = element.getBoundingClientRect();
        visible = true;

        top = rect.top + rect.height;

        switch (placement) {
            case DropdownPlacement.BottomRight:
                left = rect.left + rect.width - 200;
                break;
            case DropdownPlacement.BottomLeft:
            default:
                left = rect.left;
                break;
        }
    };
</script>

<div class="p-drop">
    <div class="p-drop-toggle" on:click={showDropdown}>
        <slot name="toggle">
            <i class="fas fa-caret-down p-2"></i>
        </slot>
    </div>

    <DropdownMenu {visible} {top} {left} on:hide={() => visible = false}>
        <slot />
    </DropdownMenu>
</div>