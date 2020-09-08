<h6 class="d-flex justify-content-between">
    <slot/>
    <slot name="actions" />
</h6>

<style type="text/scss">
    @import "../../scss/vars";

    h6 {
        padding-left: 14px;
        padding-right: 8px;
        font-size: 13px;
        opacity: 0.5;
        cursor: default;
    }
    h6 :global(button) {
        border: 0;
    }
</style>