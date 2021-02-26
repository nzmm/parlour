<script lang="ts">
    import { link } from 'svelte-spa-router';
    import { DropdownPlacement } from "../core/enums/DropdownPlacement";
    import type { IUser } from "../core/interfaces/IUser";
    import TextDropshadow from "./common/TextDropshadow.svelte";
    import Dropdown from "./common/Dropdown.svelte";

    export let user: IUser;
</script>

<Dropdown placement={DropdownPlacement.BottomRight}>
    <button class="user btn p-0" style="margin-top: 1px;" slot="toggle">
        <TextDropshadow size="smallest">
            <strong>{user.initials}</strong>
        </TextDropshadow>
    </button>

    <h6 class="dropdown-header">{user.full_name}</h6>

    <a class="dropdown-item" href="/account" use:link>
        Account
    </a>
    <a class="dropdown-item" href="/accounts/logout/">
        Log out
    </a>
    <a class="dropdown-item" href="/admin/" target="_blank">
        Admin
    </a>

    <div class="dropdown-divider"></div>

    <a class="dropdown-item" href="https://github.com/nzmm/totallywired" target="_blank">
        Github
    </a>
</Dropdown>

<style>
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