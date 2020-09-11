<h6 class="d-flex justify-content-between">
    <slot/>
    <slot name="actions" />
</h6>

<style type="text/scss">
    @import "../../scss/vars";

    h6 {
        margin-top: 5px;
        margin-bottom: 5px;
        padding-left: 14px;
        padding-right: 8px;
        font-size: 13px;
        font-weight: bold;
        color: $colour-grey-dark;
        cursor: default;
    }
    h6 :global(button) {
        border: 0;
        padding-top: 3px;
        padding-bottom: 3px;
        color: $colour-grey-medium;
        opacity: 0.8;
        transition: opacity .3s;
    }
    h6 :global(button:hover, button:active, button:focus) {
        opacity: 1;
    }
</style>