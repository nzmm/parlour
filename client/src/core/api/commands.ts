import { POST } from './requests';


export async function setLiked(id: number, liked: boolean) {
    return POST("/api/set_liked", { id, liked });
}