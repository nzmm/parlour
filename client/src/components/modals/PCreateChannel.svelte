<script lang="ts">
    import { createEventDispatcher } from "svelte";
    import { createChannel } from "../../core/api/commands";
    import { getChannels } from "../../core/api/queries";
    import { channels } from "../../core/store";
    import Modal from "../common/Modal.svelte";
    import Button from "../common/Button.svelte";

    const dispatch = createEventDispatcher();

    let name: string = "";
    let description: string  = "";
    let is_public: number = 0;

    $: disabled = !name.trim().length;

    const onCreate = async () => {
        const res = await createChannel(name, description, !!is_public);
        const data = await res.json();

        if (data.success) {
            const res = await getChannels();
            const data = await res.json();
            $channels = data.channels;
            dispatch("close");
        }
    }
</script>

<Modal title="Create a channel" on:close>

    <div class="form-group">
        <label for="channel-name">Name</label>
        <input id="channel-name" type="text" class="form-control w-100" bind:value={name} />
    </div>

    <div class="form-group">
        <label for="channel-desc">Description</label>
        <textarea id="channel-desc" class="form-control w-100" bind:value={description}></textarea>
    </div>

    <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" id="channel-public" class="custom-control-input" value={1} bind:group={is_public}>
        <label class="custom-control-label" for="channel-public">Public</label>
    </div>

    <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" id="channel-invite" class="custom-control-input" value={0} bind:group={is_public}>
        <label class="custom-control-label" for="channel-invite">Invite only</label>
    </div>

    <div slot="footer">
        <Button class="mr-1" on:click={() => dispatch("close")}>Cancel</Button>
        <Button {disabled} primary on:click={onCreate}>Create</Button>
    </div>
</Modal>
