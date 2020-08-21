import { POST } from './requests';


export async function setLiked(id: number, liked: boolean) {
    return POST("/providers/set_liked", { id, liked });
}