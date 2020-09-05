<script lang="ts">
import { DropdownPlacement } from '../core/enums/DropdownPlacement';

import Dropdown from './common/Dropdown.svelte';
    import NavBar from './common/NavBar.svelte';
    import TextDropshadow from './common/TextDropshadow.svelte';
    import PSearchMusicInput from "./PSearchMusicInput.svelte";
</script>

<NavBar class="top-nav border-bottom d-flex justify-content-between align-items-center">
    <a class="navbar-brand pr-2" href="/">
        <img src="/static/data/im/parlour-brand-32.png" alt="Parlour" height="32" />
    </a>

    <PSearchMusicInput />

    <Dropdown placement={DropdownPlacement.BottomRight}>
        <button class="user btn p-0" style="margin-top: 1px;" slot="toggle">
            <TextDropshadow size="smallest">
                <strong>MM</strong>
            </TextDropshadow>
        </button>

        <a class="dropdown-item" href="/accounts/logout/">
            Log out
        </a>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/admin/">
            Admin
        </a>

    </Dropdown>

</NavBar>

<style>
    :global(.top-nav) {
        box-shadow: 0 -0.4rem 0.9rem 0.2rem rgba(0,0,0,.175);
    }
    .user {
        width: 36px;
        height: 36px;
        border-radius: 4px;
        background-color: #adadadff;
        color: #fff;
        line-height: 36px;
        text-align: center;
    }
</style>