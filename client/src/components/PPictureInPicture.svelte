<script lang="ts">
    import type { AudioPlayer } from "../core/audio/player";
    import GlyphButton from "./common/GlyphButton.svelte";

    export let player: AudioPlayer;

    /* Picture in Picture */
    // https://googlechrome.github.io/samples/picture-in-picture/audio-playlist

    /* Picture-in-Picture Canvas */

    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 170;

    const video = document.createElement('video');
    video.srcObject = canvas.captureStream();
    video.muted = true;

    const showPictureInPictureWindow = async () => {
        if (!navigator?.mediaSession?.metadata) {
            return;
        }

        const image = new Image();
        image.src = [...navigator.mediaSession.metadata.artwork].pop().src;
        await image.decode();

        canvas.getContext('2d').drawImage(image, 0, 0, 170, 170);
        await video.play();
        await video.requestPictureInPicture();
    }

    /* Previous Track & Next Track */

    navigator.mediaSession.setActionHandler('previoustrack', () => {
    });

    navigator.mediaSession.setActionHandler('nexttrack', () => {
        player.playNext();
    });

    /* Play & Pause */

    navigator.mediaSession.setActionHandler('play', () => {
    if (document.pictureInPictureElement)
        document.pictureInPictureElement.play();
    });

    navigator.mediaSession.setActionHandler('pause', () => {
    if (document.pictureInPictureElement)
        document.pictureInPictureElement.pause();
    });
</script>

<GlyphButton
    glyphName="far fa-image"
    on:click={showPictureInPictureWindow} />