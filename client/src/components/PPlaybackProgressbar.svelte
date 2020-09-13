<script lang="ts">
    import { getHms } from '../core/utils';

    export let length: number = 0;
    export let position: number = 0;

    $: positionHms = getHms(position);
    $: lengthHms = getHms(length);
    $: percent = `${length > 0 ? position / length * 100 : 0}%`;
</script>

<div class="progressbar d-flex align-items-center mt-2 px-2">
    <div class="hms text-muted mr-2">{positionHms}</div>
    <div class="bg" role="progressbar">
        <div class="bar" style="width: {percent}"></div>
    </div>
    <div class="hms text-muted ml-2">{lengthHms}</div>
</div>

<style>
    .progressbar {
        width: 100%;
    }
    .progressbar > .hms {
        font-size: small;
    }
    .progressbar > .bg {
        width: 100%;
        height: 4px;
        background-color: #adadadff;
    }
    .progressbar > .bg > .bar {
        background-color: #ff2a2aff;
        height: 100%;
    }
</style>