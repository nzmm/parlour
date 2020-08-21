import { playerState, currentTrack, queue } from '../store';
import { getDownload } from '../api/queries';
import type { ITrack } from '../interfaces/ITrack';

const TIMER_ITERVAL = 500;


export class AudioPlayer {

    private _player = new Audio();
    private _playlist: ITrack[];

    private _timer = 0;
    private _track_id = 0;

    constructor() {
        queue.subscribe(value => this._playlist = value.data);
        this.initEvents(this._player, this._playlist);
    }

    private initEvents(player: HTMLAudioElement, playlist: ITrack[]) {
        player.addEventListener("loadedmetadata", () => {
            playerState.update(cur => ({
                ...cur,
                length: this._player.duration * 1000,
                position: this._player.currentTime * 1000
            }));
        });

        player.addEventListener("canplaythrough", () => {
            this.setPlaying();
        });

        player.addEventListener("ended", () => {
            this.onEnded(playlist);
        });
    }

    private onEnded(playlist: ITrack[]) {
        if (playlist.length) {
            this.playNext(playlist);
        } else {
            this.setPaused(true);
        }
    }

    private playNext(playlist: ITrack[]) {
        const track = playlist.shift();
        this.play(track);
        queue.update(q => ({ ready: true, data: playlist }));
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

    private setPaused(ended: boolean = false) {
        if (!this._player.paused) {
            this._player.pause();
        }

        clearTimeout(this._timer);

        playerState.update(cur => (
            ended ?
                { ...cur, playing: false, position: this._player.duration * 1000 } :
                { ...cur, playing: false }));
    }

    async play(track: ITrack) {
        if (!track.id) {
            return;
        }

        this._track_id = track.id;
        currentTrack.set(track);

        const res = await getDownload(track.id);
        const data = await res.json();

        this.setPaused();
        this._player.src = data.download;
        this._player.load();
    }

    toggle() {
        if (!this._track_id) {
            return;
        }
        if (this._player.paused) {
            this.setPlaying();
        } else {
            this.setPaused();
        }
    }
}