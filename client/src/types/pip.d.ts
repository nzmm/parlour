/* Picture-in-Picture */

interface HTMLCanvasElement {
    captureStream?(): MediaProvider;
}

interface HTMLVideoElement {
    requestPictureInPicture?(): Promise<void>;
}

interface HTMLPictureinPictureElement {
    play(): void;
    pause(): void;
}

interface Document {
    pictureInPictureElement?: HTMLPictureinPictureElement;
}