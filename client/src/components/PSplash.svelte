<script lang="ts">
    import { fade } from "svelte/transition";
    import type { IUser } from "../core/interfaces/IUser";
    import Loader from "./common/Loader.svelte";

    export let user: IUser;
    export let ready: boolean = false;
</script>

{#if user && !user.providers.length}
<div class="no-providers d-flex justify-content-center align-items-center">
    <div>
        <p>Hi {user.full_name},</p>
        <a href="/providers/graph_signin">Please begin by connecting Parlour to your OneDrive&hellip;</a>
    </div>
</div>
<div class="emergency-exit">
    <a href="/accounts/logout/" title="Log out">
        <i class="far fa-times-circle"></i>
    </a>
</div>
{/if}
{#if !ready}
<div transition:fade class="loader d-flex justify-content-center align-items-center">
    <Loader bold scale={1.25} />
</div>
{/if}

<style type="text/scss">
	@import "../scss/vars";

	.loader,
	.no-providers {
		z-index: 1100;
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background-color: $colour-white;
	}
	.loader {
		:global(.lds-roller div::after) {
			background-color: $colour-primary !important;
		}
	}
	.emergency-exit {
		z-index: 1100;
		position: fixed;
		top: 15px;
		right: 20px;
		font-size: 25px;
	}
</style>