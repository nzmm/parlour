import { playerState } from '../store';
import { getDownload } from '../api/queries';
import type { ITrack } from '../interfaces/ITrack';


const TIMER_ITERVAL = 500;


export class AudioPlayer {

    private _player = new Audio();
    private _timer = 0;

    constructor() {
        this._player.addEventListener("loadedmetadata", () => {
            playerState.update(cur => ({ ...cur, length: this._player.duration * 1000 }));
        });
        this._player.addEventListener("canplaythrough", () => {
            this.setPlaying();
        });
    }

    private updateProgress() {
        if (this._player.paused) {
            clearTimeout(this._timer);
            return;
        }

        playerState.update(cur => ({ ...cur, position: this._player.currentTime * 1000 }));
        this.newTimeout();
    }

    private newTimeout() {
        this._timer = setTimeout(() => this.updateProgress(), TIMER_ITERVAL);
    }

    private setPlaying() {
        playerState.update(cur => ({ ...cur, playing: true }));
        this._player.play();
        this.newTimeout();
    }

    private setPaused() {
        clearTimeout(this._timer);
        playerState.update(cur => ({ ...cur, playing: false }));
        this._player.pause();
    }

    async play(track: ITrack) {
        const res = await getDownload(track.id);
        const data = await res.json();
        console.log(data);

        this.setPaused();
        this._player.src = data.download;
        this._player.load();
    }

    toggle() {
        if (this._player.paused) {
            this.setPlaying();
        } else {
            this.setPaused();
        }
    }
}